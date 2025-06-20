import os
import sys
import hashlib
from datetime import datetime
import smtplib
import ssl
from email.message import EmailMessage
from config import SENDER_EMAIL, SENDER_PASSWORD

def calculatechecksum(path, blocksize = 1024):
    fobj = open(path, "rb")
    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer = fobj.read(blocksize)
    fobj.close()

    return hobj.hexdigest()

def directorywatcher(directoryname):
    flag = os.path.isabs(directoryname)

    if(flag == False):
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)
    if(flag==False):
        print("the path is invalid")
        exit()

    flag = os.path.isdir(directoryname)
    if flag == False:
        print("the path is valid but the traget is not a directory")
        exit()

    for foldername, subfoldername, filenames in os.walk(directoryname):
        for fname in filenames:
            fname = os.path.join(foldername, fname)
            checksum = calculatechecksum(fname)
            print("filename: ", fname)
            print("checksum: ", checksum)
            print()

        filename = "Marvellous\log.txt"
        
        fobj = open(filename, "w")

def findduplicate(directoryname):
    flag = os.path.isabs(directoryname)

    if(flag == False):
        directoryname = os.path.abspath(directoryname)

    flag = os.path.exists(directoryname)
    if(flag==False):
        print("the path is invalid")
        exit()

    flag = os.path.isdir(directoryname)
    if flag == False:
        print("the path is valid but the traget is not a directory")
        exit()

    duplicate = {}

    total_files = 0

    for foldername, subfoldername, filenames in os.walk(directoryname):
        for fname in filenames:
            total_files += 1
            fname = os.path.join(foldername, fname)
            checksum = calculatechecksum(fname)

            if checksum in duplicate:
                duplicate[checksum].append(fname)
            else:
                duplicate[checksum] = [fname]

    return duplicate, total_files

def delete_duplicates(duplicates_dict):
    duplicates = list(filter(lambda x: len(x) > 1, duplicates_dict.values()))
    deleted_files = []

    for group in duplicates:
        for file in group[1:]:  # Keep the first file, delete rest
            try:
                os.remove(file)
                deleted_files.append(file)
            except Exception as e:
                print(f"Failed to delete {file}: {e}")
    
    return deleted_files

def create_log(duplicates):
    if not os.path.exists("Marvellous"):
        os.makedirs("Marvellous")

    log_name = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_path = os.path.join("Marvellous", log_name)

    fobj = open(log_path, 'w')
    fobj.write("Duplicate Files Removed:\n")
    for file in duplicates:
        fobj.write(file + "\n")

    return log_path

def send_mail(to_email, log_file_path, start_time, total_scanned, total_duplicates):
    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD

    msg = EmailMessage()
    msg['Subject'] = 'Duplicate File Removal Report'
    msg['From'] = sender_email
    msg['To'] = to_email

    body = f"""
    Duplicate File Removal Operation Summary:

    Starting Time: {start_time}
    Total Files Scanned: {total_scanned}
    Duplicate Files Deleted: {total_duplicates}

    Please find attached the detailed log.
    """
    msg.set_content(body)

    fobj = open(log_file_path, "rb")
    msg.add_attachment(fobj.read(), maintype="application", subtype="octet-stream", filename=os.path.basename(log_file_path))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)
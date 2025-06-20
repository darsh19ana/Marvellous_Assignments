# design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID, username.
# after creating log file send that log file to the specified mail
# usage: procinfolog.py demo marvellousinfosystem@gmail.com
# demo is the name of the directory
# marvellousinfosystem@gmail.com is the mail id

import psutil
import sys
import os
import smtplib
import ssl
from email.message import EmailMessage
from config import SENDER_EMAIL, SENDER_PASSWORD

def create_log(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

    filepath = os.path.join(foldername, "log.txt")

    with open(filepath, "w") as fobj:
        for proc in psutil.process_iter():
            try:
                info = proc.as_dict(attrs=['pid', 'name', 'username'])
                fobj.write(f"{info}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

    return filepath

def send_email(receiver_email, file_path):
    sender_email = SENDER_EMAIL
    sender_password = SENDER_PASSWORD

    subject = "Process Info Log File"
    body = "Hello this is a test mail"

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    with open(file_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(file_path)
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print(f"Log file sent successfully to {receiver_email}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python procinfolog.py <foldername> <email>")
        return

    foldername = sys.argv[1]
    email = sys.argv[2]

    log_path = create_log(foldername)
    send_email(email, log_path)

if __name__ == "__main__":
    main()

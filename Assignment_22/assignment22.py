# Design automation script which performs following task.

# Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
# Create one Directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
# Name of that log file should contains the date and time at which that file gets created.
# Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
# Accept Mail id from user and send the attachment of the log file.
# Mail body should contains statistics about the operation of duplicate file removal.

# Mail body should contains below things:
    # Starting time of scanning
    # Total number of files scanned
    # Total number of duplicate files found

# Consider below command line options for the gives script
# DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
# - DuplicateFileRemoval.py
# Name of python automation script
# - E:/Data/Demo
# - 50
# Absolute path of directory which may contains duplicate files
# Time interval of script in minutes
# marvellousinfosystem@gmail.com

# Note:
# Mail ID of the receiver
# For every separate task write separate function.
# Write all user defined functions in one user defined module.
# Use proper validation techniques.
# Provide Help and usage option for script.
# Create one Readme file which contains description of our script, details of command line options.
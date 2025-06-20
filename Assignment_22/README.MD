## Description
This script:
- Scans a given directory for duplicate files (based on checksum)
- Deletes the duplicate files
- Logs the deleted files to a timestamped log file in a folder named `Marvellous`
- Sends the log file via email

## Usage:
python DuplicateFileRemoval.py <DirectoryPath> <DelayInMinutes> <ReceiverEmail>
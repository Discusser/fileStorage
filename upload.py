import datetime
import os
import random
import string
import sys
import pyperclip
from datetime import date


def upload():
    argv = sys.argv[1]
    if os.path.getsize(argv) > 100_000_000:
        print("Can't upload files bigger than 100 MB")
        quit()
    randomName = ""
    characters = string.ascii_letters + string.digits
    for char in range(0, 10):
        randomName += random.choice(characters)
    now = datetime.datetime.now()
    today = date.today()
    formattedDate = ("%04d-%02d" % (today.year, today.month))
    filename = randomName + " " + today.isoformat() + " " + ("%02d" % now.hour) + "h" + ("%02d" % now.minute)
    _dir = os.getcwd() + "\\files\\" + formattedDate + "\\"
    if not os.path.exists(_dir):
        os.makedirs(_dir)
    fullFilename = filename + os.path.splitext(argv)[1]
    fullPath = _dir + fullFilename
    os.system("copy \"" + argv + "\" \"" + fullPath + "\"")
    os.system("git remote set-url origin git@github.com:Discusser/fileStorage.git")
    os.system("git fetch --all")
    # Make sure that the local repo is always up to date
    os.system("git checkout origin/main -- README.md run.bat upload.py .gitignore")
    os.system("git add files")
    os.system("git commit -m \"Add file '" + fullFilename + "' (via Python)\"")
    os.system("git push -u origin main")
    os.system("git update-index --assume-unchanged \"" + fullPath + "\"")
    
    link = "https://raw.githubusercontent.com/Discusser/fileStorage/main/files/" + formattedDate + "/" + fullFilename.replace(" ", "%20")
    
    print("Uploaded file at link " + link)
    if not sys.argv[2].__includes__("copyLink=false"):
        pyperclip.copy(link)
        print("Copied link to clipboard")


if __name__ == '__main__':
    upload()

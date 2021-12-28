"""
This python script relies on a library called num2words , it also supports 
    -outputing the number in Ordinal system (First, Second, etc)
    -Outputing in numerous languages

To use it, you don't have to install any libray, the script will check if you have the library installed if not it will do it itself.
Then it will attempt to restart, sometimes it causes an error. But restarting manually once will fix it.

The only requirement is you need to have pip install

Open Cmd and type "pip" and if it doesn't cause any errors then you are good to go. 
Otherwise visit this link to get pip https://phoenixnap.com/kb/install-pip-windows
"""


#System Modules
import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from num2words import num2words
    
    imported=True
except ImportError:
    install("num2words")
    os.execv(sys.executable, ['python'] + sys.arg)

while True:
    try:
        x=int(input("Enter any number: "))
        print(num2words(x))
    except ValueError:
        print("You enterend something that is not an integer.")

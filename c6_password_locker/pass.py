#! python3

# Very insecure password storage for educational purpose only
# requires xsel utility
# sudo apt install xsel

# pass.py

import pyperclip
import sys

PASSWORDS = {"email": "ZW0C2XUfQKnmGiN3Fc2LX55Jb",
             "blog": "nghIzQCDsqJ5r7VKp8f4h",
             "luggage": "672392"}

if len(sys.argv) < 2:
    print("Usage: python pass.py [account] = copy account pasword")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for account: [{}] copied to clipboard!".format(account))
else:
    print("There is no account: {}".format(account))

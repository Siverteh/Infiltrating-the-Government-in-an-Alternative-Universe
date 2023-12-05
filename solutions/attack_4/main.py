import requests
import json
import time


def function():
    target_url = "http://10.13.13.254/login"

    session = requests.Session()

    # Increase the password length by 10 for each attempt
    password_lengths = range(0, 200, 10)

    for password_length in password_lengths:
        # Wait one second between each request in case of rate limiting
        time.sleep(1)
        try:
            payload = {
                "username": "ingrid.nilsen",
                "password": "A" * password_length
            }

            # Send the POST request with JSON data
            response = session.post(target_url, data=json.dumps(payload), timeout=60)

            # Check the response
            if response.status_code == 200:
                print(f"Password length: {password_length}")
                print(response.content)
            else:
                print(f"{password_length} failed with status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    # Close the session after the loop
    session.close()


if __name__ == "__main__":
    function()


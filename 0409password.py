"""Write a Python program to check the validity of a password (input from users).

Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters."""


import re

user_password = input("Enter your password: ")
res_lc = re.search(r'[a-z]', user_password)
res_upc = re.search(r'[A-Z]', user_password)
res_digit = re.search(r'\d', user_password)
res_symbol = re.search(r'[$#@]', user_password)
if 6 <= len(user_password) <= 16 and res_lc and res_upc and res_digit and res_symbol:
    print('Password validation is ok')
else:
    print('Change your password for more secure!')

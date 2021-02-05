import string
import random

password_length = int(input("How many characters should this password be? "))
password_characters = string.ascii_letters + string.digits + string.punctuation
password = []

for x in range(password_length):
    password.append(random.choice(password_characters))

print(''.join(password))

import re

password = input("Enter your password: ")

length = len(password) >= 8
upper = re.search(r"[A-Z]", password)
lower = re.search(r"[a-z]", password)
digit = re.search(r"[0-9]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

score = sum([length, bool(upper), bool(lower), bool(digit), bool(special)])

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")
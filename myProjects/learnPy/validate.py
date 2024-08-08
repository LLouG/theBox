import re
# https://docs.python.org/3/library/re.html


email = input("What's your email? ").strip()


# r for raw string in order to avoid error with the \
# [^@] means any character except @
# if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.com$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|edu|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
     print("Invalid")
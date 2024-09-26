MINIMUM_LENGTH = 3

password = input(f"Password of at least {MINIMUM_LENGTH} characters: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Invalid, password must be at least {MINIMUM_LENGTH} characters. ")
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")

print('*' * len(password))

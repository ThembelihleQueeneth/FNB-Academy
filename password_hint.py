password = input("Enter your password: ").strip()

first_letter = password[0]
last_letter = password[-1]

print(f"\nYour password starts with '{first_letter}' and ends with '{last_letter}'.")
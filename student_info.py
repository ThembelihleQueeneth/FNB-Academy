# student_info.py

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Combine first name and surname
full_name = f"{first_name} {surname}"

# Calculate age in months
age_in_months = age * 12

# Round favourite number to 2 decimal places
rounded_number = round(favourite_number, 2)

# Display formatted profile card
print("\n==============================")
print("     STUDENT PROFILE CARD")
print("==============================")
print(f"Welcome, {full_name}!")
print(f"Name (UPPERCASE): {full_name.upper()}")
print(f"Name (Title Case): {full_name.title()}")
print(f"Age: {age} years")
print(f"Age in Months: {age_in_months}")
print(f"Favourite Number: {rounded_number}")

# Display data types
print("\nData Types:")
print(f"First Name: {type(first_name)}")
print(f"Surname: {type(surname)}")
print(f"Age: {type(age)}")
print(f"Favourite Number: {type(favourite_number)}")
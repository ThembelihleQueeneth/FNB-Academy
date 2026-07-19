# Collect user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio: ")

username = f"{first_name[0]}{last_name}".lower()

full_name = f"{first_name} {last_name}".title()

clean_bio = bio.strip().title()

bio_length = len(clean_bio)

updated_bio = clean_bio.replace("I am", "I'm")

# Display formatted profile
print("\n==============================")
print("     USER PROFILE")
print("==============================")
print(f"Username: {username}")
print(f"Full Name: {full_name}")
print(f"Bio: {updated_bio}")
print(f"Bio Length: {bio_length} characters")
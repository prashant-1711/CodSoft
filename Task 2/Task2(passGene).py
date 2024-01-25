import random
import string

def generate_password(length):
    up_letters = string.ascii_uppercase
    low_letters = string.ascii_lowercase
    digits = string.digits
    special_char = string.punctuation

    all_characters = up_letters + low_letters + digits + special_char

    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            pass_len = int(input("Enter the password length: "))
        except ValueError:
            print("Enter a valid integer for password length.")
            continue

        generated_password = generate_password(pass_len)

        if generated_password:
            print("Generated Password:", generated_password)

        generate_new = input("Would you like to generate a new password? (y/n): ").lower()
        if generate_new != 'y':
            break

if __name__ == "__main__":
    main()

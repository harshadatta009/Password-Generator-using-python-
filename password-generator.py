import random
import string

def generate_password(length):
    # Combine character sets
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Use random.choices for more efficiency and readability
    password = ''.join(random.choices(all_characters, k=length))

    return password

def main():
    # Input the length of the password
    length = int(input("Enter the length of the password: "))

    # Generate and print the password
    password = generate_password(length)
    print(password)

if __name__ == "__main__":
    main()

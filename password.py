
import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user for password length
    while True:
        try:
            length = int(input("Enter the desired password length (8 or more): "))
            if length < 8:
                print("Please choose a length of at least 8.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
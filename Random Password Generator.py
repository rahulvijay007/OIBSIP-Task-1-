import random
import string
def generate_password(length, letters=True, numbers=True, symbols=True):
    characters = ''
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please enable at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter desired password length: "))
        letters = input("Include letters? (y/n): ").lower() == 'y'
        numbers = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, letters, usenumbers, use_symbols)
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid password length.")
if __name__ == "__main__":
    main()
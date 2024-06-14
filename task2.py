import itertools
import re
import string

# Function to load passwords from a file
def load_passwords(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Brute-force attack function
def brute_force_attack(passwords, max_length=3):
    characters = string.ascii_lowercase + string.digits
    found_passwords = []

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess in passwords and guess not in found_passwords:
                found_passwords.append(guess)
    return found_passwords

# Dictionary attack function
def dictionary_attack(passwords, dictionary):
    return [password for password in passwords if password in dictionary]

# Pattern matching attack function
def pattern_matching_attack(passwords, patterns):
    found_passwords = []
    for password in passwords:
        for pattern in patterns:
            if re.fullmatch(pattern, password) and password not in found_passwords:
                found_passwords.append(password)
                break
    return found_passwords

# Combined attack function
def combined_attack(passwords, max_length=3, dictionary=None, patterns=None):
    if dictionary is None:
        dictionary = ['123456', 'password', '123456789', '12345678', '12345', '1234567', 'admin', 'qwerty']
    if patterns is None:
        patterns = [r'[a-z]{3}', r'[a-z]{4}', r'[0-9]{4}', r'password\d*']

    found_passwords = set()

    # Perform brute-force attack
    found_passwords.update(brute_force_attack(passwords, max_length))
    # Perform dictionary attack
    found_passwords.update(dictionary_attack(passwords, dictionary))
    # Perform pattern matching attack
    found_passwords.update(pattern_matching_attack(passwords, patterns))

    return list(found_passwords)

# Main function
def main():
    file_path = input("Enter the path of the password file: ")
    passwords = load_passwords(file_path)

    print("Choose an attack method:")
    print("1. Brute-force attack")
    print("2. Dictionary attack")
    print("3. Pattern matching attack")
    print("4. Combined attack (all of the above)")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        found_passwords = brute_force_attack(passwords)
    elif choice == '2':
        dictionary = ['123456', 'password', '123456789', '12345678', '12345', '1234567', 'admin', 'qwerty']
        found_passwords = dictionary_attack(passwords, dictionary)
    elif choice == '3':
        patterns = [r'[a-z]{3}', r'[a-z]{4}', r'[0-9]{4}', r'password\d*']
        found_passwords = pattern_matching_attack(passwords, patterns)
    elif choice == '4':
        found_passwords = combined_attack(passwords)
    else:
        print("Invalid choice.")
        return

    print("\nResults:")
    for password in found_passwords:
        print(f"Found password: {password}")

    total_passwords = len(passwords)
    cracked_passwords = len(found_passwords)
    if total_passwords > 0:
        success_rate = (cracked_passwords / total_passwords) * 100
    else:
        success_rate = 0

    print(f"\nPercentage of passwords cracked: {success_rate:.2f}%")

if __name__ == "__main__":
    main()

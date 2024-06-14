import itertools  # Add this line to import itertools
import re
import string

# Brute-force attack function
def brute_force_attack(password):
    characters = string.ascii_lowercase + string.digits
    max_length = 5  # Limiting the maximum length for practicality

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess == password:
                return True
    return False

# Dictionary attack function
def dictionary_attack(password, dictionary):
    return password in dictionary

# Pattern matching attack function
def pattern_matching_attack(password, patterns):
    for pattern in patterns:
        if re.fullmatch(pattern, password):
            return True
    return False

# Combined attack function
def combined_attack(password, dictionary, patterns):
    if brute_force_attack(password):
        return "brute-force attack"
    elif dictionary_attack(password, dictionary):
        return "dictionary attack"
    elif pattern_matching_attack(password, patterns):
        return "pattern matching attack"
    else:
        return None

# Main function
def main():
    password = input("Enter the password to check: ")

    # Extended dictionary of common passwords
    dictionary = [
        '123456', 'password', '123456789', '12345678', '12345', '1234567', 'admin', 'qwerty', 'abc123', 'letmein',
        'welcome', 'monkey', '123123', 'football', 'baseball', '1q2w3e4r', 'sunshine', 'iloveyou', '1234', '000000',
        '1qaz2wsx', 'password1', 'zaq1zaq1', 'qazwsx', 'qwertyuiop', '123321', 'superman', 'batman', 'trustno1',
        'freedom', 'whatever', 'princess', 'q1w2e3r4', 'passw0rd', 'michael', 'dragon', 'jordan', 'killer', 'pepper'
    ]

    # Extended patterns for pattern matching attack
    patterns = [
        r'[a-z]{3}', r'[a-z]{4}', r'[0-9]{4}', r'password\d*', r'[a-zA-Z]{5,}', r'[0-9]{6,}', r'[a-zA-Z0-9]{6,}',
        r'[A-Z][a-z]{2}\d{2}', r'\d{2}[a-z]{2}[A-Z]', r'[a-z]{2}\d{2}[A-Z]{2}', r'[A-Z][a-z]{3}[0-9]{2}', r'[a-zA-Z]{6}',
        r'[A-Z]{2}[a-z]{3}[0-9]{1}', r'[a-z]{4}[0-9]{1}', r'[A-Z]{1}[a-z]{3}[0-9]{2}', r'[a-zA-Z0-9]{8}', r'[A-Z]{1}[a-z]{4}[0-9]{3}'
    ]

    attack_method = combined_attack(password, dictionary, patterns)

    if attack_method:
        print(f"The password '{password}' can be cracked by a {attack_method}.")
    else:
        print(f"The password '{password}' could not be cracked by any of the defined methods.")

if __name__ == "__main__":
    main()

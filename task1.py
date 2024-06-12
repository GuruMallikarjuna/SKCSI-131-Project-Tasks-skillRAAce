import re

def evaluate_password(password):
    strength = 0
    suggestions = []
    
    if len(password) > 7:
        strength += 1
    else:
        suggestions.append("Increase the length to at least 8 characters")
    
    if len(password) > 10:
        strength += 1
    else:
        suggestions.append("Increase the length to more than 10 characters")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters")
    
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Add numbers")
    
    if re.search(r'[^A-Za-z0-9]', password):
        strength += 1
    else:
        suggestions.append("Add special characters")
    
    return strength, suggestions

def generate_feedback(strength):
    if strength <= 2:
        return "Weak Password: Consider adding more characters and mixing upper/lowercase, numbers, and special characters."
    elif strength <= 4:
        return "Medium Password: Could be stronger. Add more variety to your password."
    else:
        return "Strong Password: Your password is strong."

def main():
    print("Welcome to skillRAAce Password Strength Checker")
    password = input("Enter your password: ")
    
    strength, suggestions = evaluate_password(password)
    strength_percent = (strength / 6) * 100
    
    print(f"Strength: {strength_percent:.0f}%")
    feedback = generate_feedback(strength)
    print(feedback)
    
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Good job!")

if __name__ == "__main__":
    main()

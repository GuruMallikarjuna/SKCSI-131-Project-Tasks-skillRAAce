**Password Cracking Methods Comparison**
This repository contains two Python scripts that demonstrate different methods for password cracking: Code 1 and Code 2. Each script employs various techniques to crack passwords from a specified list or input.

**Code 1: Multi-method Password Cracking**

**Overview**
1. Features: Allows users to choose between brute-force, dictionary, pattern matching, or combined attacks on passwords loaded from a file.
2. Libraries Used: itertools, re, string.
   
**Functionality:**
1. Brute-force Attack: Generates combinations of lowercase letters and digits up to a specified length.
2. Dictionary Attack: Checks passwords against a predefined list of common passwords.
3. Pattern Matching Attack: Uses regular expressions to match passwords against common patterns.
4. Combined Attack: Sequentially applies all three methods to maximize password discovery.
   
**How to Use**
1. Input File: Provide a file path containing passwords, one per line.
2. Attack Method: Choose an attack type (brute-force, dictionary, pattern matching, or combined) by entering the respective number.
3. Output: Displays passwords found by the chosen method and calculates the success rate of cracking passwords.

**Code 2: Simple Password Cracking Functions**

**Overview**

1. Features: Accepts a single password input and checks it against predefined lists and patterns.
2. Libraries Used: itertools, re, string.
   
**Functionality:**
1. Brute-force Attack: Checks for lowercase letters and digits combinations up to a practical length.
2. Dictionary Attack: Matches passwords against a predefined list of common passwords.
3. Pattern Matching Attack: Uses regular expressions to detect common patterns in passwords.
   
**How to Use**

1. Input Password: Enter a password to check its vulnerability.
2. Output: Indicates if the password can be cracked and which method (brute-force, dictionary, or pattern matching) succeeded.

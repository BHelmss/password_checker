# NIST 800-63B Password Checker

This project implements a password strength checker based on the **NIST Special Publication 800-63B: Digital Identity Guidelines**. It evaluates passwords against modern security standards, focusing on length, usability, and avoidance of common or compromised passwords rather than arbitrary complexity rules.

## Features
- **Minimum Length**: Enforces a minimum of 8 characters, with encouragement for longer passwords (12+).
- **Blacklist Checking**: Cross-references passwords against the `rockyou.txt` list of common passwords.
- **No Complexity Mandates**: Aligns with NIST’s recommendation to avoid forcing specific character types (e.g., special characters, uppercase) unless necessary.
- **User-Friendly Feedback**: Provides clear suggestions for improving weak passwords.

## Prerequisites
- **Python 3.x**: Ensure Python is installed (tested with Python 3.12).
- **rockyou.txt**: File listed in this repo.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BHelmss/password_checker.git
   cd password_checker
2. **Use Mode 1**
    ```bash
    python Password_Checker.py
    Welcome to the NIST 800-63B password compliance checker!!
    Please enter the password you want to check: iloveyou
    Check successful... feedback listed below!!
    Password exists in a common password list, please select a different password.
3. **Use Mode 2**
   ```bash
   python Password_Checker.py -l [/path/to/passwordlist]
   Checking password: kdndlkdl12324
   The password is strong by NIST standards, no changes needed!!
   --------------------------------------------------
   Checking password: iloveyou
   Password exists in a common password list, please select a different password.
   --------------------------------------------------
   Checking password: password
   Password exists in a common password list, please select a different password.
   --------------------------------------------------
   Checking password: 1234
   Password too short, should be longer than 8 characters(12 or more recommended).
   Password exists in a common password list, please select a different password.
   --------------------------------------------------
   

# Warehouse End-Effector for the Quanser QArm

A team project to design a lightweight end-effector that packages items of different shapes and sizes, paired with a Python ordering system that runs the QArm automatically. The goal was to reduce the need for manual labour in warehouses.

<p align="center">
<img width="370" alt="Final CAD model in Inventor" src="https://github.com/user-attachments/assets/5da86000-d9bd-45f6-9678-9bec76dba0c4" />
<img width="320" alt="3D printed end-effector mounted on the QArm" src="https://github.com/user-attachments/assets/851799a3-7316-4e11-8b32-d6fcec2ab5d2" />
</p>
<p align="center"><i>Final CAD model (Inventor) · 3D printed and mounted on the QArm</i></p>

## Objective

Design an end-effector of **100 g or less** that can grip products of varying shapes and sizes, and develop software to manage its operations and decisions.

## The End-Effector

A servo-driven gripper designed in Inventor and 3D printed with PrusaSlicer.

- A gear on the servo motor drives both arms
- Both arms close on the object, so force is applied from both sides
- Gear ratios increase the torque delivered to the arms
- The gears spin freely on axles

<p align="center">
<img width="516" height="399" alt="Picture1" src="https://github.com/user-attachments/assets/7ec48c8c-ada4-4e57-87e1-06ba1f5d69f0" />
</p>
<p align="center"><i>Exploded view of the end-effector assembly</i></p>

## Software System

- **User accounts:** users create a secure account and log in with authentication
- **Inventory:** a barcode scanner reads items and retrieves product info from a CSV database
- **Order processing:** calculates discounts, applies tax, generates a receipt, and records order history in a CSV database
- **Package identification:** barcode scans determine each object's destination and how many items are in the order
- **Automated handling:** the QArm, fitted with the end-effector, picks up each object and places it in the correct parcel location until the whole order is processed

## My Contributions

- Designed the end-effector in Inventor, produced the engineering drawings, and 3D printed the parts
- Wrote the account system (`sign_up()` and `authenticate()`)

**`sign_up()`** checks for duplicate usernames, enforces password rules (6+ characters with an uppercase letter, lowercase letter, digit, and symbol), and saves the password as a bcrypt hash so plain-text passwords are never stored.

**`authenticate()`** sends new users to sign-up, checks the entered password against the stored hash, and returns the user ID once the login is correct.

**Sign-up: password rules and hashing**

```python
# Reject usernames that already exist
if userid in userids:
    print("Error: That userid already exists.")

# Check the password for uppercase, lowercase, digit, and symbol
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_symbols:
        has_symbol = True

if len(password) < 6 or not (has_upper and has_lower and has_digit and has_symbol):
    print("Error: Password must be at least 6 characters with upper, lower, digit, and symbol")

# Hash the password before saving
hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
```

**Login: checking the password**

```python
# Compare the entered password against the stored hash
if bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
    password_valid = True
```

## Outcome

Most of the system worked as intended, but the final demonstration exposed two issues: a formatted string that didn't transfer correctly in the VNC viewer (affecting order completion and the CSV output), and QArm calibration that was off by about a centimetre from our predefined pickup coordinates. The main takeaway was to test in less controlled environments and design for tolerance.

## Tools

`Python` `bcrypt` `Autodesk Inventor` `PrusaSlicer` `Quanser QArm`

## Demo

▶️ **[Watch the QArm Pick up an Item](https://youtube.com/shorts/yu3ImisCyhk?feature=share)**

# Warehouse End-Effector for the Quanser QArm

A team project to design a lightweight end-effector that packages items of different shapes and sizes, paired with a Python ordering system that runs the QArm automatically. The goal was to reduce the need for manual labour in warehouses.

<p align="center">
  <img src="images/final-design.png" width="380">
  <img src="images/printed-model.png" width="380">
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

```python
# Hash the password before saving
hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verify a login attempt against the stored hash
bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8'))
```

## Outcome

Most of the system worked as intended, but the final demonstration exposed two issues: a formatted string that didn't transfer correctly in the VNC viewer (affecting order completion and the CSV output), and QArm calibration that was off by about a centimetre from our predefined pickup coordinates. The main takeaway was to test in less controlled environments and design for tolerance.

## Tools

`Python` `bcrypt` `Autodesk Inventor` `PrusaSlicer` `Quanser QArm`

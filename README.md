# Password Hash Calculator

This Python program calculates a simple hash for a password. 
It splits the password into two blocks, converts each character to its ASCII value, multiplies it by a growing multiplier, and adds the products to a running total. 
Intermediate sums are displayed step by step.

## Features
- Split password into two blocks
- Calculate ASCII value of each character
- Multiplier grows with each character
- Display running total
- Simple and understandable hash calculation

## Usage
1. Install Python 3.x
2. Run `python password_hash.py`
3. Change the password in the `password` variable
4. See table with ASCII values, multiplier, product, and hash

## Note
This is a **simple, educational hash algorithm** and **not suitable for secure passwords**.

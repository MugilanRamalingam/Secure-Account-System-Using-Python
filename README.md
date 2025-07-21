# 🔐 Encrypted Account Manager in Python

A Python-based CLI app for secure login and signup using custom character-mapping encryption. It stores user credentials and personal notes in encoded `.txt` files. Users can securely log in, view, add, or delete their private data.

## 🚀 Features

- User registration with name, email, and password
- Custom encryption and decryption functions
- Secure login verification
- Encrypted data storage per user
- Options to add or delete personal data

## 🔧 How It Works

1. On running the program, the user can:
   - Press `1` to log in
   - Press `2` to create a new account

2. Credentials are encoded using a predefined dictionary.
3. User data is saved in:
   - `database.txt` (stores login info)
   - `[username].txt` (stores personal data)

## 📁 File Structure

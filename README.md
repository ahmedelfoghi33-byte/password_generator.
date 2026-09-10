# &#x20;Secure Password Generator

A simple and secure password generator built with **Python** and **Tkinter**.

##     Features

- Generate strong passwords
- Choose password length from 8 to 128 characters
- Uppercase letters
- Numbers
- Symbols
- Password strength indicator
- Copy password to clipboard
- Show / hide password
- Save generated password to a file
- Uses Python's `secrets` module for secure password generation

## 🛠️ Requirements

- Python 3.10+
- Tkinter

No external Python packages are required.

## 🚀 How to Run

Clone or download the project, then run:

```bash
python password_generator.py
```

## 📁 Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── README.md
```

## ⚠️ Security Note

The current **Save** feature stores the password as plain text.

Do not use it to store important passwords. For a real password manager, passwords should be encrypted and protected with a master password.

## &#x20;License

This project is free to use and modify.

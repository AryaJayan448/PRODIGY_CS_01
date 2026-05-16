# 🔐 PRODIGY_CS_01 - Caesar Cipher

## 📌 Task Overview

> Implement a Python program that can **encrypt** and **decrypt** text using the **Caesar Cipher** algorithm.
> Users can input a message and a shift value to perform encryption and decryption.

This is **Task 01** of the **Prodigy InfoTech Cybersecurity Internship**.

---

## 🔍 What is Caesar Cipher?

The **Caesar Cipher** is one of the oldest and simplest encryption techniques.
It works by **shifting each letter** in the plaintext by a fixed number of positions in the alphabet.

**Example with Shift = 3:**

| Plain Text | A | B | C | H | E | L | O |
|------------|---|---|---|---|---|---|---|
| Encrypted  | D | E | F | K | H | O | R |

So `HELLO` with shift `3` becomes `KHOOR` 🔒

---

## ✨ Features

- ✅ Encrypt any text message
- ✅ Decrypt any Caesar-encrypted message
- ✅ Supports both **uppercase** and **lowercase** letters
- ✅ Preserves **spaces**, **numbers**, and **special characters**
- ✅ Validates shift value input (1–25)
- ✅ Simple interactive menu-driven interface

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Concepts Used:** String manipulation, ASCII values, Modular arithmetic, Loops, Functions

---

## 📁 File Structure
PRODIGY_CS_01/
│
├── caesar_cipher.py   # Main Python program
└── README.md          # Project documentation
---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/AryaJayan448/PRODIGY_CS_01.git
cd PRODIGY_CS_01
```

### 2. Run the program
```bash
python caesar_cipher.py
```

> Make sure Python 3 is installed on your system.

---

## 💻 Sample Output
========================================
CAESAR CIPHER PROGRAM
Options:

Encrypt
Decrypt
Exit

Enter your choice (1/2/3): 1
Enter your message: Hello World
Enter shift value (1-25): 3
Encrypted message: Khoor Zruog
---

## 🧠 How It Works

1. User selects **Encrypt** or **Decrypt**
2. User enters a **message** and a **shift value**
3. Each letter is shifted by the given value using the formula:
   
Encrypted = (original_position + shift) % 26
Decrypted = (original_position - shift) % 26

4. Non-alphabetic characters remain **unchanged**

---

## 👨‍💻 Author

**Arya Jayan**
🔗 [LinkedIn](www.linkedin.com/in/arya-jayan55)
🐙 [GitHub](https://github.com/AryaJayan448)

---

## 🏢 Internship

This project was completed as part of the
**Prodigy InfoTech — Cybersecurity Internship**
📅 May 2026

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

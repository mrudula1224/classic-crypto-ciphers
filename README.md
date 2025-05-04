# Classic & Modern Cryptographic Ciphers 🔐

A compact collection of classical and modern cryptographic algorithms implemented in **Python**. This repository is intended for learning, experimentation, and understanding how traditional and widely-used encryption techniques work under the hood.

---

## 🧠 What’s Included

### 🔸 Classical Ciphers
These are historic encryption algorithms used before the advent of modern cryptography:
- **Caesar Cipher** – Simple substitution using character shifts
- **Playfair Cipher** – Bigram substitution based on a 5x5 key matrix
- **Rail Fence Cipher** – Zigzag transposition cipher

### 🔹 Modern Ciphers
These represent the foundational concepts of modern-day encryption:
- **RSA Cipher** – Asymmetric encryption using large prime numbers
- **DES (Data Encryption Standard)** – Symmetric key block cipher (now deprecated)
- **AES (Advanced Encryption Standard)** – Industry-standard secure encryption

---

## 📁 Repository Structure


> Each file contains a standalone implementation with test examples and optional helper functions.

---

## ⚙️ Requirements

Most algorithms use only standard Python libraries. For AES and DES, you may need:

```bash
pip install pycryptodome

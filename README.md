# Blockchainbased-pwd-manager-and-encrypter
# 🔐 BlockCrypt Vault

### Password Manager and Encrypter using Blockchain and Cryptography

## 📌 Overview

BlockCrypt Vault is a secure desktop-based password manager developed using **Python**, **AES-256 encryption**, and **Ethereum blockchain technology**. The application securely stores encrypted passwords on a blockchain network while ensuring that the user’s master password and encryption key are never stored permanently.

The project combines **cryptography** and **blockchain** concepts to create a decentralized and tamper-resistant password management system.

---

# 🚀 Features

* 🔑 Master Password Authentication
* 🔒 AES-256 Password Encryption
* 🧠 SHA-256 Hashing for Key Generation
* ⛓️ Blockchain-based Password Storage
* 🖥️ Desktop GUI using Tkinter
* 📂 Secure Password Retrieval and Decryption
* 🔄 Real-time Password Refresh
* 🛡️ Zero Plaintext Password Storage

---

# 🏗️ Tech Stack

## 🔧 Frontend

* Python Tkinter

## 🧠 Backend

* Python
* hashlib (SHA-256)
* cryptography library (AES Encryption)

## ⛓️ Blockchain

* Solidity
* Ganache
* Web3.py
* py-solc-x (solcx)

---

# 📂 Project Structure

```plaintext
blockcrypt_vault/
│
├── blockchain/
│   ├── Vault.sol
│   ├── deploy_contract.py
│   ├── contract_interact.py
│   └── __init__.py
│
├── crypto/
│   ├── aes_cipher.py
│   ├── hash_util.py
│   └── __init__.py
│
├── gui/
│   ├── login_screen.py
│   ├── main_window.py
│   ├── add_password.py
│   └── __init__.py
│
├── config.py
├── main.py
├── vault_hash.txt
├── requirements.txt
└── README.md
```

---

# 🔐 How the System Works

## 1️⃣ Master Password Authentication

* User enters a master password during login.
* The password is hashed using SHA-256.
* The hash is stored locally for verification.
* The actual password is never stored.

---

## 2️⃣ AES Key Generation

The AES encryption key is dynamically generated using:

```python
key = sha256(master_password)
```

* The key exists only in memory during runtime.
* The key is regenerated every time the user logs in.
* No encryption key is permanently stored.

---

## 3️⃣ Password Encryption

Before storing a password:

* AES-256 encryption is applied
* CBC (Cipher Block Chaining) mode is used
* A random Initialization Vector (IV) is generated

Example:

```python
encrypted = encrypt(password, aes_key)
```

---

## 4️⃣ Blockchain Storage

Encrypted passwords are stored on a local Ethereum blockchain using a Solidity smart contract.

### Smart Contract Stores:

* Password Label
* AES Encrypted Password

Example Structure:

```solidity
struct Entry {
    string label;
    string encryptedPassword;
}
```

---

## 5️⃣ Password Retrieval

When retrieving passwords:

1. Encrypted data is fetched from blockchain
2. Hex data is converted back to bytes
3. AES decryption is applied
4. Password is displayed in GUI

---

# 🔒 Security Features

* Master password is never stored
* AES key is never stored permanently
* Passwords are encrypted before blockchain storage
* SHA-256 hashing prevents plaintext password exposure
* Blockchain ensures tamper resistance

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/blockcrypt-vault.git
cd blockcrypt-vault
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install web3 cryptography py-solc-x pycryptodome
```

---

## 3️⃣ Start Ganache

* Open Ganache
* Start local blockchain at:

```plaintext
http://127.0.0.1:7545
```

---

## 4️⃣ Deploy Smart Contract

```bash
python blockchain/deploy_contract.py
```

This generates:

* Contract Address
* ABI
* config.py

---

## 5️⃣ Run the Application

```bash
python main.py
```

---

# 🧪 Example Workflow

```plaintext
User Login
    ↓
SHA-256 Hash Generation
    ↓
AES Key Generation
    ↓
Encrypt Password
    ↓
Store Encrypted Data on Blockchain
    ↓
Retrieve Data
    ↓
Decrypt using AES Key
    ↓
Display Password
```

---

# 📖 Cryptographic Concepts Used

| Concept                    | Purpose                      |
| -------------------------- | ---------------------------- |
| AES-256                    | Password Encryption          |
| SHA-256                    | Hashing & Key Generation     |
| CBC Mode                   | Secure Block Cipher Chaining |
| IV (Initialization Vector) | Prevents Pattern Repetition  |
| Blockchain                 | Decentralized Secure Storage |

---

# ⚠️ Limitations

* If the master password is forgotten, passwords cannot be recovered
* Uses local blockchain (Ganache) instead of public blockchain
* No cloud synchronization

---

# 🚀 Future Improvements

* Biometric Authentication
* AES-GCM Encryption
* Password Generator
* Multi-user Support
* Cloud/Distributed Deployment
* Mobile Application Version
* Real Ethereum Testnet Deployment

---

# 👨‍💻 Author

**Kailash NP**

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

* Ethereum
* Ganache
* Solidity
* Python Cryptography Library
* Web3.py
* Tkinter GUI Framework

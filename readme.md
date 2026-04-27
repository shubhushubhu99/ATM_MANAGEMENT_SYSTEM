# 🏧 ATM System — Python Console Application
 
A lightweight, menu-driven ATM simulation built in Python. It supports core banking operations including balance inquiry, cash withdrawal, deposit, and PIN management — all secured by account number and PIN authentication.
 
---
 
## 📋 Table of Contents
 
- [Features](#features)
- [Demo](#demo)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Author](#author)
---
 
## ✨ Features
 
| Feature            | Status      |
|--------------------|-------------|
| Account Authentication | ✅ Implemented |
| Show Balance       | ✅ Implemented |
| Withdraw Balance   | ✅ Implemented |
| Deposit Balance    | 🔧 Coming Soon |
| Change PIN         | 🔧 Coming Soon |
| Exit               | ✅ Implemented |
 
---
 
## 🎬 Demo
 
```
Hello.. How may i assist you?
[1] SHOW BALANCE
[2] WITHDRAW BALANCE
[3] DEPOSITE BALANCE
[4] CHANGE PIN
[5] EXIT
 
Enter your choice : 1
Enter your account number : 2546284
Enter your pin : 1122
Your available balance is 10000
```
 
---
 
## 🚀 Getting Started
 
### Prerequisites
 
- Python **3.10+** (f-string with nested quotes requires 3.12+ for the current syntax)
- No external libraries required — uses Python standard library only
### Installation
 
```bash
# 1. Clone the repository
git clone https://github.com/your-username/atm-system.git
 
# 2. Navigate into the project directory
cd atm-system
 
# 3. Run the application
python atm.py
```
 
---
 
## 📁 Project Structure
 
```
atm-system/
│
├── atm.py          # Main application file
└── README.md       # Project documentation
```
 
---
 
## 🖥️ Usage
 
When you run the program, you are presented with a main menu:
 
```
[1] SHOW BALANCE     → Authenticate and view your current balance
[2] WITHDRAW BALANCE → Authenticate and withdraw an amount
[3] DEPOSITE BALANCE → (Coming Soon)
[4] CHANGE PIN       → (Coming Soon)
[5] EXIT             → Quit the application
```
 
### Authentication Flow
 
Every sensitive operation requires:
1. **Account Number** — a unique numeric ID
2. **PIN** — a 4-digit numeric PIN linked to the account
If either is incorrect, the system prints an error and exits for security.
 
---
 
## 🗄️ Database Structure
 
The application uses an in-memory Python dictionary as its mock database. Each entry follows this schema:
 
```python
database = {
    ACCOUNT_NUMBER: {
        "name":    str,    # Account holder's name
        "balance": int,    # Current account balance (in ₹)
        "pin":     int     # 4-digit security PIN
    }
}
```
 
### Default Test Accounts
 
| Account Number | Name    | Balance | PIN  |
|----------------|---------|---------|------|
| `2546284`      | Shubham | ₹10,000 | 1122 |
| `2546900`      | Saloni  | ₹10,000 | 2233 |
 
> ⚠️ **Note:** This is an in-memory store. All changes (withdrawals, PIN updates) are lost when the program exits. For persistence, integrate a database like SQLite or MySQL.
 
---
 
## 🛣️ Roadmap
 
- [x] Account authentication (account number + PIN)
- [x] Show balance
- [x] Withdraw balance
- [ ] Deposit balance
- [ ] Change PIN
- [ ] Transaction history / mini statement
- [ ] Multiple incorrect PIN lockout
- [ ] Persistent storage with SQLite
- [ ] GUI version using `tkinter`
---
 
## 🤝 Contributing
 
Contributions are welcome! Follow these steps:
 
```bash
# 1. Fork the repository
# 2. Create a feature branch
git checkout -b feature/deposit-balance
 
# 3. Commit your changes
git commit -m "feat: add deposit balance functionality"
 
# 4. Push to your fork and open a Pull Request
git push origin feature/deposit-balance
```
 
Please keep code clean, commented, and consistent with the existing style.
 
---
 
## ⚠️ Disclaimer
 
This project is built purely for **educational purposes**. It is not intended for production use and does not implement real-world banking security standards.
 
---
 
## 👨‍💻 Author
 
**Shubham**
- YouTube: [Your Channel Name](https://youtube.com)
- GitHub: [@your-username](https://github.com)
---
 
> *"Code is like humor. When you have to explain it, it's bad." — Cory House*
 
⭐ If you found this project helpful, consider giving it a star on GitHub!
 
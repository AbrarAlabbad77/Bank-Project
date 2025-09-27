# 🏦 Bank Management System

A simple terminal Python-based banking application that represent real-world operations such as deposits, withdrawals, and transfers.
It supports overdraft handling, account states (active/inactive), and CSV file storage for customer records.

---

## 📌Key Features

* Create and manage customer accounts
* Deposit into savings or checking accounts
* Withdraw funds with overdraft protection
* Transfer money between accounts
* Lock accounts after repeated overdrafts
* Reactivate accounts by depositing funds
* Data stored in a CSV file (`bank.csv`)

---

## 🚀 Getting Started

### Prerequisites

* Python3
* `csv` file

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AbrarAlabbad77/bank_project.git
   cd bank_project
   ```

2. Run the program:

   ```bash
   python3 main.py
   ```

3. Run tests:

   ```bash
   python3 -m unittest test.(file.name.py)

   ```

---

## 🛠️ Project Structure

```
bank_project/
│── bank/
│   ├── account.py       # Deposit, Withdraw, Transfer logic
│   ├── customer.py      # Customer class
│   ├── csv_bank.py      # handle writing, reading CSV file 
│   ├── error.py         # error classed 
│── test/
│   ├── test_csv_bank.py # 
│   ├── test_account.py 
│── main.py              # Entry point
│── README.md            # Project documentation
│── bank.csv             # data
```

---


## 👩‍💻 Author

* **Abrar M.**
  📧 Email: [AbrarAlabbad192@outlook.com](mailto:your-email@example.com)
  🔗 GitHub: [AbrarAlabbad77](https://github.com/AbrarAlabbad77)

# QA Automation Demo (Selenium + API + SQL)

This project demonstrates end-to-end QA automation using:

- **Selenium (Python, pytest)** → Automated login and form validation tests  
- **Postman + Newman** → API testing (REST) with assertions  
- **SQLite3** → SQL validation for backend data consistency  

Tested on **Kali Linux** environment.


## 🔧 Setup Instructions

### 1. Clone the repository

git clone git@github.com:<your-username>/qa-automation-demo.git
cd qa-automation-demo

2. Create virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Install Newman (for API tests)

npm install -g newman


▶️ Running Tests

Run Selenium + API + SQL tests

pytest -v --html=report.html --self-contained-html

📄 Results will be available in report.html.


Run API collection via Newman

newman run demo_api.json


Run SQL validation manually

sqlite3 demo.db "SELECT * FROM users WHERE status='active';"


📂 Project Structure

qa-automation-demo/
│
├── tests/
│   ├── test_login.py        # Selenium login test
│   ├── test_api.py          # API test (Newman runner)
│   ├── sql_validation.py    # SQL validation test
│   └── conftest.py          # Pytest fixtures (WebDriver, hooks)
│
├── demo_api.json            # Postman collection
├── demo.db                  # SQLite sample DB
├── requirements.txt         # Python dependencies
├── report.html              # Test report (generated after pytest run)
└── README.md                # Project documentation


✅ Tech Stack

Python 3.13 + Pytest
Selenium WebDriver (Firefox, Geckodriver)
Postman / Newman
SQLite3


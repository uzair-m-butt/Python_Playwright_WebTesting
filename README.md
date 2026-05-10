# 🎭 Python Playwright Web Testing

A web automation testing framework built with **Python** and **Playwright**, designed to run end-to-end (E2E) tests on web applications with speed and reliability.

---

## 🚀 Features

- End-to-end web testing using Microsoft Playwright
- Written in Python with clean, modular structure
- Supports Chromium, Firefox browsers
- Easy to extend with new test cases
- CI/CD ready (Jenkins, GitHub Actions)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Playwright | Browser automation |
| pytest | Test runner |
| pytest-playwright | Playwright plugin for pytest |

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/uzair-m-butt/Python_Playwright_WebTesting.git
cd Python_Playwright_WebTesting
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Linux/Mac
venv\Scripts\activate           # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers
```bash
playwright install
```

---

## ▶️ Running Tests

### Run all tests
```bash
pytest
```

### Run tests in headed mode (see the browser)
```bash
pytest --headed
```

### Run tests on a specific browser
```bash
pytest --my_browser chromium
pytest --my_browser firefox
```

### Run a specific test file
```bash
pytest tests/test_example.py
```

---

## 📁 Project Structure

```
Python_Playwright_WebTesting/
│
├── Test Files			 # test files
├── data/				 # user credentials in JSON file
├── PageObjects/         # Page Object Models
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🔁 CI/CD

A .yml file configures GitHub Actions to automatically execute tests daily through a scheduled pipeline.


---

## 👤 Author

**Uzair M Butt**
- GitHub: [@uzair-m-butt](https://github.com/uzair-m-butt)

---
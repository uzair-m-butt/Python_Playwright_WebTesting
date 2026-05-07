# 🎭 Python Playwright Web Testing

A web automation testing framework built with **Python** and **Playwright**, designed to run end-to-end (E2E) tests on web applications with speed and reliability.

---

## 🚀 Features

- End-to-end web testing using Microsoft Playwright
- Written in Python with clean, modular structure
- Supports Chromium, Firefox, and WebKit browsers
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
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
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
├── tests/               # Test files
├── pages/               # Page Object Models (if used)
├── requirements.txt     # Python dependencies
├── Jenkinsfile          # Jenkins CI/CD pipeline
└── README.md            # Project documentation
```

---

## 🔁 CI/CD

This project includes a **Jenkinsfile** to run tests automatically every day via a scheduled Jenkins pipeline.

See [`Jenkinsfile`](./Jenkinsfile) for the full pipeline configuration.

---

## 👤 Author

**Uzair M Butt**
- GitHub: [@uzair-m-butt](https://github.com/uzair-m-butt)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

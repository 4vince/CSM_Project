# Bisection Method Calculator - Setup Guide

This guide will help you set up and run the **Bisection Method Calculator application**, a simple tool for finding the roots of polynomial equations using the Bisection Method. No prior experience is required—just follow the steps below.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
- **pip** (Python package manager) which comes with python
- **Web browser** (Chrome, Firefox, Edge, etc.)

---

## Project Structure
Your project folder should look like this:
```
CSM_Project/
├── src/
│ ├── main.py
│ ├── bisection_method.py
│ ├── polynomial.py
├── gui/
│ ├── index.html
│ ├── style.css
│ └── script.js
├── backend/
│ └── app.py
├── requirements.txt
├── README.md
└── SETUP_GUIDE.md
```
---

### Step 1: Install Required Packages
Open your **Command Prompt** or **Terminal** and enter:

```bash
python -m pip install flask flask-cors numpy matplotlib
```
Or install everything from the requirements file:
```bash
python -m pip install -r requirements.txt
```

### Step 2: Start the Web Application
If you extracted the files in you chosen directory for example : C:\Users\ravon\Documents\CSM_Project\

There are 2 ways you can start the web application:

### Methods of Using the Application

### Method 1: Web GUI (Recommended)
1. Open http://localhost:5000 in your browser
2. Enter polynomial degree and coefficients
3. Set lower and upper bounds
4. Specify tolerance (relative error %)
5. Click "Solve" to see results and plot

You will see:
- The approximate root
- A table showing each iteration
- A graph of the function and the root

### Method 2: Command Line Interface
1. Open a terminal window
2. Navigate to the project folder:
```bash
cd C:\Users\ravon\Documents\CSM_Project\backend
```
3. Start the server:
```bash
python app.py
```
If successful, the terminal will show that the server is runnig.

### Step 3: Open the Calculator
In your browser, go to:
```bash
http://localhost:5000
```
To stop the server lator, press:
```bash
CTRL + C
```
Or just close the terminal.

---




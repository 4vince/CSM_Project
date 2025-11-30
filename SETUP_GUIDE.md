# Bisection Method Calculator - Setup Guide

This guide will help you set up and run the Bisection Method Calculator application.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Web browser** (Chrome, Firefox, Edge, etc.)

## Quick Setup

### Step 1: Check Your Project Structure
Ensure your project has this structure:
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
├── SETUP_GUIDE.md


### Step 2: Install Dependencies
Open terminal/command prompt and run:
# Install required Python packages
pip install flask flask-cors numpy matplotlib

### Step 3: Run the Application
If you extracted the files in you chosen directory for example : C:\Users\ravon\Documents\CSM_Project\

# Navigate to the backend directory and copy the directory 
then tyoe: cd (directory)
example: cd C:\Users\ravon\Documents\CSM_Project\backend

# Start the web server
python app.py

### Step 4: Access the Application
Open your web browser and go to:
http://localhost:5000

### To close the application 
exit the command prompt 

### Methods of Using the Application

### Method 1: Web GUI (Recommended)
1. Open http://localhost:5000 in your browser
2. Enter polynomial degree and coefficients
3. Set lower and upper bounds
4. Specify tolerance (relative error %)
5. Click "Solve" to see results and plot

### To close the application 
exit the command prompt 

### Method 2: Command Line Interface
# Navigate to src directory
cd src
example: cd C:\Users\ravon\Documents\CSM_Project\src

# Run the CLI version
python main.py


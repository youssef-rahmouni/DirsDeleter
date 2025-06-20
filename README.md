# 🧹 DirsDeleter

**DirsDeleter** is a small Python script I built while learning programming. It helps delete directories that contain files with special permissions (like executables or locked files) — which often cause errors when deleted manually or with basic scripts.

---

## 🚀 Why I Created It

Sometimes, when I try to delete a folder that includes:

- 🛑 Executable files  
- 🔒 Read-only files  
- 📂 Nested subdirectories  

The system shows an error or stops the deletion process.  
This tool solves that by:

- Entering the folder step-by-step  
- Deleting all files and subfolders  
- Finally removing the empty folder itself  

---

## ⚙️ Key Features

- ✅ Recursively deletes any non-empty folder  
- 🔐 Handles permission-protected files  
- 🧾 Shows logs of deleted files and folders  
- 🧹 Cleans up `__pycache__` directories  
- 🐍 Simple command-line interface  
- 🧪 Comes with a test file (`unittest`)  

---

## 💡 Who is it for?

This script is made for:

- Beginners learning Python  
- Users who want to clean up directories fast  
- Anyone needing a quick tool to remove “stubborn” folders  

---

## 📦 Project Overview

- `DirsDeleter.py` → Main logic that deletes files and folders  
- `RunDeleter.py` → Interactive script you can run in terminal  
- `tests/test_DirsDeleter.py` → Automated test to verify that it works  

---

## ▶️ How to Use

### Requirements

- Python 3.x

### Run the tool

```bash
python RunDeleter.py
```

### Run the test
```bash
python -m unittest discover -s tests
```

---

## ⚠️ Disclaimer

It’s not a professional tool — just a simple script I made while learning Python, but it works well and solves a real problem.


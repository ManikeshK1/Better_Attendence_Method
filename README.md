# Better_Attendence_Method
This system reimagines classroom management by replacing slow, sequential roll calls with a rapid, randomized entry method. It allows students to call out roll numbers in any order they sit on bench in class while the teacher uses shorthand input to update records. This simple approach minimizes manual effort, saves time, reduces proxy attendance.

# 🎓 Smart Attendance System 🚀

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)](https://www.python.org/)

A powerful, multi-branch attendance management system designed to eliminate the burden of manual roll calls. Whether you are online using **Google Colab** or offline with a **Modern Desktop App**, this tool handles mixed branch roll numbers (CSE, DSAI, ECE) with ease! 🏫✨

---

## 🌟 Key Features
* **⚡ Rapid Entry:** Just type the last 3 digits (e.g., `1 12 45`) instead of full IDs.
* **🤖 Multi-Branch Support:** Auto-prefixes for **23BCS** (CSE), **23BDS** (DSAI), and **23BEC** (ECE).
* **📅 Smart Dating:** Automatically creates new columns for today's date or uses existing ones.
* **🛡️ Proxy Prevention:** Alerts you if a roll number is already marked present.
* **💻 Dual Mode:** Works via Google Sheets (Cloud) or Excel (Offline).

---

## 🛠️ Installation & Usage

### Method 1: Google Colab (Cloud Sync) ☁️
*Best for syncing directly to a shared Google Sheet.*
1. Open `Colab_Attendance.ipynb` in **Google Colab**.
2. Run the **Setup Cell** to authenticate your Google Account.
3. Enter your **Sheet URL** when prompted.
4. Input the date once, then use the branch-specific text boxes to enter roll numbers.
5. Click **Submit** to update the cloud sheet instantly!

### Method 2: Python Desktop App (Offline) 🖥️
*Best for local use with a beautiful GUI.*
1. **Install dependencies:**
   ```bash
   pip install customtkinter pandas openpyxl

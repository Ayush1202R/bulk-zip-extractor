# 📂 Bulk ZIP Extractor

A clean, simple, and efficient **Streamlit application** that extracts multiple ZIP files and organizes them automatically.  
The tool creates separate folders for each ZIP file and removes the original ZIPs after extraction—making bulk file management fast and convenient.

---

## 🚀 Features

- Detects all `.zip` files inside the selected folder  
- Extracts each ZIP into **its own subfolder**  
- Automatically **removes original ZIP files** after extraction  
- Real-time **progress bar**  
- Clean and user-friendly UI  
- Lightweight — uses only Python built-ins and Streamlit

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **zipfile** (built-in)
- **os** (built-in)

---

## ▶ How to Run Locally

```bash
pip install streamlit
streamlit run app.py

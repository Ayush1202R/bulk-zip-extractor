# 📂 Bulk ZIP Extractor

[![GitHub license](https://img.shields.io/github/license/Ayush1202R/bulk-zip-extractor?style=flat-square)](https://github.com/Ayush1202R/bulk-zip-extractor/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ayush1202R/bulk-zip-extractor?style=flat-square)](https://github.com/Ayush1202R/bulk-zip-extractor/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/Ayush1202R/bulk-zip-extractor/pulls)
[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?style=flat-square)](https://bulk-zip-extractor.streamlit.app/)

A clean, lightweight **Streamlit application** that automates the extraction and organization of multiple ZIP files in a directory. 

The application automatically scans a designated target directory, extracts each archive into its own custom subdirectory (preventing file clashes), and securely cleans up the source ZIP files upon successful extraction.

---

## 🌟 Key Features

* **Auto-Discovery**: Scans and indexes all `.zip` files in the specified path.
* **Organized Unpacking**: Creates a matching directory for each archive to keep file trees clean.
* **Secure Post-Cleanup**: Deletes the original compressed ZIP files only *after* confirming complete and successful extraction.
* **Real-time Monitoring**: Streamlit progress bar displaying extraction status.
* **Zero Bloat**: Built purely using Python standard library packages (`zipfile`, `os`, `shutil`) and Streamlit.

---

## 📂 Project Structure

```text
bulk-zip-extractor/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
├── CONTRIBUTING.md
├── LICENSE                  # MIT License
├── README.md                # Documentation
└── app.py                   # Streamlit UI & extraction execution flow
```

---

## 🛠️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Ayush1202R/bulk-zip-extractor.git
cd bulk-zip-extractor
```

### 2. Install dependency
```bash
pip install streamlit
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

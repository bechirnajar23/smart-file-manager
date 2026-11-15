# Smart File Manager (v1.0.0)

A modular, lightweight, and robust Python-based file management utility designed to automatically scan directories, organize files by their extensions, detect exact duplicates using cryptographic hashing, and generate structured execution reports.

---

## Features (v1.0.0)

* **Recursive Scanning (`pathlib`)**: Deeply explores source directories and safely collects all files while handling permission errors gracefully.
* **Smart Organization (`shutil`)**: Automatically categorizes files into structured folders (`document`, `image`, `video`, `audio`, `archive`, `script`, `package`) based on their extensions.
* **Duplicate Detection (`hashlib`)**: Computes **MD5 hashes** of files using chunk-based reading to accurately detect identical files regardless of their names, without risking memory overload.
* **JSON Reporting (`json`)**: Cleans paths and saves a detailed execution report containing statistics and detected duplicate groups into a structured JSON file (`report_file_manager.json`).
* **Modular Architecture**: Built following clean code principles with separated responsibilities across distinct modules.

---

## Technologies Used

* **Python 3.x**
* `pathlib` (Modern path manipulation)
* `shutil` (High-level file operations)
* `hashlib` (MD5 checksum generation)
* `json` (Data serialization)

---

## Project Structure

```text
smart-file-manager/
│
├── scanner.py           # Recursively scans and collects files
├── organizer.py         # Classifies and moves files into extension-based folders
├── duplicate_finder.py  # Detects true file duplicates using MD5 hashing
├── reporter.py          # Handles data cleaning and JSON report generation
├── main.py              # CLI orchestrator running the full workflow
└── README.md            # Project documentation
```
---
## Installation & Setup

git clone [https://github.com/bechirnajar23/smart-file-manager.git](https://github.com/bechirnajar23/smart-file-manager.git)
cd smart-file-manager

---
## How To use

python main.py

---

## Future Perspectives & Roadmap

- **Extended File Type Support**: Expand the extension mapping dictionary to support specialized formats and custom user-defined configuration rules in future releases.
- **Graphical User Interface (GUI)**: Build an intuitive desktop interface (using CustomTkinter or PyQt) to allow drag-and-drop directory selection and visual storage management.
- **AI-Powered File Agent**: Integrate an intelligent LLM-based agent capable of reading document contents (PDFs, text files) to perform semantic classification (smart sorting of invoices, resumes, and academic notes) and automated file renaming.

---

## Author

Developed by **Bechir Najjar** as a practical Python project demonstrating modular software design and file system manipulation.

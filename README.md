# Python Code Quality Checker

[![Python](https://img.shields.io/badge/python-3.8+-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A Python tool to analyze code quality, maintainability, and complexity. Automatically detects PEP8 violations, syntax errors, and calculates cyclomatic complexity to help developers write cleaner, more maintainable code.


## 🔍 Features
- Detects **PEP8 violations** in Python scripts.
- Identifies **syntax errors**.
- Calculates **cyclomatic complexity** and **maintainability index**.
- Generates **JSON** and **HTML** reports for easy review.


## 🛠️ Technologies Used
- Python
- Jupyter Notebook
- [Radon](https://pypi.org/project/radon/) – for complexity analysis
- [Pylint / Flake8](https://pypi.org/project/flake8/) – for style checking


## 📂 Project Structure
code_quality_checker/
├── reports/ # Generated JSON and HTML reports
├── scripts/ # Sample Python scripts for analysis
├── Code_Quality_Check.ipynb # Main notebook
├── requirements.txt # Project dependencies
└── README.md

Clone the repository:

git clone https://github.com/aditivir29/code_quality_checker.git
cd code_quality_checker

Launch Jupyter Notebook:

jupyter notebook

Open Code_Quality_Check.ipynb and follow the instructions to analyze Python scripts.

📈 Output

JSON report: reports/analysis_report.json
HTML report: reports/analysis_report.html
Metrics include:
Cyclomatic Complexity
Maintainability Index
PEP8 Violations
Syntax Errors

📝 Future Enhancements

Add GUI interface for easier interaction.
Integrate automated GitHub repository analysis.
Support multiple languages beyond Python.

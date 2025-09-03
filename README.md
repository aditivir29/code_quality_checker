# Python Code Quality Checker

## Overview
A Python tool in Jupyter Notebook that analyzes scripts for PEP8 violations, syntax errors, cyclomatic complexity (CC), and maintainability index (MI). Generates numeric metrics, suggestions, and JSON/HTML reports with visualizations.

## Features
- PEP8 & syntax checking with line-level suggestions  
- Cyclomatic complexity & maintainability index per function  
- Dynamic file selection and interactive analysis in Jupyter Notebook  
- JSON and HTML reports with visual highlights  

## Tech Stack
Python 3.x, radon, pandas, pycodestyle/autopep8, matplotlib/seaborn  

## Project Structure
Code_Quality_Checker/
├─ src/                          # Python modules for analysis
│  ├─ pep8_checker.py            # PEP8 violation checker
│  ├─ syntax_checker.py          # Syntax error checker
│  ├─ scoring.py                 # Calculates overall score
│  ├─ suggestions.py             # Generates improvement suggestions
│  ├─ visualizer.py              # Visualization of code issues
│  ├─ report_generator.py        # Saves JSON & HTML reports
│  └─ features.py                # Cyclomatic complexity & maintainability analysis
├─ data/                         # Sample Python files for testing
│  ├─ sample.py
│  └─ sample1.py
├─ reports/                      # Saved analysis reports (JSON & HTML)
├─ Code_Quality_Check.ipynb      # Main notebook for interactive analysis
├─ requirements.txt              # Dependencies
└─ README.md                     # Project description

## How to Run
1. Open `Code_Quality_Check.ipynb` in Jupyter Notebook  
2. Select a Python file from the `data/` folder  
3. Run all cells to see analysis results and reports  

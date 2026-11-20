# Week 5: Python Programming for Testers

## Overview

This repository contains the completed tasks and practical exercises of Week-5.

## Learning Objectives
- Understand Python installation, setup and execution.
- Work with Python variables, data types and operators.
- Use conditional statements and loops.
- Understand and implement functions.
- Work with Python data structures.
- Perform string manipulation.
- Handle exceptions and errors.
- Read and process CSV and JSON files.
- Solve beginner level Python programming exercises.
- Validate structured test data using Python.
- Understand basic Git and GitHub operations.
---

## 1. Python Environment Setup

### Topics Covered

- Python installation and configuration.
- Understanding the Python interpreter.
- Using an IDE (Visual Studio Code).
- Creating and activating virtual environments.
- Installing Python packages using pip.
- Executing Python scripts from the terminal.

---

## 2. Python Fundamentals

### 2.1 Variables and Data Types

### 2.2 Operators

### 2.3 Conditional Statements

### 2.4 Loops

### 2.5 Functions

### 2.6 Python Data Structures

### 2.7 String Manipulation

### 2.8 List Comprehension

### 2.9 Exception Handling

### 2.10 File Handling

### 2.11 CSV file Validation
---

## 3. Python Practice Exercises

The exercises cover:

1. Conditional calculations using functions.
2. Printing characters at even indices of a string.
3. Working with lists and loops.
4. Dictionary operations and merging dictionaries.
5. Counting character occurrences in a string.
6. String manipulation and case conversion.
7. Filtering elements using conditions.
8. List comprehension.
9. Working with numbers and mathematical operations.
10. Using conditional statements.
11. Iterating through collections.
12. Working with tuples and sets.
13. Dictionary key-value operations.
14. Creating and calling functions.
15. Handling user input.
16. Filtering strings based on length and starting characters.

Each exercise is maintained in an individual Python file for practice and reference.

---

## 4. Practical Task: CSV Test Data Validation

Develop a Python script that reads a CSV test-data file, validates each record against predefined rules, identifies invalid data, and generates a pass/fail summary.

### Technologies Used
- Python 3
- Pandas
- CSV

### Validation Requirements

| Field | Validation Criteria |
|---|---|
| Name | Must not be empty |
| Age | Must be a valid integer between 0 and 100 |
| Grade | Must be A, B, C, D, or F |
| Mark | Must be numeric and between 0 and 100 |

### Implementation

The CSV validation script (`valid.py`) uses Pandas to read and process the test data.

The script performs the following operations:

1. Reads the CSV file using `pd.read_csv()`.
2. Checks if the required column names are present in the correct order.
3. Iterates through each row using `iterrows()`.
4. Validates the Name, Age, Grade and Mark fields.
5. Identifies empty, invalid or out-of-range values.
6. Stores validation errors for each individual row.
7. Displays PASS or FAIL results for every row.
8. Calculates the total number of passed and failed rows.
9. Displays a final validation summary.

---

## 5. Git and GitHub

Learned the basics of version control and repository management using Git and GitHub.

### Topics Covered

- Understanding version control.
- Initializing a Git repository.
- Tracking changes.
- Staging files.
- Creating commits.
- Managing branches.
- Connecting a local repository to GitHub.
- Pushing code to a remote repository.

### Common Git Commands

```bash
# Initialize repository
git init

# Check repository status
git status

# Stage all changes
git add .

# Commit changes
git commit -m "Complete Week 5 Python tasks"

# Rename branch
git branch -M main

# Add remote repository
git remote add origin <repository-url>

# Push changes
git push -u origin main

# View commit history
git log
```

---

## 6. Project Folder Structure

The repository is organized to keep Python exercises, CSV validation files, and documentation separate.

```text
program/
│
├── ex1.py
├── ex2.py
├── ex3.py
├── ex4.py
├── ...
├── ex9.py
│
├── valid.py
├── test_data.csv
│
├── README.md
```

---

## 7. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/bsg-tasnim/python_exercises.git
```

### Step 2: Navigate to the Project Directory

```bash
cd python_exercises
```

### Step 3: Create and Activate the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Required Dependencies

```bash
pip install pandas
```

### Step 5: Run Individual Python Exercises

```bash
python3 ex1.py
```

Replace `ex1.py` with the exercise file you want to execute.

### Step 6: Run the CSV Validation Script

```bash
python3 valid.py
```

The validation results and summary will be displayed in the terminal.

---

# Student Performance Analytics System

## INSIGHTX

A Python-based Student Performance Analytics System that analyzes
student academic data using Python, NumPy, and Pandas.

---

## Project Overview

INSIGHTX is a student performance analysis system designed to
process academic records and generate meaningful performance
statistics.

The system calculates student totals, averages, grades,
pass/fail status, rankings, subject-wise performance, and
attendance statistics.

It also provides visual charts and an interactive menu for
exploring the results.

---

## Objectives

- Analyze student academic performance
- Calculate total and average marks
- Assign grades automatically
- Identify pass/fail students
- Find top-performing students
- Perform subject-wise analysis
- Analyze attendance
- Provide visual representation of results
- Create a simple interactive analytics system

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| NumPy | Numerical calculations |
| Pandas | Data loading and analysis |
| Matplotlib | Data visualization |
| CSV | Student dataset storage |
| VS Code | Development environment |
| GitHub | Project repository |

---

## Dataset

The project uses a CSV dataset containing student information.

### Dataset Fields

- Student ID
- Name
- Department
- Python Marks
- SQL Marks
- Mathematics Marks
- AI Marks
- Attendance

The dataset contains 20 student records.

---

## Main Features

### 1. Student Performance Calculation

The system calculates:

- Total marks
- Average marks
- Grade
- Pass/Fail status
- Performance level

### 2. Student Ranking

Students are ranked according to their average marks.

### 3. Top Performers

The system identifies the top-performing students in the class.

### 4. Student Search

A student can be searched using their Student ID.

### 5. Subject Analysis

The system calculates the average performance for each subject.

### 6. Attendance Analysis

The system calculates average attendance and identifies
students above and below the 75% attendance level.

### 7. Visual Analytics

The project generates charts for:

- Subject-wise performance
- Top 10 student performance
- Grade distribution
- Attendance vs academic performance

---

## Grading System

| Average Marks | Grade |
|---------------|-------|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

A student is considered **Pass** when every subject mark is at
least 40 and attendance is at least 75%.

---

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── charts.py
├── students.csv
└── README.md
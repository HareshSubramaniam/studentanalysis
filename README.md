# Student Performance Analytics System

An end-to-end, menu-driven Python application developed as an internship mini-project for **EWB EDUTECH ("Python with AI")**.

---

## 1. Project Overview

The **Student Performance Analytics System** is designed to help educational institutions, mentors, and academic administrators efficiently analyze student academic performance. Built using fundamental Python concepts, **Pandas**, and **NumPy**, this system processes academic data from CSV files, calculates totals and averages, assigns letter grades, evaluates multi-subject pass/fail criteria, tracks attendance thresholds, and generates insightful summary reports.

---

## 2. Problem Statement

Manual compilation and analysis of student examination marks and attendance across multiple subjects is time-consuming, prone to calculation errors, and lacks instantaneous analytical insights. Academic mentors need an automated yet transparent system to:
- Quickly identify students who need academic intervention or counseling.
- Detect subject-level strengths and weaknesses across departments.
- Flag attendance shortages without prematurely penalizing students before administrative review.

---

## 3. Project Objectives

- **Automate Academic Calculations:** Accurately compute total marks, percentage averages, and class rankings without manual errors.
- **Enforce Consistent Grading & Pass Rules:** Implement configurable grade thresholds and enforce subject-specific passing rules (minimum 40 marks in every subject).
- **Separate Academic Performance from Attendance:** Track attendance deficits (< 75%) separately to ensure fair academic evaluations while flagging compliance warnings.
- **Provide Actionable Insights:** Deliver immediate statistical breakdowns, including top performers, subject-wise averages, and overall pass percentages.
- **Maintain High Code Quality:** Build clean, modular, and beginner-friendly code with automated unit testing and robust data validation.

---

## 4. Technologies Used

- **Language:** Python (3.10+)
- **Data Manipulation:** [Pandas](https://pandas.pydata.org/)
- **Numerical Calculations:** [NumPy](https://numpy.org/)
- **Data Storage:** Comma-Separated Values (`CSV`)
- **Testing Framework:** Python Standard Library `unittest`
- **Version Control:** Git & GitHub

---

## 5. System Features

1. **Tabular Student Record Display:** Full class ledger showing individual subject marks, total score, percentage, grade, pass/fail result, and attendance status.
2. **Individual Student Report Card:** Instant search by Student ID or Name to view a detailed breakdown of individual marks and eligibility.
3. **Subject-Wise Analysis:** Calculates average scores for each subject and automatically highlights the highest-performing and lowest-performing subjects.
4. **Top 3 Performers Recognition:** Identifies and ranks the top 3 academic achievers in the class based on average marks.
5. **Pass / Fail Statistics:** Calculates total passed students, failed students, and overall pass percentage based on the strict rule that every subject must be passed.
6. **Attendance Shortage Monitoring:** Analyzes attendance metrics and filters all students with attendance below 75% for mentor follow-up.
7. **Comprehensive Class Summary:** Executive dashboard displaying class averages, high/low boundaries, pass rate, and subject rankings.
8. **Interactive CLI Menu:** Clean, user-friendly command-line interface with thorough input validation and graceful exit handling.

---

## 6. Dataset Description

The dataset is stored in `students.csv` and contains realistic sample student records representing diverse performance levels across four departments: Computer Science, Information Technology, AI & Data Science, and Electronics.

### Dataset Schema:
| Column Name | Data Type | Range / Format | Description |
| :--- | :--- | :--- | :--- |
| `Student_ID` | String | e.g., `S101` | Unique student identifier |
| `Name` | String | Text | Full student name |
| `Department` | String | Text | Academic department / branch |
| `Mathematics` | Numeric | 0 to 100 | Marks scored in Mathematics |
| `Python` | Numeric | 0 to 100 | Marks scored in Python Programming |
| `Artificial_Intelligence` | Numeric | 0 to 100 | Marks scored in Artificial Intelligence |
| `Database` | Numeric | 0 to 100 | Marks scored in Database Management |
| `Attendance` | Numeric | 0.0 to 100.0 | Overall attendance percentage |

> **Note:** The dataset contains 28 sample student records created specifically for demonstration and testing purposes.

---

## 7. Grading and Pass/Fail Rules

### Grading Criteria (Configurable)
Letter grades are assigned based on the student's average percentage:

| Average Marks Range | Grade | Description |
| :---: | :---: | :--- |
| **>= 90%** | **A+** | Outstanding Performance |
| **>= 80%** | **A** | Excellent Performance |
| **>= 70%** | **B** | Very Good Performance |
| **>= 60%** | **C** | Good Performance |
| **>= 50%** | **D** | Average Performance |
| **>= 40%** | **E** | Pass (Minimum Threshold) |
| **< 40%** | **F** | Fail |

### Pass / Fail Rule
- **Rule:** A student is awarded a **PASS** result **only if they score at least 40 marks in every single subject** (`Mathematics >= 40`, `Python >= 40`, `Artificial_Intelligence >= 40`, and `Database >= 40`).
- If a student scores less than 40 marks in even one subject, their final result is **FAIL**, regardless of whether their overall average is high.

### Attendance Policy
- **Threshold:** Minimum acceptable attendance is **75.0%**.
- **Rule:** Attendance below 75% is flagged separately with an alert (`[LOW]`) for counseling. In accordance with project requirements, low attendance does **not** automatically fail a student academically unless explicitly mandated.

---

## 8. Project Structure

```text
student-performance-analytics/
│
├── main.py                   # Main CLI entry point and menu controller
├── functions.py              # Modular business logic, math calculations & validation
├── test_analytics.py         # Automated unit test suite (unittest)
├── students.csv              # Sample student dataset (28 records)
├── requirements.txt          # Python external dependencies (pandas, numpy)
├── README.md                 # Project documentation and guide
├── Project_Documentation.md  # Detailed project report for EWB internship
│
└── screenshots/
    └── output.png            # Actual console execution screenshot
```

---

## 9. Installation & Setup Instructions

### Prerequisites
- Python 3.10 or higher installed on your system.
- `pip` package manager.

### Step 1: Clone or Navigate to the Project Directory
```bash
cd student-performance-analytics
```

### Step 2: Create and Activate a Virtual Environment
- **On Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **On Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### Step 3: Install Required Libraries
```bash
pip install -r requirements.txt
```

---

## 10. Execution Commands

### To Run the Interactive Application:
```bash
python3 main.py
```

### To Run Automated Unit Tests:
```bash
python3 -m unittest -v test_analytics.py
```

---

## 11. Sample Output

### Overall Class Performance Summary:
```text
======================================================================
  OVERALL CLASS PERFORMANCE SUMMARY
======================================================================
Total Number of Students    : 28
Overall Class Average       : 70.54%
Highest Student Average     : 95.75% (Sneha Kulkarni - S104)
Lowest Student Average      : 33.75% (Varun Menon - S121)
-----------------------------------------------------------------
Total Passed Students       : 23 / 28 (82.14%)
Total Failed Students       : 5 / 28 (17.86%)
-----------------------------------------------------------------
Best-Performing Subject     : Artificial_Intelligence (72.68 avg)
Lowest-Performing Subject   : Mathematics (67.93 avg)
-----------------------------------------------------------------
Attendance Shortage (<75%)  : 7 student(s)
=================================================================
```

### Top 3 Performers:
```text
======================================================================
  TOP 3 PERFORMERS OF THE CLASS
======================================================================
Rank   ID     Name                   Department         Total   Average  Grade
---------------------------------------------------------------------------
#1     S104   Sneha Kulkarni         Computer Science   383     95.75    A+
#2     S126   Deepa Krishnan         Computer Science   382     95.50    A+
#3     S120   Neha Saxena            AI & Data Science  373     93.25    A+
---------------------------------------------------------------------------
```

---

## 12. Future Enhancements

- **Data Exporting:** Export student reports into formatted PDF or Excel workbooks.
- **Data Visualizations:** Generate distribution histograms, bar charts, and attendance heatmaps using Matplotlib/Seaborn.
- **Dynamic Student Entry:** Allow administrators to add, update, or remove student records directly through the CLI interface.
- **Department-Specific Filtering:** Enable departmental breakdown and cross-branch comparative analytics.

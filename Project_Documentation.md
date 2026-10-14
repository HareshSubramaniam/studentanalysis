# Project Documentation: Student Performance Analytics System

---

## 1. Project Title and Student Details

- **Project Title:** Student Performance Analytics System
- **Internship Program:** EWB EDUTECH - "Python with AI" Internship Mini Project
- **Student Name:** Haresh Subramaniam
- **Student ID / Roll No:** `[Student ID / Roll Number Here]`
- **College / University:** `[College / University Name Here]`
- **Mentor / Trainer:** Senior Python Developer & Project Mentor
- **Submission Date:** October 2026

---

## 2. Objective

The primary objective of this mini-project is to develop a reliable, command-line **Student Performance Analytics System** using fundamental Python programming, **Pandas**, and **NumPy**.

The project aims to:
1. Load, validate, and clean student records stored in a CSV file.
2. Automate total marks and percentage average calculations across subjects.
3. Apply configurable grade allocation rules and multi-subject pass/fail criteria.
4. Separate academic results from attendance evaluation, flagging attendance shortages (< 75%) independently.
5. Provide aggregate metrics including class averages, subject-wise comparisons, top performer rankings, and pass/fail statistics.
6. Verify accuracy and reliability through an automated `unittest` suite.

---

## 3. Technologies Used

| Technology | Purpose in Project |
| :--- | :--- |
| **Python 3** | Core programming language for application flow, loops, and conditional logic |
| **Pandas** | Tabular data loading, validation, indexing, column transformations, and filtering |
| **NumPy** | High-performance vector operations (`np.sum`, `np.mean`, `np.round`, `np.max`, `np.min`) |
| **CSV** | Lightweight, portable flat-file format for storing student records |
| **Python `unittest`** | Automated testing of validation functions, mathematical formulas, and business rules |
| **Git & GitHub** | Version control and source code repository management |

---

## 4. Dataset Description

The application processes data from `students.csv`, containing 28 realistic student records across 4 engineering departments.

### Schema:
- **`Student_ID`**: Unique student ID code (e.g., `S101` to `S128`).
- **`Name`**: Full student name.
- **`Department`**: Branch (Computer Science, Information Technology, AI & Data Science, Electronics).
- **`Mathematics`**: Marks out of 100 (Numeric, range 0–100).
- **`Python`**: Marks out of 100 (Numeric, range 0–100).
- **`Artificial_Intelligence`**: Marks out of 100 (Numeric, range 0–100).
- **`Database`**: Marks out of 100 (Numeric, range 0–100).
- **`Attendance`**: Attendance percentage (Float, range 0.0–100.0).

> **Dataset Note:** This is sample data created to represent realistic academic diversity:
> - High achievers (e.g., average >= 90%, Grade A+).
> - Moderate and passing students (Grades A through E).
> - Students failing due to scoring < 40 in one subject despite a decent overall average.
> - Students with attendance below 75% who passed academically, and those who failed academically, demonstrating separate attendance tracking.

---

## 5. Implementation

The project adheres to a clean separation of concerns:

### Architecture:
1. **`functions.py` (Business Logic & Analytics Module):**
   - **`load_student_data(filepath)`:** Reads CSV with Pandas; checks file existence, required columns, missing/NaN values, numeric types, and 0–100 range constraints.
   - **`assign_grade(average_marks)`:** Configurable if-elif-else logic mapping average to grades `A+`, `A`, `B`, `C`, `D`, `E`, or `F`.
   - **`determine_result(subject_marks, passing_mark=40.0)`:** Iterates through marks using a for-loop and evaluates if every subject meets or exceeds the minimum passing threshold of 40 marks.
   - **`check_attendance_status(attendance_percentage, threshold=75.0)`:** Evaluates if attendance is below 75% and assigns an alert status without altering academic grade/result.
   - **`process_student_performance(df)`:** Vectorized calculations using NumPy (`np.sum`, `np.mean`) to enrich DataFrame with `Total`, `Average`, `Grade`, `Result`, and `Attendance_Status`.
   - **Statistical Aggregators:** `get_class_statistics()`, `get_subject_statistics()`, `get_top_performers()`, and `get_low_attendance_students()`.
   - **CLI View Formatters:** Clean text table formatters for menu options.

2. **`main.py` (CLI Controller):**
   - Displays project banner.
   - Automatically detects dataset path.
   - Executes main interactive loop offering options 1 through 8.
   - Catches invalid inputs and handles keyboard interrupts gracefully.

3. **`test_analytics.py` (Automated Unit Tests):**
   - Implements 14 comprehensive unit test cases covering data loading, error handling, calculations, grading boundaries, pass/fail rules, and rankings.

---

## 6. Key Features

1. **Robust Input Validation:** Rejects missing columns, empty datasets, non-numeric values, and out-of-range marks (e.g. > 100 or < 0).
2. **Clear Pass Criterion:** Strict evaluation requiring at least 40 marks in every subject.
3. **Independent Attendance Alerts:** Flags low attendance (< 75%) separately without conflating attendance with exam marks.
4. **Subject Insights:** Automatically determines the best-performing and lowest-performing subjects.
5. **Top 3 Ranking:** Accurately sorts and displays the top 3 class achievers.
6. **Detailed Individual Reports:** Provides individual student lookup by ID or name substring.

---

## 7. Output and Screenshots

### Verified Terminal Run Results:
- **Total Students Evaluated:** 28
- **Overall Class Average:** 70.54%
- **Passed Students:** 23 (82.14%)
- **Failed Students:** 5 (17.86%)
- **Best-Performing Subject:** Artificial_Intelligence (72.68 avg)
- **Lowest-Performing Subject:** Mathematics (67.93 avg)
- **Top 3 Performers:**
  1. `#1 S104 Sneha Kulkarni` (Total: 383, Avg: 95.75%, Grade: A+)
  2. `#2 S126 Deepa Krishnan` (Total: 382, Avg: 95.50%, Grade: A+)
  3. `#3 S120 Neha Saxena` (Total: 373, Avg: 93.25%, Grade: A+)
- **Low Attendance (< 75%):** 7 students flagged.

### Screenshot of Output:
A verified screenshot of the terminal output generated from the live execution is saved at:
`screenshots/output.png`

```text
+--------------------------------------------------------------------------+
|          STUDENT PERFORMANCE ANALYTICS SYSTEM - TERMINAL OUTPUT          |
|  [+] Successfully loaded and validated 28 student records.               |
|  - Class Average: 70.54%                                                 |
|  - Top Student: Sneha Kulkarni (95.75%)                                  |
|  - Pass Rate: 82.14% (23 Passed, 5 Failed)                               |
|  - All 14 Unit Tests Passing (test_analytics.py)                         |
+--------------------------------------------------------------------------+
```

---

## 8. Final Outcome

The system successfully meets all functional, analytical, and architectural requirements:
- Fully automated evaluation of multi-subject datasets.
- Clean command-line user experience suitable for academic trainers and mentors.
- 100% test pass rate across 14 test cases in the test suite.
- Clean, documented, and modular code ready for internship project submission.

---

## 9. Challenges and Learning

### Key Learnings:
- **Pandas & NumPy Integration:** Learned how to use NumPy's vector arrays (`np.sum(axis=1)`, `np.mean(axis=1)`) alongside Pandas DataFrames for clean, fast data processing.
- **Validation & Edge Case Handling:** Understood the importance of validating inputs (checking missing values, verifying 0–100 bounds) before performing calculations.
- **Separation of Concerns:** Structuring business logic in `functions.py` and interface handling in `main.py` made code readable and easy to maintain.
- **Unit Testing:** Writing test cases with `unittest` helped ensure that grade thresholds and pass/fail rules behaved accurately.

### Challenges Faced & Solutions:
1. **Ensuring Subject-Level Pass Rule:** A student could have an 80% average but still score 35 in one subject. Implemented a dedicated function iterating over all subjects to guarantee that failing even one subject results in `FAIL`.
2. **Attendance Decoupling:** Balanced academic assessment with institutional compliance by creating a separate alert flag rather than failing students automatically.

---

## 10. GitHub Repository URL

- **Repository Link:** `https://github.com/HareshSubramaniam/studentanalysis`
- **Clone Command:**
  ```bash
  git clone https://github.com/HareshSubramaniam/studentanalysis.git
  ```

# Student Performance Analytics System

---

## 1. Project Title
**Student Performance Analytics System**  
An automated command-line analytics and evaluation system for academic performance monitoring.

---

## 2. Project Overview
The Student Performance Analytics System is a Python-based academic evaluation application designed to process, analyze, and summarize student examination performance and attendance records. Leveraging **Pandas** for tabular data manipulation and **NumPy** for numerical vector calculations, the system computes total marks, percentage averages, letter grades, pass/fail statuses, subject rankings, and attendance threshold alerts. It provides educators and mentors with transparent, automated insights through a modular command-line interface.

---

## 3. Problem Statement
Manual computation and assessment of multi-subject academic records is labor-intensive, error-prone, and inefficient when scaling across multiple students and departments. Furthermore, manual grading often fails to systematically enforce subject-level passing criteria or decouple compliance alerts (such as low attendance) from academic evaluations. An automated system is required to:
- Eliminate manual arithmetic errors in totals and percentage averages.
- Consistently apply multi-subject pass/fail criteria.
- Provide immediate class-wide benchmarks (class average, highest/lowest marks, top performers).
- Flag attendance shortages without prematurely imposing academic penalties before administrative review.

---

## 4. Project Objectives
- **Automated Record Processing:** Load and validate structured student datasets from standard CSV files.
- **Accurate Mathematical Operations:** Compute total scores, average percentages, and class metrics using high-performance NumPy calculations.
- **Rule-Based Grading:** Implement configurable letter grade assignments across defined percentage boundaries.
- **Strict Academic Pass Enforcement:** Enforce clear criteria requiring a minimum threshold score in every individual subject.
- **Independent Attendance Auditing:** Monitor attendance compliance against a 75% benchmark independently of academic results.
- **Actionable Reporting:** Deliver immediate tabular reports, individual student cards, subject performance breakdowns, and top-performer rankings.
- **Code Quality & Reliability:** Maintain modular, PEP 8-compliant Python architecture verified by automated unit tests.

---

## 5. Technologies Used
- **Python 3:** Core programming language implementing business logic, iteration, and conditional evaluation.
- **Pandas:** Tabular data loading (`pd.read_csv`), column validation, record filtering, and DataFrame handling.
- **NumPy:** Vectorized numerical operations (`np.sum`, `np.mean`, `np.round`, `np.max`, `np.min`).
- **CSV:** Lightweight, flat-file format for persistent student record storage.
- **Python `unittest`:** Standard library test automation framework.
- **Git & GitHub:** Version control and repository distribution.

---

## 6. System Requirements
- **Operating System:** Platform independent (Linux, macOS, Windows).
- **Python Version:** Python 3.10 or higher.
- **Core Dependencies:**
  - `pandas>=2.0.0`
  - `numpy>=1.24.0`
- **Hardware Requirements:** Minimal (runs smoothly on any standard modern hardware with >= 512 MB available RAM).

---

## 7. Project Folder Structure
```text
studentanalysis/
│
├── main.py                   # Application entry point and interactive CLI menu loop
├── functions.py              # Modular business logic, calculations, and validation
├── test_analytics.py         # Automated unit test suite (18 test cases)
├── students.csv              # Student records dataset (28 sample records)
├── requirements.txt          # Python library dependencies (pandas, numpy)
├── README.md                 # Project summary and user guide
├── Project_Documentation.md  # Comprehensive technical system documentation
│
└── screenshots/
    └── output.png            # Live execution terminal output screenshot
```

---

## 8. Dataset Description
The dataset is maintained in `students.csv` and contains 28 realistic student records spanning four engineering departments: Computer Science, Information Technology, AI & Data Science, and Electronics.

### Dataset Schema
| Column Name | Data Type | Permissible Range | Description |
| :--- | :--- | :---: | :--- |
| `Student_ID` | String | Unique Identifier | Primary key representing the student (e.g., S101 to S128). |
| `Name` | String | Non-empty text | Full student name. |
| `Department` | String | Non-empty text | Academic department / specialization. |
| `Mathematics` | Numeric | 0 to 100 | Marks obtained in Mathematics examination. |
| `Python` | Numeric | 0 to 100 | Marks obtained in Python Programming examination. |
| `Artificial_Intelligence`| Numeric | 0 to 100 | Marks obtained in Artificial Intelligence examination. |
| `Database` | Numeric | 0 to 100 | Marks obtained in Database Management examination. |
| `Attendance` | Numeric | 0.0 to 100.0 | Overall semester attendance percentage. |

The dataset incorporates diverse academic performance tiers, including high achievers, moderate students, students failing due to a single subject deficiency despite high averages, and varied attendance profiles.

---

## 9. System Architecture and Workflow
The system employs a modular, two-tier architecture separating interface presentation from computational logic:

```text
+-----------------------------------------------------------+
|                        CSV Dataset                        |
|                       (students.csv)                      |
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                     Data Layer                            |
|             functions.py: load_student_data()             |
|   - Verifies existence & non-zero file size               |
|   - Validates column presence & non-null constraints      |
|   - Rejects blank fields, duplicates, and out-of-bounds   |
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                   Processing Layer                        |
|       functions.py: process_student_performance()         |
|   - NumPy 2D array conversion                             |
|   - Vectorized Total (np.sum) & Average (np.mean)         |
|   - Grade assignment via if-elif-else                     |
|   - Pass/Fail evaluation across all subjects              |
|   - Attendance threshold tagging                          |
+-----------------------------+-----------------------------+
                              |
                              v
+-----------------------------------------------------------+
|                   Presentation Layer                      |
|                   main.py: main() Loop                    |
|   - CLI Welcome Banner & Interactive Navigation Menu      |
|   - Query routing (Options 1 to 8)                        |
|   - Formatted table display & individual report cards     |
+-----------------------------------------------------------+
```

---

## 10. Implementation Details
The application is structured into three primary Python modules:
1. **`functions.py`:** Contains reusable functions for dataset ingestion, validation, vector arithmetic, aggregation, and tabular console formatting.
2. **`main.py`:** Provides the user entry point, detects dataset file paths across directories, handles interactive menu input, and catches keyboard interrupts gracefully.
3. **`test_analytics.py`:** Implements automated unit tests utilizing Python's `unittest` framework to verify data integrity, calculation correctness, boundary grading, and edge cases.

---

## 11. Total Marks and Average Calculation
Total and average marks are computed across the four academic subjects (`Mathematics`, `Python`, `Artificial_Intelligence`, `Database`):
- **Vector Transformation:** Marks are extracted into a 2-dimensional NumPy array:
  $$\text{marks\_array} = \text{DataFrame}[\text{SUBJECT\_COLUMNS}].\text{to\_numpy}()$$
- **Total Marks:**
  $$\text{Total} = \sum_{i=1}^{4} \text{Mark}_i \quad \Longrightarrow \quad \text{np.sum}(\text{marks\_array}, \text{axis}=1)$$
- **Average Percentage:**
  $$\text{Average} = \frac{\text{Total}}{4} \quad \Longrightarrow \quad \text{np.round}(\text{np.mean}(\text{marks\_array}, \text{axis}=1), 2)$$

---

## 12. Grade Assignment Logic
Grades are assigned based on the calculated average marks using a deterministic classification scheme:

| Average Marks Range | Letter Grade | Academic Standing |
| :---: | :---: | :--- |
| **Average >= 90.0%** | **A+** | Outstanding |
| **Average >= 80.0%** | **A** | Excellent |
| **Average >= 70.0%** | **B** | Very Good |
| **Average >= 60.0%** | **C** | Good |
| **Average >= 50.0%** | **D** | Satisfactory |
| **Average >= 40.0%** | **E** | Pass (Minimum) |
| **Average < 40.0%** | **F** | Fail |

The evaluation is implemented using standard `if-elif-else` branches evaluated sequentially.

---

## 13. Pass/Fail Determination
The system enforces a strict subject-level passing rule:
- **Rule:** A student receives a **PASS** result if and only if their mark in **every individual subject** is greater than or equal to **40.0**.
- **Condition:**
  $$\text{Result} = \begin{cases} \text{PASS}, & \text{if } \forall s \in \text{Subjects}, \text{Mark}_s \ge 40.0 \\ \text{FAIL}, & \text{otherwise} \end{cases}$$
- Even if a student achieves an overall average of 80% or higher, scoring below 40 marks in even a single subject produces an overall result of **FAIL**.

---

## 14. Class Performance Statistics
Class-level statistics aggregate the entire cohort to measure overall academic outcomes:
- **Total Students:** $N = \text{len}(\text{df}) = 28$
- **Overall Class Average:** $70.54\%$ (mean of student averages)
- **Highest Student Average:** $95.75\%$ (Achieved by student S104)
- **Lowest Student Average:** $33.75\%$ (Student S121)
- **Passed Students Count:** $23$ students ($82.14\%$)
- **Failed Students Count:** $5$ students ($17.86\%$)

---

## 15. Subject-wise Performance Analysis
Subject averages are calculated by applying `np.mean()` across individual subject columns:

| Subject Name | Class Average (Out of 100) | Relative Performance |
| :--- | :---: | :--- |
| **Mathematics** | 67.93 | Lowest-Performing Subject |
| **Python** | 70.25 | Moderate Performance |
| **Artificial Intelligence** | 72.68 | Best-Performing Subject |
| **Database** | 71.29 | Strong Performance |

The system dynamically determines the best and lowest performing subjects using `max()` and `min()` lookups across the computed averages dictionary.

---

## 16. Top Performer Identification
Top achievers are identified by sorting the cohort in descending order of average percentage:
- **Sorting Criteria:** Primary sort on `Average` (descending), secondary sort on `Total` (descending), and tertiary sort on `Student_ID` (ascending) to ensure deterministic rankings in case of ties.
- **Top 3 Cohort Achievers:**
  1. **Rank 1:** Student ID `S104` (Total: 383 / 400, Average: 95.75%, Grade: A+)
  2. **Rank 2:** Student ID `S126` (Total: 382 / 400, Average: 95.50%, Grade: A+)
  3. **Rank 3:** Student ID `S120` (Total: 373 / 400, Average: 93.25%, Grade: A+)

---

## 17. Attendance Monitoring
Attendance compliance is evaluated against a fixed institutional benchmark of **75.0%**:
- **Evaluation Rule:** If $\text{Attendance} < 75.0\%$, the record is tagged with an alert status (`[LOW (<75%)]`).
- **Separation from Academic Result:** In accordance with institutional guidelines, attendance shortage does not automatically alter a student's academic pass/fail status.
- **Cohort Attendance Metrics:**
  - Overall Class Attendance Average: $81.93\%$
  - Adequate Attendance ($\ge 75\%$): $21$ students ($75.00\%$)
  - Low Attendance ($< 75\%$): $7$ students ($25.00\%$)

---

## 18. Input Validation and Error Handling
The system implements comprehensive defensive programming checks to guarantee data integrity:
- **File System Validation:** Validates file existence via `os.path.exists()` and verifies non-zero byte size before reading.
- **Column Integrity:** Checks that all 8 required column headers exist; otherwise raises a clear `ValueError`.
- **Null Value Rejection:** Scans for `NaN` / null entries and reports the exact problematic columns.
- **Empty Field Rejection:** Validates that text columns (`Student_ID`, `Name`, `Department`) do not contain blank or whitespace-only strings.
- **Uniqueness Check:** Enforces that `Student_ID` values are strictly unique across the dataset.
- **Type and Range Boundaries:** Verifies that all subject marks and attendance are numeric and strictly fall within $[0.0, 100.0]$.
- **Graceful CLI Handling:** Catches `KeyboardInterrupt` and `EOFError` to allow clean termination without printing tracebacks.
- **Empty DataFrame Protection:** Analytics and presentation routines accept empty DataFrames safely, returning empty structures or informative notices.

---

## 19. How to Install and Run the Project

### Prerequisites
- Python 3.10 or higher.
- `pip` package manager.

### Installation Steps
1. Navigate to the project directory:
   ```bash
   cd studentanalysis
   ```
2. Create and activate a Python virtual environment:
   - **Linux / macOS:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
Launch the interactive command-line interface:
```bash
python3 main.py
```

---

## 20. How to Run Unit Tests
The test suite is built on Python's standard `unittest` framework and requires no third-party test runner.

Execute all automated unit tests:
```bash
python3 -m unittest -v test_analytics.py
```

---

## 21. Testing Results
The automated test suite in `test_analytics.py` executes 18 targeted test cases validating data loading, boundaries, mathematical accuracy, ranking consistency, and error handling:

```text
test_01_dataset_loading_and_count ... ok
test_02_missing_file_raises_error ... ok
test_03_missing_columns_validation ... ok
test_04_out_of_bounds_marks_validation ... ok
test_05_grade_assignment_rules ... ok
test_06_pass_fail_rule ... ok
test_07_attendance_threshold_alert ... ok
test_08_total_and_average_calculations ... ok
test_09_top_performers_ranking ... ok
test_10_subject_statistics ... ok
test_11_class_statistics ... ok
test_12_low_attendance_filtering ... ok
test_13_non_numeric_marks_validation ... ok
test_14_empty_dataset_validation ... ok
test_15_duplicate_student_id_validation ... ok
test_16_blank_text_field_validation ... ok
test_17_empty_dataframe_analytics ... ok
test_18_ranking_ties_deterministic ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.023s

OK
```
**Test Pass Rate:** 100% (18/18 passed, 0 failures, 0 errors).

---

## 22. Sample Output

### Overall Class Performance Summary (Option 7)
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

### Top 3 Performers (Option 4)
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

### Verified Terminal Screenshot
A complete execution capture is stored in:
`screenshots/output.png`

---

## 23. Limitations
- **Console Interface Only:** The system operates strictly via command-line menus without a graphical web or desktop UI.
- **Static Schema:** Subject columns are configured for four core subjects; dynamic column additions require constant configuration updates.
- **In-Memory Analysis:** Data processing loads the entire CSV into memory via Pandas DataFrames, which is optimal for small-to-medium datasets (thousands of rows) but not designed for distributed big data.

---

## 24. Future Enhancements
- **Export Capabilities:** Generating styled PDF report cards and Excel summaries with embedded charts.
- **Data Visualizations:** Integrating Matplotlib / Seaborn to plot grade distribution histograms and attendance scatter plots.
- **Dynamic Subject Configuration:** Allowing users to specify arbitrary subject names and counts at runtime via configuration files.
- **Relational Database Backend:** Storing historical semester records using SQLite or PostgreSQL for multi-term tracking.

---

## 25. Conclusion
The Student Performance Analytics System successfully demonstrates the application of Python fundamentals, Pandas, and NumPy in automating academic record evaluation. By implementing strict data validation, rule-based grading, subject-level pass enforcement, and decoupled attendance tracking, the application provides an accurate, dependable, and maintainable solution for academic performance analytics.

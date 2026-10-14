import os
import pandas as pd
import numpy as np

REQUIRED_COLUMNS = [
    'Student_ID',
    'Name',
    'Department',
    'Mathematics',
    'Python',
    'Artificial_Intelligence',
    'Database',
    'Attendance'
]

SUBJECT_COLUMNS = [
    'Mathematics',
    'Python',
    'Artificial_Intelligence',
    'Database'
]

PASSING_MARK_PER_SUBJECT = 40.0
ATTENDANCE_THRESHOLD = 75.0


def load_student_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Error: The dataset file '{filepath}' was not found.")

    if os.path.getsize(filepath) == 0:
        raise ValueError("Error: The CSV dataset is empty.")

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Error reading CSV file: {e}")

    if df.empty:
        raise ValueError("Error: The CSV dataset is empty.")

    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Error: Dataset is missing required columns: {missing_cols}")

    if df[REQUIRED_COLUMNS].isnull().any().any():
        null_counts = df[REQUIRED_COLUMNS].isnull().sum()
        problematic_cols = null_counts[null_counts > 0].to_dict()
        raise ValueError(f"Error: Dataset contains missing (NaN) values in columns: {problematic_cols}")

    numeric_columns = SUBJECT_COLUMNS + ['Attendance']
    for col in numeric_columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                raise ValueError(f"Error: Column '{col}' contains non-numeric values.")

        out_of_bounds = df[(df[col] < 0) | (df[col] > 100)]
        if not out_of_bounds.empty:
            raise ValueError(
                f"Error: Column '{col}' contains values outside the valid range [0, 100] "
                f"for Student ID(s): {out_of_bounds['Student_ID'].tolist()}."
            )

    return df


def assign_grade(average_marks):
    if average_marks >= 90.0:
        return 'A+'
    elif average_marks >= 80.0:
        return 'A'
    elif average_marks >= 70.0:
        return 'B'
    elif average_marks >= 60.0:
        return 'C'
    elif average_marks >= 50.0:
        return 'D'
    elif average_marks >= 40.0:
        return 'E'
    else:
        return 'F'


def determine_result(subject_marks, passing_mark=PASSING_MARK_PER_SUBJECT):
    for mark in subject_marks:
        if mark < passing_mark:
            return 'FAIL'
    return 'PASS'


def check_attendance_status(attendance_percentage, threshold=ATTENDANCE_THRESHOLD):
    if attendance_percentage < threshold:
        return 'LOW (<75%)'
    return 'ADEQUATE'


def process_student_performance(df):
    processed_df = df.copy()
    marks_array = processed_df[SUBJECT_COLUMNS].to_numpy()

    processed_df['Total'] = np.sum(marks_array, axis=1)
    processed_df['Average'] = np.round(np.mean(marks_array, axis=1), 2)

    grades = []
    for avg in processed_df['Average']:
        grades.append(assign_grade(avg))
    processed_df['Grade'] = grades

    results = []
    for _, row in processed_df.iterrows():
        student_marks = [row[sub] for sub in SUBJECT_COLUMNS]
        results.append(determine_result(student_marks))
    processed_df['Result'] = results

    attendance_flags = []
    for att in processed_df['Attendance']:
        attendance_flags.append(check_attendance_status(att))
    processed_df['Attendance_Status'] = attendance_flags

    return processed_df


def get_class_statistics(df):
    total_students = len(df)
    if total_students == 0:
        return {}

    averages = df['Average'].to_numpy()
    highest_avg = float(np.max(averages))
    lowest_avg = float(np.min(averages))
    class_avg = float(np.round(np.mean(averages), 2))

    passed_count = int(np.sum(df['Result'].to_numpy() == 'PASS'))
    failed_count = int(total_students - passed_count)
    pass_percentage = float(np.round((passed_count / total_students) * 100, 2))
    low_att_count = int(np.sum(df['Attendance'].to_numpy() < ATTENDANCE_THRESHOLD))

    return {
        'total_students': total_students,
        'highest_average': highest_avg,
        'lowest_average': lowest_avg,
        'class_average': class_avg,
        'passed_count': passed_count,
        'failed_count': failed_count,
        'pass_percentage': pass_percentage,
        'low_attendance_count': low_att_count
    }


def get_subject_statistics(df):
    subject_averages = {}
    for subject in SUBJECT_COLUMNS:
        subject_marks = df[subject].to_numpy()
        subject_averages[subject] = float(np.round(np.mean(subject_marks), 2))

    best_subject = max(subject_averages, key=subject_averages.get)
    lowest_subject = min(subject_averages, key=subject_averages.get)

    return {
        'subject_averages': subject_averages,
        'best_subject': best_subject,
        'best_subject_average': subject_averages[best_subject],
        'lowest_subject': lowest_subject,
        'lowest_subject_average': subject_averages[lowest_subject]
    }


def get_top_performers(df, n=3):
    sorted_df = df.sort_values(by=['Average', 'Total'], ascending=[False, False])
    return sorted_df.head(n)


def get_low_attendance_students(df, threshold=ATTENDANCE_THRESHOLD):
    return df[df['Attendance'] < threshold]


def display_header(title):
    border = "=" * 70
    print("\n" + border)
    print(f"  {title.upper()}")
    print(border)


def display_all_students(df):
    display_header("All Student Records")
    print(f"Total Records: {len(df)}\n")

    header = (
        f"{'ID':<6} {'Name':<20} {'Dept':<12} "
        f"{'Math':<5} {'Py':<5} {'AI':<5} {'DB':<5} "
        f"{'Total':<6} {'Avg':<6} {'Grd':<4} {'Result':<6} {'Att%':<6} {'Status'}"
    )
    print(header)
    print("-" * len(header))

    for _, row in df.iterrows():
        status_flag = "[LOW]" if row['Attendance'] < ATTENDANCE_THRESHOLD else "OK"
        print(
            f"{row['Student_ID']:<6} "
            f"{row['Name'][:19]:<20} "
            f"{row['Department'][:11]:<12} "
            f"{int(row['Mathematics']):<5} "
            f"{int(row['Python']):<5} "
            f"{int(row['Artificial_Intelligence']):<5} "
            f"{int(row['Database']):<5} "
            f"{int(row['Total']):<6} "
            f"{row['Average']:<6.2f} "
            f"{row['Grade']:<4} "
            f"{row['Result']:<6} "
            f"{row['Attendance']:<6.1f} "
            f"{status_flag}"
        )
    print("-" * len(header))


def display_individual_student_report(df, query):
    query_clean = str(query).strip()
    match = df[
        (df['Student_ID'].str.upper() == query_clean.upper()) |
        (df['Name'].str.lower() == query_clean.lower())
    ]

    if match.empty:
        match = df[df['Name'].str.lower().str.contains(query_clean.lower(), na=False)]

    if match.empty:
        print(f"\n[!] No student record found matching query: '{query_clean}'")
        return

    for _, student in match.iterrows():
        display_header(f"Student Report Card - {student['Student_ID']}")
        print(f"Student ID     : {student['Student_ID']}")
        print(f"Full Name      : {student['Name']}")
        print(f"Department     : {student['Department']}")
        print("-" * 50)
        print("SUBJECT-WISE MARKS (Passing Mark = 40):")
        for sub in SUBJECT_COLUMNS:
            mark = student[sub]
            sub_status = "PASS" if mark >= PASSING_MARK_PER_SUBJECT else "FAIL (<40)"
            print(f"  * {sub:<25}: {mark:>3} / 100  [{sub_status}]")
        print("-" * 50)
        print(f"Total Marks    : {student['Total']} / 400")
        print(f"Average Marks  : {student['Average']:.2f}%")
        print(f"Assigned Grade : {student['Grade']}")
        print(f"Final Result   : {student['Result']} {'(All subjects >= 40)' if student['Result'] == 'PASS' else '(Scored < 40 in one or more subjects)'}")
        print("-" * 50)
        att = student['Attendance']
        att_note = "ELIGIBLE (>= 75%)" if att >= ATTENDANCE_THRESHOLD else "[!] WARNING: Attendance Below 75% Requirement"
        print(f"Attendance     : {att:.1f}% -> {att_note}")
        print("=" * 50)


def display_subject_analysis(df):
    display_header("Subject-Wise Performance Analysis")
    stats = get_subject_statistics(df)

    print(f"{'Subject':<30} {'Average Marks':<15}")
    print("-" * 45)
    for sub, avg in stats['subject_averages'].items():
        print(f"{sub:<30} {avg:>6.2f} / 100")
    print("-" * 45)
    print(f"\n[+] Best-Performing Subject   : {stats['best_subject']} ({stats['best_subject_average']:.2f} avg)")
    print(f"[-] Lowest-Performing Subject : {stats['lowest_subject']} ({stats['lowest_subject_average']:.2f} avg)")


def display_top_performers(df, n=3):
    display_header(f"Top {n} Performers of the Class")
    top_df = get_top_performers(df, n=n)

    print(f"{'Rank':<6} {'ID':<6} {'Name':<22} {'Department':<18} {'Total':<7} {'Average':<8} {'Grade'}")
    print("-" * 75)

    rank = 1
    for _, row in top_df.iterrows():
        print(
            f"#{rank:<5} "
            f"{row['Student_ID']:<6} "
            f"{row['Name']:<22} "
            f"{row['Department']:<18} "
            f"{int(row['Total']):<7} "
            f"{row['Average']:<8.2f} "
            f"{row['Grade']}"
        )
        rank += 1
    print("-" * 75)


def display_pass_fail_statistics(df):
    display_header("Pass / Fail Statistics")
    stats = get_class_statistics(df)

    total = stats['total_students']
    passed = stats['passed_count']
    failed = stats['failed_count']
    pass_pct = stats['pass_percentage']
    fail_pct = round(100.0 - pass_pct, 2)

    print(f"Pass Criterion         : Minimum {int(PASSING_MARK_PER_SUBJECT)} marks in EACH subject")
    print("-" * 55)
    print(f"Total Students Assessed: {total}")
    print(f"Students Passed        : {passed:<5} ({pass_pct:.2f}%)")
    print(f"Students Failed        : {failed:<5} ({fail_pct:.2f}%)")
    print("-" * 55)


def display_attendance_analysis(df):
    display_header(f"Attendance Analysis (Threshold: {int(ATTENDANCE_THRESHOLD)}%)")

    avg_att = float(np.round(np.mean(df['Attendance'].to_numpy()), 2))
    low_att_df = get_low_attendance_students(df, ATTENDANCE_THRESHOLD)
    low_count = len(low_att_df)
    total = len(df)
    low_pct = round((low_count / total) * 100, 2)

    print(f"Overall Class Attendance Average : {avg_att:.2f}%")
    print(f"Students with Adequate (>= 75%)  : {total - low_count} ({round(100 - low_pct, 2)}%)")
    print(f"Students with Low (< 75%)        : {low_count} ({low_pct:.2f}%)")
    print("\n[NOTE] Attendance below 75% is flagged separately.")
    print("       It does not automatically fail students academically unless specified.")

    if not low_att_df.empty:
        print(f"\n--- Students with Attendance Below {int(ATTENDANCE_THRESHOLD)}% ---")
        print(f"{'ID':<6} {'Name':<22} {'Department':<18} {'Att%':<8} {'Academic Result'}")
        print("-" * 65)
        for _, row in low_att_df.iterrows():
            print(
                f"{row['Student_ID']:<6} "
                f"{row['Name']:<22} "
                f"{row['Department']:<18} "
                f"{row['Attendance']:<8.1f} "
                f"{row['Result']}"
            )
        print("-" * 65)
    else:
        print("\nAll students have attendance at or above 75%. Great job!")


def display_class_summary(df):
    display_header("Overall Class Performance Summary")
    class_stats = get_class_statistics(df)
    sub_stats = get_subject_statistics(df)

    highest_row = df.loc[df['Average'].idxmax()]
    lowest_row = df.loc[df['Average'].idxmin()]

    print(f"Total Number of Students    : {class_stats['total_students']}")
    print(f"Overall Class Average       : {class_stats['class_average']:.2f}%")
    print(f"Highest Student Average     : {class_stats['highest_average']:.2f}% ({highest_row['Name']} - {highest_row['Student_ID']})")
    print(f"Lowest Student Average      : {class_stats['lowest_average']:.2f}% ({lowest_row['Name']} - {lowest_row['Student_ID']})")
    print("-" * 65)
    print(f"Total Passed Students       : {class_stats['passed_count']} / {class_stats['total_students']} ({class_stats['pass_percentage']:.2f}%)")
    print(f"Total Failed Students       : {class_stats['failed_count']} / {class_stats['total_students']} ({100 - class_stats['pass_percentage']:.2f}%)")
    print("-" * 65)
    print(f"Best-Performing Subject     : {sub_stats['best_subject']} ({sub_stats['best_subject_average']:.2f} avg)")
    print(f"Lowest-Performing Subject   : {sub_stats['lowest_subject']} ({sub_stats['lowest_subject_average']:.2f} avg)")
    print("-" * 65)
    print(f"Attendance Shortage (<75%)  : {class_stats['low_attendance_count']} student(s)")
    print("=" * 65)

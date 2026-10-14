import unittest
import os
import tempfile
import pandas as pd
import numpy as np

from functions import (
    REQUIRED_COLUMNS,
    SUBJECT_COLUMNS,
    load_student_data,
    assign_grade,
    determine_result,
    check_attendance_status,
    process_student_performance,
    get_class_statistics,
    get_subject_statistics,
    get_top_performers,
    get_low_attendance_students
)


class TestStudentAnalytics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cls.csv_path = os.path.join(script_dir, "students.csv")
        cls.raw_df = load_student_data(cls.csv_path)
        cls.processed_df = process_student_performance(cls.raw_df)

    def test_01_dataset_loading_and_count(self):
        self.assertIsNotNone(self.raw_df)
        self.assertGreaterEqual(len(self.raw_df), 25)
        for col in REQUIRED_COLUMNS:
            self.assertIn(col, self.raw_df.columns)

    def test_02_missing_file_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            load_student_data("non_existent_dataset_12345.csv")

    def test_03_missing_columns_validation(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tf:
            tf.write("Student_ID,Name,Department,Mathematics,Python\nS999,Test,CS,50,50\n")
            temp_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                load_student_data(temp_path)
            self.assertIn("missing required columns", str(ctx.exception).lower())
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_04_out_of_bounds_marks_validation(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tf:
            tf.write(
                "Student_ID,Name,Department,Mathematics,Python,Artificial_Intelligence,Database,Attendance\n"
                "S999,Invalid Student,CS,105,80,75,70,90\n"
            )
            temp_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                load_student_data(temp_path)
            self.assertIn("outside the valid range", str(ctx.exception).lower())
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_05_grade_assignment_rules(self):
        self.assertEqual(assign_grade(100.0), 'A+')
        self.assertEqual(assign_grade(90.0), 'A+')
        self.assertEqual(assign_grade(89.9), 'A')
        self.assertEqual(assign_grade(80.0), 'A')
        self.assertEqual(assign_grade(79.9), 'B')
        self.assertEqual(assign_grade(70.0), 'B')
        self.assertEqual(assign_grade(69.9), 'C')
        self.assertEqual(assign_grade(60.0), 'C')
        self.assertEqual(assign_grade(59.9), 'D')
        self.assertEqual(assign_grade(50.0), 'D')
        self.assertEqual(assign_grade(49.9), 'E')
        self.assertEqual(assign_grade(40.0), 'E')
        self.assertEqual(assign_grade(39.9), 'F')
        self.assertEqual(assign_grade(0.0), 'F')

    def test_06_pass_fail_rule(self):
        self.assertEqual(determine_result([40, 40, 40, 40]), 'PASS')
        self.assertEqual(determine_result([80, 75, 90, 85]), 'PASS')
        self.assertEqual(determine_result([39, 95, 95, 95]), 'FAIL')
        self.assertEqual(determine_result([50, 39.5, 60, 70]), 'FAIL')
        self.assertEqual(determine_result([30, 20, 25, 35]), 'FAIL')

    def test_07_attendance_threshold_alert(self):
        self.assertEqual(check_attendance_status(75.0), 'ADEQUATE')
        self.assertEqual(check_attendance_status(95.5), 'ADEQUATE')
        self.assertEqual(check_attendance_status(74.9), 'LOW (<75%)')
        self.assertEqual(check_attendance_status(50.0), 'LOW (<75%)')

    def test_08_total_and_average_calculations(self):
        df = self.processed_df
        for _, row in df.iterrows():
            expected_total = sum([row[s] for s in SUBJECT_COLUMNS])
            expected_avg = round(expected_total / len(SUBJECT_COLUMNS), 2)
            self.assertEqual(row['Total'], expected_total)
            self.assertAlmostEqual(row['Average'], expected_avg, places=2)

    def test_09_top_performers_ranking(self):
        top_3 = get_top_performers(self.processed_df, n=3)
        self.assertEqual(len(top_3), 3)
        averages = top_3['Average'].tolist()
        self.assertEqual(averages, sorted(averages, reverse=True))

    def test_10_subject_statistics(self):
        stats = get_subject_statistics(self.processed_df)
        for sub in SUBJECT_COLUMNS:
            expected_mean = round(float(np.mean(self.processed_df[sub].to_numpy())), 2)
            self.assertAlmostEqual(stats['subject_averages'][sub], expected_mean, places=2)

        self.assertIn(stats['best_subject'], SUBJECT_COLUMNS)
        self.assertIn(stats['lowest_subject'], SUBJECT_COLUMNS)
        self.assertGreaterEqual(stats['best_subject_average'], stats['lowest_subject_average'])

    def test_11_class_statistics(self):
        stats = get_class_statistics(self.processed_df)
        total = len(self.processed_df)
        self.assertEqual(stats['total_students'], total)
        self.assertEqual(stats['passed_count'] + stats['failed_count'], total)

        expected_pass_pct = round((stats['passed_count'] / total) * 100, 2)
        self.assertAlmostEqual(stats['pass_percentage'], expected_pass_pct, places=2)

    def test_12_low_attendance_filtering(self):
        low_att_df = get_low_attendance_students(self.processed_df, threshold=75.0)
        self.assertEqual(len(low_att_df), 7)
        for att in low_att_df['Attendance']:
            self.assertLess(att, 75.0)

    def test_13_non_numeric_marks_validation(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tf:
            tf.write(
                "Student_ID,Name,Department,Mathematics,Python,Artificial_Intelligence,Database,Attendance\n"
                "S999,Invalid Student,CS,eighty,80,75,70,90\n"
            )
            temp_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                load_student_data(temp_path)
            self.assertIn("non-numeric", str(ctx.exception).lower())
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def test_14_empty_dataset_validation(self):
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tf:
            tf.write("")
            temp_path = tf.name

        try:
            with self.assertRaises(ValueError) as ctx:
                load_student_data(temp_path)
            self.assertIn("empty", str(ctx.exception).lower())
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


if __name__ == "__main__":
    unittest.main()

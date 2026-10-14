import sys
import os

from functions import (
    load_student_data,
    process_student_performance,
    display_all_students,
    display_individual_student_report,
    display_subject_analysis,
    display_top_performers,
    display_pass_fail_statistics,
    display_attendance_analysis,
    display_class_summary
)


def get_dataset_path():
    """Locate students.csv across common working directory paths."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "students.csv"),
        os.path.join(os.getcwd(), "students.csv"),
        os.path.join(os.getcwd(), "studentanalysis", "students.csv"),
        os.path.join(os.getcwd(), "student-performance-analytics", "students.csv")
    ]
    for path in candidates:
        if os.path.isfile(path):
            return path
    return os.path.join(script_dir, "students.csv")


def print_welcome_banner():
    """Display system title and project banner."""
    print("\n" + "=" * 60)
    print("        STUDENT PERFORMANCE ANALYTICS SYSTEM        ")
    print("      EWB EDUTECH - Python with AI Mini Project      ")
    print("=" * 60)


def print_menu():
    """Display CLI navigation menu."""
    print("\n------------------- MAIN MENU -------------------")
    print("1. View all students")
    print("2. View individual student report")
    print("3. View subject-wise analysis")
    print("4. View top 3 performers")
    print("5. View pass/fail statistics")
    print("6. View attendance analysis")
    print("7. View overall class summary")
    print("8. Exit")
    print("-------------------------------------------------")


def main():
    """Run interactive menu-driven console loop."""
    print_welcome_banner()

    dataset_path = get_dataset_path()
    print(f"[*] Loading student records from: {os.path.basename(dataset_path)}...")

    try:
        raw_df = load_student_data(dataset_path)
        processed_df = process_student_performance(raw_df)
        print(f"[+] Successfully loaded and validated {len(processed_df)} student records.")
    except Exception as e:
        print(f"\n[X] Initialization Failed: {e}")
        sys.exit(1)

    while True:
        print_menu()
        try:
            choice = input("Enter your choice (1-8): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nOperation interrupted by user. Exiting gracefully. Goodbye!")
            break

        if choice == '1':
            display_all_students(processed_df)

        elif choice == '2':
            try:
                query = input("\nEnter Student ID (e.g. S101) or Student Name: ").strip()
                if query:
                    display_individual_student_report(processed_df, query)
                else:
                    print("[!] Input cannot be empty. Please enter a valid ID or Name.")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled.")

        elif choice == '3':
            display_subject_analysis(processed_df)

        elif choice == '4':
            display_top_performers(processed_df, n=3)

        elif choice == '5':
            display_pass_fail_statistics(processed_df)

        elif choice == '6':
            display_attendance_analysis(processed_df)

        elif choice == '7':
            display_class_summary(processed_df)

        elif choice == '8':
            print("\nThank you for using the Student Performance Analytics System!")
            print("Session closed successfully. Goodbye!\n")
            break

        else:
            print("\n[!] Invalid option! Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()

import pandas as pd
import numpy as np

from functions import (
    calculate_total,
    calculate_average,
    assign_grade,
    check_pass_fail,
    get_performance_level,
    find_strongest_subject,
    find_weakest_subject
)

from charts import (
    subject_performance_chart,
    student_performance_chart,
    grade_distribution_chart,
    attendance_vs_performance
)

def show_header():
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + "STUDENT PERFORMANCE ANALYTICS".center(58) + "║")
    print("║" + "INSIGHTX".center(58) + "║")
    print("╚" + "═" * 58 + "╝")


def show_section(title):
    print("\n")
    print("┌" + "─" * 58 + "┐")
    print("│" + title.center(58) + "│")
    print("└" + "─" * 58 + "┘")
# -------------------------------
# PROJECT SETTINGS
# -------------------------------

SUBJECTS = ["Python", "SQL", "Mathematics", "AI"]


# -------------------------------
# LOAD DATA
# -------------------------------

data = pd.read_csv("students.csv")


# -------------------------------
# CALCULATE STUDENT PERFORMANCE
# -------------------------------

totals = []
averages = []
grades = []
results = []
performance_levels = []
strongest_subjects = []
weakest_subjects = []


for index, student in data.iterrows():

    marks = np.array([
        student["Python"],
        student["SQL"],
        student["Mathematics"],
        student["AI"]
    ])

    total = calculate_total(marks)
    average = calculate_average(marks)

    grade = assign_grade(average)

    result = check_pass_fail(
        marks,
        student["Attendance"]
    )

    performance = get_performance_level(average)

    strongest = find_strongest_subject(
        marks,
        SUBJECTS
    )

    weakest = find_weakest_subject(
        marks,
        SUBJECTS
    )

    totals.append(total)
    averages.append(average)
    grades.append(grade)
    results.append(result)
    performance_levels.append(performance)
    strongest_subjects.append(strongest)
    weakest_subjects.append(weakest)


# -------------------------------
# ADD RESULTS TO DATAFRAME
# -------------------------------

data["Total"] = totals
data["Average"] = np.round(averages, 2)
data["Grade"] = grades
data["Result"] = results
data["Performance"] = performance_levels
data["Strongest Subject"] = strongest_subjects
data["Needs Focus"] = weakest_subjects


# -------------------------------
# SORT STUDENTS BY PERFORMANCE
# -------------------------------

data = data.sort_values(
    by="Average",
    ascending=False
).reset_index(drop=True)

data["Rank"] = np.arange(1, len(data) + 1)


# -------------------------------
# CLASS ANALYSIS
# -------------------------------

class_average = np.mean(data["Average"])

highest_average = data["Average"].max()

lowest_average = data["Average"].min()

pass_count = (data["Result"] == "Pass").sum()

fail_count = (data["Result"] == "Fail").sum()


# Subject averages

subject_averages = data[SUBJECTS].mean()

best_subject = subject_averages.idxmax()

best_subject_average = subject_averages.max()


# -------------------------------
# DISPLAY DASHBOARD
# -------------------------------

print("\n")
print("=" * 60)
print("           STUDENT PERFORMANCE ANALYTICS")
print("                    INSIGHTX")
print("=" * 60)

print("\nCLASS OVERVIEW")
print("-" * 60)

print(f"Students          : {len(data)}")
print(f"Class Average     : {class_average:.2f}%")
print(f"Highest Average   : {highest_average:.2f}%")
print(f"Lowest Average    : {lowest_average:.2f}%")
print(f"Passed Students   : {pass_count}")
print(f"Failed Students   : {fail_count}")
print(f"Pass Rate         : {(pass_count / len(data)) * 100:.2f}%")
print(f"Best Subject      : {best_subject}")
print(f"Subject Average   : {best_subject_average:.2f}%")


# -------------------------------
# TOP PERFORMERS
# -------------------------------

print("\n")
print("TOP 5 PERFORMERS")
print("-" * 60)

top_students = data.head(5)

for _, student in top_students.iterrows():

    print(
        f"{int(student['Rank']):<6}"
        f"{student['Name']:<15}"
        f"{student['Average']:.2f}%"
    )


# -------------------------------
# SUBJECT ANALYSIS
# -------------------------------

print("\n")
print("SUBJECT-WISE PERFORMANCE")
print("-" * 60)

for subject in SUBJECTS:

    average = data[subject].mean()

    print(
        f"{subject:<15}"
        f"{average:.2f}%"
    )


# -------------------------------
# COMPLETE STUDENT REPORT
# -------------------------------

print("\n")
print("STUDENT PERFORMANCE TABLE")
print("-" * 60)

print(
    data[
        [
            "Rank",
            "Student_ID",
            "Name",
            "Average",
            "Grade",
            "Result",
            "Attendance"
        ]
    ].to_string(index=False)
)


print("\n")
print("=" * 60)
print("              ANALYSIS COMPLETED")
print("=" * 60)

# -------------------------------
# INTERACTIVE MENU
# -------------------------------

while True:

    show_header()

    print("\n")
    print("=" * 60)
    print("                 INSIGHTX MENU")
    print("=" * 60)

    print("1. View Class Dashboard")
    print("2. View Top Performers")
    print("3. Search Student")
    print("4. Subject Analysis")
    print("5. Attendance Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------
    # OPTION 1 - CLASS DASHBOARD
    # --------------------------------

    if choice == "1":

        show_section("CLASS DASHBOARD")

        print(f"Total Students     : {len(data)}")
        print(f"Class Average      : {class_average:.2f}%")
        print(f"Highest Average    : {highest_average:.2f}%")
        print(f"Lowest Average     : {lowest_average:.2f}%")
        print(f"Passed Students    : {pass_count}")
        print(f"Failed Students    : {fail_count}")
        print(f"Pass Rate          : {(pass_count / len(data)) * 100:.2f}%")
        print(f"Best Subject       : {best_subject}")

    # --------------------------------
    # OPTION 2 - TOP PERFORMERS
    # --------------------------------

    elif choice == "2":

        show_section("TOP PERFORMERS")

        for _, student in data.head(5).iterrows():

            print(
                f"Rank {int(student['Rank'])}  |  "
                f"{student['Name']:<15} | "
                f"{student['Average']:.2f}% | "
                f"Grade {student['Grade']}"
            )

    # --------------------------------
    # OPTION 3 - SEARCH STUDENT
    # --------------------------------

    elif choice == "3":

        student_id = input("\nEnter Student ID: ").upper()

        student = data[
            data["Student_ID"] == student_id
        ]

        if student.empty:

            print("\nStudent not found.")

        else:

            student = student.iloc[0]

            show_section("STUDENT INSIGHT")

            print(f"Student ID        : {student['Student_ID']}")
            print(f"Name              : {student['Name']}")
            print(f"Department        : {student['Department']}")
            print(f"Attendance        : {student['Attendance']}%")
            print(f"Total Marks       : {student['Total']}")
            print(f"Average           : {student['Average']:.2f}%")
            print(f"Grade             : {student['Grade']}")
            print(f"Result            : {student['Result']}")
            print(f"Performance       : {student['Performance']}")
            print(f"Strongest Subject : {student['Strongest Subject']}")
            print(f"Needs Focus       : {student['Needs Focus']}")

    # --------------------------------
    # OPTION 4 - SUBJECT ANALYSIS
    # --------------------------------

    elif choice == "4":

        show_section("SUBJECT ANALYSIS")

        for subject in SUBJECTS:

            average = data[subject].mean()

            print(f"{subject:<15} : {average:.2f}%")

        print("\nBest Subject:", best_subject)

    # --------------------------------
    # OPTION 5 - ATTENDANCE ANALYSIS
    # --------------------------------

    elif choice == "5":

        attendance_average = data["Attendance"].mean()

        high_attendance = (
            data["Attendance"] >= 75
        ).sum()

        low_attendance = (
            data["Attendance"] < 75
        ).sum()

        show_section("ATTENDANCE ANALYSIS")

        print(
            f"Average Attendance : "
            f"{attendance_average:.2f}%"
        )

        print(
            f"Students >= 75%   : "
            f"{high_attendance}"
        )

        print(
            f"Students < 75%    : "
            f"{low_attendance}"
        )

            # --------------------------------
    # OPTION 6 - VISUAL ANALYTICS
    # --------------------------------

    elif choice == "6":

        while True:

            show_section("VISUAL ANALYTICS")

            print("1. Subject Performance")
            print("2. Top 10 Students")
            print("3. Grade Distribution")
            print("4. Attendance vs Performance")
            print("5. Back to Main Menu")

            chart_choice = input("\nChoose a chart: ")

            if chart_choice == "1":

                subject_performance_chart(
                    data,
                    SUBJECTS
                )

            elif chart_choice == "2":

                student_performance_chart(data)

            elif chart_choice == "3":

                grade_distribution_chart(data)

            elif chart_choice == "4":

                attendance_vs_performance(data)

            elif chart_choice == "5":

                break

            else:

                print("Invalid choice.")
    # --------------------------------
    # OPTION 6 - EXIT
    # --------------------------------

    elif choice == "6":

        print("\nThank you for using INSIGHTX!")
        print("Student Performance Analytics System")
        break

    else:

        print("\nInvalid choice. Please select 1-6.")

        
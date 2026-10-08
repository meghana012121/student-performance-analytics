import matplotlib.pyplot as plt
import pandas as pd


def subject_performance_chart(data, subjects):
    """Display average marks for each subject."""

    averages = data[subjects].mean()

    plt.figure(figsize=(9, 5))

    plt.bar(
        averages.index,
        averages.values
    )

    plt.title("Subject-wise Average Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)

    for subject, value in averages.items():
        plt.text(
            subject,
            value + 1,
            f"{value:.1f}",
            ha="center"
        )

    plt.tight_layout()
    plt.show()


def student_performance_chart(data):
    """Display top 10 student averages."""

    top_students = data.head(10)

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_students["Name"],
        top_students["Average"]
    )

    plt.title("Top 10 Student Performance")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.ylim(0, 100)

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def grade_distribution_chart(data):
    """Display grade distribution."""

    grade_counts = data["Grade"].value_counts()

    plt.figure(figsize=(7, 5))

    plt.bar(
        grade_counts.index,
        grade_counts.values
    )

    plt.title("Grade Distribution")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.show()


def attendance_vs_performance(data):
    """Compare attendance with average marks."""

    plt.figure(figsize=(8, 5))

    plt.scatter(
        data["Attendance"],
        data["Average"]
    )

    plt.title("Attendance vs Academic Performance")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Average Marks (%)")

    plt.grid(True)

    plt.tight_layout()
    plt.show()
import numpy as np


def calculate_total(marks):
    """Calculate total marks."""
    return np.sum(marks)


def calculate_average(marks):
    """Calculate average marks."""
    return np.mean(marks)


def assign_grade(average):
    """Assign grade based on average marks."""

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(marks, attendance):
    """Check whether a student has passed."""

    if min(marks) >= 40 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"


def get_performance_level(average):
    """Give a simple performance description."""

    if average >= 90:
        return "Outstanding"
    elif average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Average"
    else:
        return "Needs Improvement"


def find_strongest_subject(marks, subjects):
    """Find the subject in which the student scored highest."""

    highest_index = np.argmax(marks)
    return subjects[highest_index]


def find_weakest_subject(marks, subjects):
    """Find the subject in which the student scored lowest."""

    lowest_index = np.argmin(marks)
    return subjects[lowest_index]
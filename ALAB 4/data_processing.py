def get_average_Grades(grades):
    try:
        if not grades:
            raise ValueError("The grades list is empty.")
        
        total = sum(grades)
        average = total / len(grades)
        return average
    except ValueError as ve:
        print("ValueError:", ve)

course_grades = {
    "Math": [85, 92, 78],
    "Science": [90, 88, 95],
    "History": [95, 92, 88]
}
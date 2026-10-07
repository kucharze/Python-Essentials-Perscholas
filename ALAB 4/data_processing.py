def get_average_Grades(grades):
    try:
        if not grades:
            raise ValueError("The grades list is empty.")
        
        total = sum(grades)
        average = total / len(grades)
        return average
    except ValueError as ve:
        print("ValueError:", ve)

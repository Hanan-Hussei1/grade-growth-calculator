def calculate_grade_growth(initial_grade, grade_increase_rate, school_years):
    final_grade = initial_grade * (1 + grade_increase_rate / 100) ** school_years
    grade_growth = final_grade - initial_grade
    return grade_growth
initial_grade = float(input("Enter the initial grade: "))
grade_increase_rate = float(input("Enter the grade increase rate (in percentage): "))
school_years = int(input("Enter the number of school years: "))

grade_growth = calculate_grade_growth(initial_grade, grade_increase_rate, school_years)

print("Grade growth:", grade_growth)
print("Final grade:", initial_grade + grade_growth)

def analyze_result(name, roll, marks):

    # Calculate total
    total = sum(marks)

    # Calculate average
    average = total / len(marks)

    # Find grade
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Display student details
    print("\n----- Student Result -----")
    print("Student:", name)
    print("Roll:", roll)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)

    # Find subjects below 40
    print("Subjects below 40:")

    found = False

    for i in range(len(marks)):
        if marks[i] < 40:
            print("Subject", i + 1)
            found = True

    if not found:
        print("None")


# Get student details
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))

# Get 5 subject marks
marks = []

for i in range(5):
    mark = float(input("Enter mark for Subject " + str(i + 1) + ": "))
    marks.append(mark)

# Call the function
analyze_result(name, roll, marks)
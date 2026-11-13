print("=" * 50)
print("          SCHOOL RESULT PROCESSING")
print("=" * 50)

# 1. Enter student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# 2. Enter marks for 5 subjects
marks = []

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

for i in range(1, 6):
    while True:
        mark = float(input(f"Enter marks for Subject {i}: "))

        if mark < 0 or mark > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
        else:
            marks.append(mark)
            break

# 3. Calculate total and percentage
total = sum(marks)
percentage = (total / 500) * 100

# 4. Check passing status
if any(mark < 40 for mark in marks):
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"

else:
    result = "PASS"

    if percentage >= 90:
        grade = "A+"
        remark = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        remark = "Excellent"
    elif percentage >= 70:
        grade = "B"
        remark = "Very Good"
    elif percentage >= 60:
        grade = "C"
        remark = "Good"
    elif percentage >= 50:
        grade = "D"
        remark = "Satisfactory"
    elif percentage >= 40:
        grade = "E"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

# 5. Display report card
print("\n" + "=" * 50)
print("             STUDENT REPORT CARD")
print("=" * 50)

print(f"Student Name : {name}")
print(f"Roll Number  : {roll_no}")
print("-" * 50)

for i in range(5):
    print(f"Subject {i + 1} Marks : {marks[i]:.1f}")

print("-" * 50)
print(f"Total Marks  : {total:.1f} / 500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Result       : {result}")
print(f"Grade        : {grade}")
print(f"Remarks      : {remark}")

print("=" * 50)
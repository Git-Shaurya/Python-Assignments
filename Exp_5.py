n = int(input("Enter number of students: "))
total = 0

for i in range(n):
    sum_marks = 0
    print("Student", i + 1)

    for j in range(5):
        marks = float(input("Enter test marks: "))
        sum_marks += marks

    average = sum_marks / 5
    total += average
    print("Student average:", average)

print("Overall class average:", total / n)
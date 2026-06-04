# Exercise 
scores = [32,45,67,89,34,90,76]

# Printing scores greater than 45
scores_greater_than_45 = []
for i in range(len(scores)):
    if scores[i] > 45:
        scores_greater_than_45.append(scores[i])

print(f"The scores greater than 45 are: {scores_greater_than_45}")

# Average score
average_score = sum(scores)/len(scores)
print(f"The average score is {average_score}")

# How many students passed
passed_students_count = 0
for i in range(len(scores)):
    if scores[i] >= 45:
        passed_students_count += 1

print(f"The number of students who passed are {passed_students_count} students")
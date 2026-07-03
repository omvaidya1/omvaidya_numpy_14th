import numpy as np

# -------------------------------
# Step 1: Generate marks matrix
# 10 students × 5 subjects
# Marks range: 30 to 100
# -------------------------------
marks = np.random.randint(30, 101, size=(10, 5))

print("Student Marks (10x5):")
print(marks)

# -------------------------------
# Step 2: Total and Average per student
# axis=1 → row-wise operation (each student)
# -------------------------------
total_marks = np.sum(marks, axis=1)
average_marks = np.mean(marks, axis=1)

print("\nTotal Marks (per student):")
print(total_marks)

print("\nAverage Marks (per student):")
print(average_marks)

# -------------------------------
# Step 3: Highest and Lowest scorer
# argmax/argmin gives student index
# -------------------------------
highest_student = np.argmax(total_marks)
lowest_student = np.argmin(total_marks)

print("\nStudent with Highest Total Marks:", highest_student)
print("Student with Lowest Total Marks:", lowest_student)

# -------------------------------
# Step 4: Class statistics
# -------------------------------
class_mean = np.mean(marks)
class_std = np.std(marks)

print("\nClass Mean Marks:", class_mean)
print("Class Standard Deviation:", class_std)

# -------------------------------
# Step 5: Reshape and extract top 3 students
# (Already 2D; reshape shown for demonstration)
# Sorting students by total marks
# -------------------------------
top3_students = np.argsort(total_marks)[-3:]  # last 3 highest

print("\nTop 3 Students (row indices):", top3_students)

print("\nMarks of Top 3 Students:")
print(marks[top3_students])

# -------------------------------
# Step 6: Example of indexing
# Access marks of first student, first subject
# -------------------------------
print("\nExample Indexing:")
print("Marks of Student 0, Subject 0:", marks[0, 0])
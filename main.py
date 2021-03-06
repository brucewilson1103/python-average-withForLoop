student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for n in student_heights:
  total = n + total
  average = total/len(student_heights)

print(average)



# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0
count = 0
#Write your code below this row 👇
for ht in student_heights:
    total += ht
    count+=1

print(round(total/count))



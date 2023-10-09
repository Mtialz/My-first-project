
name = input("firstname: ")
last_name = input("lastname ")
grade1 = float(input("grade1: "))
grade2 = float(input("garde2: "))
grade3 = float(input("grade3: "))

 
average = (grade1 + grade2 + grade3) / 3
 
if average >= 17:
    status = "great"
elif average >= 14:
    status = "normal"
else:
    status = "failed"

print("name: " ,name)
print("Last name:",last_name)
print("avrage:",average)
print("status:",status)
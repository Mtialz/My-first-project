weight = float(input("please enter your weight in Kg" ))
height = float(input("Please enter your height in M "))
bmi = weight/(height**2)

if bmi < 18.5:
    print ("UnderWeight")
elif 18.5 <= bmi < 24.9:
    print("NormalWeight")
elif 25 <= bmi < 29.9:
    print("OverWeight")
elif 30 <=bmi <34.9:
    print("Obeslity")
else:
    print("Extreme obesilty")

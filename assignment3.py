# BMI calculator

def calculate_BMI():

    print("This is a BMI calculator")

    weight = float(input("wha is your wight in kg: "))
    hight = float(input("what is your hight m: "))

    BMI = weight/(hight**2)

    if BMI < 18.5 :
        print("underweight")

    elif BMI >= 18.6 and BMI <= 24.9 :
        print("normal weight")
    
    elif BMI >= 25 and BMI <= 29.9 :
        print("overwight")

    elif BMI >= 30 and BMI <= 34.9 :
        print("class 1 obese")

    elif BMI >= 35 and BMI <= 39.9 :
        print("class 2 obese")
    
    else :
        print("class 3 obese")

calculate_BMI()
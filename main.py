from calculate import sum,division,minus,multiply
while True :

    num1 = int(input("what is the first number in your calculation: "))
    num2 = int(input("what is the second number in your calculation: "))

    operator = input("what operation would you like to perform (+,-,*,/,%,press E for exit) : ")

    if operator == "+" :
        # print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} + {num2} = {sum(num1,num2)}")


    elif operator == "-" :
        print(f"{num1} - {num2} = {num1 - num2}")

    elif operator == "*" :
        print(f"{num1} * {num2} = {num1 * num2}")

    elif operator == "/" :
        print(f"{num1} / {num2} = {num1 / num2}")

    elif operator == "%" :
        print(f"{num1} % {num2} = {num1 % num2}")

    elif operator == "E" :
        break
    
    else :
        print("you have entered an incorrect symbol, please try again and pick a symbol from the options presented to you")
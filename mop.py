def calculator():
    while True:
        try:
            one_number = float(input("the first number"))
            action = input("action")
            two_number = float(input("the second number"))

            match action:
                case "+":
                    print(one_number + two_number)
                case "-":
                    print(one_number - two_number)
                case "*":
                    print(one_number * two_number)
                case "/":
                    print(one_number / two_number)
                case "**":
                    print(one_number ** two_number)
        except ValueError:
            print("ValueError") 

calculator()
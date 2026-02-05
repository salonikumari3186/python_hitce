num1= int(input("Enter a number1: "))
num2= int(input("Enter a number2: "))
operators=["+","-","*","/","%","**","//"]
operator = input("Enter opreator(+,-,/,%,**,//,):")

if operator not in operators:
    print("Enter a valid operetor")
else:
    match operator:
        case "+":
            print("Sum is:",num1+num2)
        case "-":
            print("differece is:",num1-num2)
        case "*":
            print("product is:",num1*num2)
        case "/":
            if num2 !=0:
                print("Division is:",num1/num2)
            else:
                print("cannot divide by zero")
        case "%":
            if num2 != 0:
                print("Modulos is",num1%num2)
            else: 
                print('cannot modulos by Zero')
        case "**":
            print("Exponentiation is:",num1**num2)
        case"//":
            if num2 != 0:
                print("Floor division is:",num1//num2)
            else:
                print("cannot divide by zero")
        case _ :
            print("Enter a valid operator")                                      
   
   

def menu():
    print("1. Add")
    print("2.substract")
    print("3.Multiply ")
    option= int(input("Enter your option "))
    return option



def opretor (choice):
    a =int(input("Enter a first number:"))
    b = int(input("Enter a second mumber"))

    if choice ==1:
        print("ADD=",a+b)
    elif choice ==2:
        print("SUB=",a-b)
    elif choice == 3:
        print("MUL=",a*b)
    else:
        print("Inalid option")
                    


choice=menu()
opretor(choice)

               








        

'''x= int(input("Enter a first number"))
y= int(input("Enter a second number"))

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)    

def menu():
    print("1.multiply")
    print("2.divide")
    option= int(input("please enter option: "))
    return option
def dashboard():
    number=menu()
    if number==1:
        multiply(x,y)

    elif number==2:
        divide(x,y)

    else:
        print("Invalid option")

dashboard()    '''


# def get_number(x,y=2):
#     return x/y
# print(get_number(10,20))
# get_number(10,20)

def user_input():
      

     id = int(input("Enter a ID "))
     name=input("Enter a name ")
     return id,name

def user_output(id,name):
     print("ID",id)
     print("Name",name)

id,name=user_input()
user_output(id,name)
listdata=[]

while True:
    print("<===== MENU =====>")
    print("1. Registration ")
    print("2. Search Id Record ")
    print("3. Exit.")
    choice=int(input("Enter your choice "))

    if choice==1:
        print("<---- Registration ---->")
        
        student={}
        student["id"]=input("Enter a Id:")
        student["name"]=input("Enter a name")
        student["email"]=input("Enter a Email")
        student["address"]=input("Enter a Address")
        listdata.append(student)
        print(listdata)

        print("Registration Sucessfully ")

    elif choice==2: 
        print("search by Id --->")
        search_id = input("Enter a id  to Saerch:")
        found = False

        for i in listdata:
            if i ["id"]== search_id:
                print("Id:",i ["id"])
                print("Name:",i["name"])
                print("Email:",i["email"])
                print("Address:",i["address"])

                break
        else:
            print("record not found")
            
    elif choice==3:
        print("Exit")
        break
    else:
        print("Invalid choice: ") 







    
    





#listdata=[]

# for i in range(1,3):
    
#     student= {}
#     student["id"]=(input("Enter id")), 
#     student["name"]=input("enter name")     
    
#     listdata.append(student)
#     print(listdata)
    
    


























    


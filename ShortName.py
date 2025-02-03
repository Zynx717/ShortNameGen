print("== Welcome To The Short Name Gen ==\n")

UserName = []

Q_Name = input("Enter Your Name: ").upper()
Q_FullName = input("Enter Your Full Name: ").upper()

if Q_Name == "" or Q_FullName == "" or Q_Name == " " or Q_FullName == " ":
    print("Invaild Name, Pls Try Agein")
else : 
    UserName.append(Q_Name[0])
    UserName.append(Q_FullName[0])
    
print(",".join(UserName))

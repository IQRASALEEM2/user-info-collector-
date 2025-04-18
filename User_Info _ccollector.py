def collect_user_info():
    user_name=input("Enter your Name : ")
    Father_name=input("Enter a father Name : ")
    age=input("Enter your age : iqra")

    with open("user_info.txt","a") as file:
        file.write(f"Name:{user_name}, age :{age}, father Name {Father_name}")
    
    print("\n user info Added Sucessfully")

while True:
    collect_user_info ()
    again= input("Do you want to add another User info? (yes/no):").strip().lower()
    if again !="yes":
            print("goodbye")
            break

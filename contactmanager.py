# contact manager

import json
import os

class Contact:
    def __init__(self,name,phone,email):
        self.name= name
        self.phone= phone
        self.email= email

    def to_dict(self):
        return {"name":self.name, "phone":self.phone, "email":self.email}
    
FILENAME= "contacts.json"

def load_contacts():
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as f:
                data= json.load(f)
                return [Contact(d["name"],d["phone"],d["email"]) for d in data]
        else:
            return [Contact("amy",984450834,"amy@gmail.com"),
          Contact("linda",984450434,"linda@gmail.com")
           ]
        
def save_contacts():
    with open(FILENAME, "w") as f:
        json.dump([c.to_dict() for c in contacts], f, indent=4)


contacts= load_contacts()

           

def view_all():
    for index,contact in enumerate(contacts):
        print(f"{index}:{contact.name}|{contact.phone}|{contact.email}")

while True:
    print("\nMenu")
    print("1.Add new contact")
    print("2.View all contacts")
    print("3.Search contact by name")
    print("4.Delete contact")
    print("5.Edit contact")
    print("6.Quit")
    try:
        choice=int(input("Enter the task you want to perform: "))
    except:
        print("invalid input!choose an integer!!")
        continue

    if choice==1:
        try:
         new_student_name= input("enter name of new student: ")
         new_student_phone=input("enter phone of new student: ")
         new_student_email= input("Enter email of new student: ")
         new_std_details= Contact(new_student_name,new_student_phone,new_student_email)
         contacts.append(new_std_details)
         save_contacts()
         print(f"{new_student_name}'s details sucessfully added!")
        except:
            print("invalid input! try again!!")
            continue
    elif choice==2:
        view_all()
        continue
    
    elif choice==3:
        std_name= input("enter name to search: ")
        for index,contact in enumerate(contacts):
            if std_name== contact.name:
                print(f"details of {contact.name}:{contact.phone},{contact.email}")
                break
        else:
            print("sorry! contact not found")
            continue

    elif choice==4:
        view_all()
        try:
            chc= int(input("enter the contact serial no to delete:"))
            contact= contacts.pop(chc)
            save_contacts()
            print(f"{contact.name} sucessfully deleted ")
        except:
            print("invalid input!!")
            continue

    elif choice==5:
        view_all()
        try:
            idx = int(input("Enter index to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new number: ")
            email = input("Enter new email: ")
            contacts[idx] = Contact(name, phone, email)
            save_contacts()
            print("Contact updated successfully!")
        except:
            print("value error !!")
            continue

    elif choice==6:
        break










        
    
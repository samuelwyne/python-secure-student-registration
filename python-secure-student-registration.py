students=[]

while True:
    
 student={}  
 student["name"]=input("Enter student's name: ")
 if student["name"].lower()=="exit":
    break
 while True:
    try:
     student["age"]=int(input("Enter student's age: "))
     if student["age"]>0:
        break
     elif student["age"]<160:
        break
     else :
        print("Invalid age try agin!")
    except ValueError:
        print("Invalid age try agin!")

 while True:
   try:
     student["marks"]=int(input("Enter student's marks: "))
     if student["marks"]>0 and student["marks"]<100:
        break
     else :
        print("Invalid marks try agin!")
   except ValueError:
        print("Invalid marks try agin!")    
 print("Enter exit to stop: ")
 students.append(student)
print()
print(f"{"="*5}STUDENT RECORDS{"="*5}")
for student in students:
  print(f"{student["name"]}--{student["age" ]}yrs old-- scored{student["marks"]}%")

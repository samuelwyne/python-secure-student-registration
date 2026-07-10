name={}
marks={}
age={}
i=0
while True:
 name[i]=input("Enter student's name: ")
 if name[i].lower()=="exit":
    break
 while True:
    try:
     age[i]=int(input("Enter student's age: "))
     if age[i]>0:
        break
     elif age[i]<160:
        break
     else :
        print("Invalid age try agin!")
    except ValueError:
        print("Invalid age try agin!")

 while True:
   try:
     marks[i]=int(input("Enter student's marks: "))
     if marks[i]>0 and marks[i]<100:
        break
     else :
        print("Invalid marks try agin!")
   except ValueError:
        print("Invalid marks try agin!")    
 print("Enter exit to stop: ")
 i+=1
print()
print(f"{"="*5}STUDENT RECORDS{"="*5}")
for j in range(i):
  print(f"{name[j]}--{age[j]}yrs old-- scored{marks[j]}%")
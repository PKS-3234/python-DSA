#LIST

#creat list
list=[]

#add elements to list
list.append("a")
list.append("b")
list.append("c")

#remove element from list
list.remove("b")

#print list
print("List: ",list)
print("Length of list: ",len(list))


######################################################################################

#TUPLE

#creat tuple
emp1=(101,"A","Finance")
emp2=(102,"B","HR")
emp3=(103,"C","Finance")

#add elements to list
employees=[emp1,emp2,emp3]

#print tuple
for emp in employees:
  if emp[2]=="Finance":
    print(f"ID:{emp[0]}, Name:{emp[1]}")

################################################################################

#DICTIONARY

#create dictionary
grades={}

print("\nMenu:")
while(True):
  print("1. Add a grade")
  print("2. Update grades")
  print("3. View grades")
  print("4. Exit")

  choice=int(input("Enter your choice: "))

  if choice==1:
    name=input("Enter student name: ")
    grade=input("Enter grade: ")
    grades[name]=grade

  elif choice==2:
    name=input("Enter student name: ")
    if name in grades:
      grade=input("Enter new grade: ")
      grades[name]=grade
    else:
      print("Student not found")

  elif choice==3:
    print("Grades:")
    for name,grade in grades.items():
      print(f"{name}: {grade}")

  elif choice==4:
    print("Exiting...")
    break

  else:
    print("Invalid choice")
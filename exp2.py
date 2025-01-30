# 1-D ARRAY
arr=[10,20,30,40,50]
print("Element at index 2: ",arr[2])
print("Elements of array:")
for num in arr:
  print(num)

print("Length of array :",len(arr))

#############################################################################

# 2-D ARRAY
arr2d=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
print("Element at index [1][2]: ",arr2d[1][2])

#traverse array
print("Elements of array:")
for row in arr2d:
  for ele in row:
    print(ele,end=" ")
  print()

  #################################################################################

#MULTI-DIMENSIONAL ARRAY

import numpy as np
multi_arr=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
    ])
print("Element at position [1][0][1]:",multi_arr[1][0][1])

#traverse array
print("Elements of array:")
for matrix in multi_arr:
  for row in matrix:
    for ele in row:
      print(ele,end=" ")
    print(",",end=" ")
  print()

###########################################################################

#ARRAY OPERATIONS

arr=[10,20,30,40]
print("Original array:",arr)
arr.append(50)
print("Array after appending 50:",arr)
arr.insert(2,25)
print("Array after inserting 25 at index 2:",arr)
arr.pop()
print("Array after popping last element:",arr)
arr.pop(1)
print("Array after popping element at index 1:",arr)

#################################################################################

#SEARCHING
arr=[10,20,30,40,50]

#linear search
def linear_search(arr,x):
  for i,ele in enumerate(arr):
    if ele==x:
      return i
  return -1

#binary search
def binary_search(arr,x):
  low,high=0,len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==x:
      return mid
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return -1

print("Linear search for 30:",linear_search(arr,30))
print("Binary search for 40:",binary_search(arr,40))

######################################################################

#grocery store bill

items=['a','b','c','d']
price=[10,20,30,40]

def bill(items,price,quantity):
  total=0
  for i in range(len(items)):
    total+=price[i]*quantity[i]
  return total

q1=int(input("Enter number of item 'a': "))
q2=int(input("Enter number of item 'b': "))
q3=int(input("Enter number of item 'c': "))
q4=int(input("Enter number of item 'd': "))

quantity=[q1,q2,q3,q4]
print("Total bill:",bill(items,price,quantity))

##################################################################################


# a teacher inputs marks for multiple students across multiple subjects and calculate the average marks for each students

students=int(input("Enter number of students: "))
subjects=int(input("Enter number of subjects: "))

marks=[]
for stu in range(students):
  marks.append([])
  for sub in range(subjects):
    marks[stu].append(int(input(f"Enter marks for student {stu+1} in subject {sub+1}: ")))

for stu in range(students):
  total=0
  for sub in range(subjects):
    total+=marks[stu][sub]
  print(f"Average marks for student {stu+1}: {total/subjects}")

##################################################################################################
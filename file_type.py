# -*- coding: utf-8 -*-
"""file.type

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PVcS2_uatBjSP5nMEA8AEb6Fvi2oi3Ki
"""

a=30
b=20
temp=b
b=a
a=temp
print(a,b)



a=0
print(a)
b=1
print(b)
c=b+a
print(c)
d=c+b
print(d)
e=d+c
print(e)
f=d+e
print(f)
g=f+e
print(g)
h=g+f
print(h)
i=h+g
print(i)

a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,3,4,5]
for i in range(0,5):
    print(i)
    #print(b[1])+a[0])
    #print(b[2])+a[1])
    #print(b[3])+a[2])
    #print(b[4])+a[3])
    #print(1,5)
    #print(i-1)

a=[76,34,21,67,87]
b=0
for i in range(0,5):
  if a[i]>b:
    b = a[i]
print(b)

a=[5,4,3,2,1]
b=[]
for i in range(0,5):
  i=-i
  b.append(a[i])
print(b)

lst=[10,11,12,13]
lst[::-1]
print(lst[::-1])

b=[5,4,3,2,1]
b.sort()
b

a=[1,2,3,4,5]
for i in range(len(a)):
  if a[i]>a[1+1]:
    print(a[i])

array1=[1,2,3,4,5]
min=array1[0]


for i in (array1):
  if i<min:
    min=i
print(min)

a=(1,2,3,4,5)
for i in range(5,0,-1):

    print("*"*i)

for i in range(1,5):

  print("* "*i)

for i in range(6,0,-1):

  print("* "*i)

j=5
for i in range (5,1,-1):
  print(' ' * (i), '@ ' * (j-i+1) )

j=5
for i in range(1,5):
  print(' ' * (i), '@ ' * (j-i) )

array1= [1,2,3,4,5]
max=array1[0]


for i in (array1):
  if i-1 > max:
    max=i-1
print(max)

a=0
print(a)
b=1
print(b)
c=b+a
print(c)
d=c+b
print(d)
e=d+c
print(e)

user= int(input('enter any number'))
print(user * 2)

a= 'ameermuzammil'
 for i in range(1,10)

array=[0,1]
user1=int(input('enter any number'))
def feb (array,user1):
    for i in range(user1):
      array.append(array[-1]+array[-2])

    return array

print(feb(array,user1))

array1 = ['cat','dog','rat','catdogcat','hippotamas','rhinosaurous']
array2=  ['cat','dog','rat','catdogcat','hippotamas','rhinosaurous']
array3=  ['cat','dog','rat','hippotamas','rhinosaurous']
for i in range(len(array1)):
  for n in range (len(array3)):
      if array1[i] == array3[n]:
        array2.remove(array1[i])
print(array2)

array=[ [5,8,6],
      [6,10,6],
      [7,8,5] ]
print(array[1][1])

output=[8,7,6,5]

flattened_array = array.flattened()
print("Sorted Flattened Array:")
print(sorted_array)

sorted_rows = np.sort(array, axis=1)
print("Sorted Rows:")
print(sorted_rows)

sorted_colums = np.sort(array, axis=0)
print("Sorted Colums:")
print(sorted_colums)

class car:
  def set_details(self,make,model,year,color):
    self.make=make
    self.model=model
    self.year=year
    self.color=color

  def display_info(self):
    print(f'{self.make} {self.model} {self.year} in {self.color}')

car1=car()
car1.set_details('Toyota','Corolla',2023,'black')
car1.display_info()

car1=car()
car1.set_details('Honda','Civic',1992,'red')
car1.display_info()

class students:
  def set_details(self, name, fathers_name, class_name, fee):
    self.name = name
    self.fathers_name=fathers_name
    self.class_name=class_name
    self.fee=fee

  def display_info(self):
    print(f'{self.name} {self.fathers_name} {self.class_name} {self.fee}')

class1 = students()
class1.set_details('Ahmed','Zaid','second_grade',12000)
class1.display_info()

def find_second_largest(arr):
    if len(arr) < 2:
        return None

    first_max = second_max = float('-inf')

    for num in arr:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max

arr= [1,2,3,4,5]
find_second_largest(arr)
print("Second largest number in the array:", "4")

class student:
  def set_details(self,name,fathername,grade,fees):
    self.name=name
    self.fathername=fathername
    self.grade=grade
    self.fees=fees
  def display_info(self):
    print(f"{self.name} {self.fathername} {self.grade} {self.fees}")
students=student()
students.set_details('hamza','fazal',9,2000)
students.display_info()
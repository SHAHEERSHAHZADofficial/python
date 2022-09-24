#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[17]:


a=2
b=3
c=a+b
print(c)


# In[ ]:


print("Hello Mohammed")
#hello world programm


# In[14]:


# ASSIGNMENT 2 WITH INPUT  STARTED

name =input("enter their name ")
print("student:",name)
computer=int(input("enter your computer marks from 100:"))
print("computer:",computer)
math=int(input("enter your math marks from 100:"))
print("math:",math)
physics=int(input("enter your physics marks from 100:"))
print("physics:",physics)
addmath=int(input("enter your addmath marks from 100:"))
print("addmath:",addmath)
islamiat=int(input("enter your islamiat marks from 100:"))
print("islamiat:",islamiat)
total=computer+islamiat+math+physics+addmath
print("totalmarks:",total)
percentage=total/500*100
print("your percentage is :",percentage)
if percentage>=90:
  print("Grade:A*")
elif percentage>=80:
  print("grade:A")
elif percentage>=70:
   print("grade:B")
elif percentage>=60:
   print("grade:C")
elif percentage>=50:
   print("grade:D")
elif percentage>=40:
   print("grade:E")
else :
   print("grade:Fail")
# ASSIGNMENT 2 WITH INPUT  ENDED


# In[16]:


# ASSIGNMENT 2 STARTED

math=100
english=80
islamiat=90
total=math+english+islamiat
percentage=total/300*100;
print("your percentage is :",percentage,"%");
if  percentage< 100 and percentage >= 90:
  print("Grade:A*");
elif percentage<90 and percentage >= 80 :
  print("grade:A");
elif percentage<80 and percentage >= 70:
   print("grade:B");
elif percentage<70 and percentage >= 60:
  print("grade:C");
elif percentage<60 and percentage >= 50:
  print("grade:D");
elif percentage<50 and percentage >= 33:
  print("grade:E");
elif percentage <0:
  print("Enter Accurate Value");
else :
  print("grade:F");

# ASSIGNMENT 2 ENDED


# In[23]:


#list
name=["hello world","jupyterNoteBook","flask","diango"]
print(name)


# In[12]:



name


# In[15]:


name.insert(1,"javascript")
print(name)


# In[22]:


name


# In[25]:


name.append("ahmad")
print(name)


# In[27]:


print("hello Future Data scientist")


# In[15]:


# ASSIGNMENT 3 STARTED
# Write a Python program to print the following string in a specific format (see the output).
# Twinkle, twinkle, little star,
#        How I wonder what you are!
#                Up above the world so high,
#                Like a diamond in the sky.
# Twinkle, twinkle, little star,
#         How I wonder what you are
secondLine="How I wonder what you are!"
print("Twinkle, twinkle, little star,")
print("","","","","","","","How I wonder what you are!")
print("","","","","","","","","","","","","",""," Up above the world so high,")
print("","","","","","","","","","","","","",""," Like a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("","","","","","","","How I wonder what you are!")


# In[17]:


#Write a Python program to get the Python version you are using

from platform import python_version
print(python_version())


# In[22]:


# Write a Python program to display the current date and time.
from datetime import datetime
now = datetime.now()
print (now)


# In[ ]:


# Write a Python program which accepts the radius of a circle from the user and compute the area.


# In[35]:


# 5. Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them.
firstName= input("Write Your First Name : ")
lastName= input("Write Your Last Name : ")
arr=[firstName  ,  lastName]
arr.reverse()
print(arr)


# In[27]:


# Write a python program which takes two inputs from user and print them addition
firstNum=int(input("Enter First Number "))
lastNum=int(input("Enter First Number "))
total=firstNum+lastNum
print(total)


# In[28]:


# Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ?

name =input("enter their name ")
computer=int(input("enter your computer marks from 100:"))
math=int(input("enter your math marks from 100:"))
physics=int(input("enter your physics marks from 100:"))
addmath=int(input("enter your addmath marks from 100:"))
islamiat=int(input("enter your islamiat marks from 100:"))
total=computer+islamiat+math+physics+addmath
print("student:",name)
print("computer:",computer)
print("math:",math)
print("physics:",physics)
print("addmath:",addmath)
print("islamiat:",islamiat)
print("totalmarks:",total)
percentage=total/500*100
print("your percentage is :",percentage)
if percentage>=90:
  print("Grade:A*")
elif percentage>=80:
  print("grade:A")
elif percentage>=70:
   print("grade:B")
elif percentage>=60:
   print("grade:C")
elif percentage>=50:
   print("grade:D")
elif percentage>=40:
   print("grade:E")
else :
   print("grade:Fail")


# In[29]:


# Write a program which take input from user and identify that the given number is even or odd?
number=int(input("Enter Any Number : "))
mod=number%2
if mod>0 :
 print("Number is Odd");
else:
  print("Number is even");


# In[31]:


# Write a program which print the length of the list?
arr=[1,2,3,4,"abdullah","ali","hamza","ali"]
print(len(arr))


# In[36]:


# Write a Python program to sum all the numeric items in a list?


# In[37]:


# Write a Python program to get the largest number from a numeric list.


# In[14]:


# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Write a program that prints out all the elements of the list that are less than 5.


# In[1]:


# Assignment Ended


# In[8]:


a=(1,2,3,4,5,6)
b= 1,2,3,4,5
c=(1,)
d=(("a","b","c","d"),(1,2,3,4))
abcd=[a,b,c,d]
del d
print(abcd)


# In[13]:


lst=[1,2,3,4,5]
for i in lst:
 print(i)
for i in range(len(lst)):
 print(i)


# In[2]:


for i in range(10):
 if i%2==0:
  print(i)


# In[ ]:


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


# In[7]:


#  Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")     
num_1=int(input("Enter first number: "));  
num_2=int(input("Enter second number: "));

if choice == "1":
  print(num_1,"+",num_2,"=",add(num_1, num_2)) 

elif choice == "2":
  print(num_1,"-",num_2,"=",subtract(num_1, num_2))

elif choice =="3":
  print(num_1,"x",num_2,"=",multiply(num_1, num_2))

elif choice == "4":
  print(num_1,"/",num_2,"=",divide(num_1, num_2))


else:
 print("Invalid Choice")
 print("Enter Valid Choice ")


# 

# In[1]:


arr=[]
for i in range(10):
 input("enter any number")
print("the value is",i)
print("hello world")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





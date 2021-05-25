#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Create three variables in a single line and assign values to them in such a manner that each one of
#them belongs to a different data type.
a = int(1)
b = float(2.01)
c = str('string')
print(type(a), type(b), type(c))


# In[ ]:


#2. Create a variable of type complex and swap it with another variable of type integer.
d = complex()
d = a
print(type(d))


# In[ ]:


#3. Swap two numbers using a third variable and do the same task without using any third variable.
x=10
y=20
temp=y
y=x
x=temp
print(x,y)
a=10
b=15
a,b=b,a
print(a,b)


# In[ ]:


#4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
#Version.
print(input("please enter the no:"))


# In[ ]:


"""""
5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output.
"""""
a = int(input("select from numbers 1-10:"))
b = int(input("select from numbers 1-10:"))
z=a+b
result=z+30
print(result)


# In[ ]:


"""""
6. Write a program to check the data type of the entered values.
HINT: Printed output should say - The data type of the input value is : int/float/string/etc
"""""
p=input("please enter:")
print("The data type of the input value is", type(p))


# In[3]:


"""
7. Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
UPPERCASE.
"""
a=str("upperCamelcase")
b=str("UpperCamelcase")
c=str("upper_camelcase")
d=str("UPPERCAMELCASE")
print(a,b,c,d)


# In[5]:


"""
8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
again. Will it change the value? If Yes then Why?
"""
a=10
a="string"
print(a)

"""
yes it will take the latest datatype value
since we are assigning it to a variable which is empty box takes the value dynamically and reassigns to the latest value.
"""


# In[ ]:





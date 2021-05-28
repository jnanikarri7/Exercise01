#!/usr/bin/env python
# coding: utf-8

# In[14]:


#1. Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    1/0
except ZeroDivisionError:
    print("zero division error")


# In[46]:


"""
2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode.
"""
import sys
f= open("text.txt","w+")
f.write("This is line %d\r\n" )
fname="text.txt"
b=input("")

try:
        f = open(b,'r')
        print(f.read())
except:
    print("Renter the file name:", fname)


# In[48]:


#3. Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits” 
b=input("enter four digits:")
try:
    if len(b)!=4:
        raise ValueError
    else:
        print("4 digits entered")
except ValueError:
    print("The length is too short/long !!! Please provide only four digits")
    


# In[57]:


"""
4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.
"""
password="jnani"
b=input("enter the password:")
c=input("re enter the password:")
try:
    if b!=c:
        raise ValueError
    if password!=b:
        raise ValueError
    else:
        print("password matched")
except ValueError:
    print("mismatch with the password, please renter")

    


# In[59]:


#5. Go through the link provided below to understand finally and raise concept:
#https://www.programiz.com/python-programming/exception-handling
try:
    1/0
except ZeroDivisionError:
    print("finally block will be executed no matter what")
finally:
    print("its a zerodiv error")


# In[88]:


"""
6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present
"""
f= open("doc.txt","w+")
f.write("Hello I am a file Where you need to return the data string Which is of even length Make sure you return the content in The same link as it is present")
print(f.read())
  
cont = f.readlines()
type(cont)
for i in range(0, len(cont)):
    if(i % 2 == 0):
        f.write(cont[i])
f.close()
f = open('doc.txt', 'r')
print(f.read())
    


# In[84]:





# In[ ]:





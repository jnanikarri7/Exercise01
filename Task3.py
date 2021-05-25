#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
1. Create a list of 10 elements of four different data types like int, string, complex and float.
"""
mylist=[1,2,"jnana",2.3,1+2j,6,7,8,9,10]
print(mylist)


# In[13]:


#2. Create a list of size 5 and execute the slicing structure
a = ("a", "b", "c", "d", "e")
x = slice(0, 2)
print(a[x])


# In[16]:


#3. Write a program to get the sum and multiply of all the items in a given list
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result
def sumList(myList) :
    result = 0
    for x in myList:
         result = result + x
    return result
    
list1 = [1, 2, 3,4]
print(multiplyList(list1))
print(sumList(list1))


# In[32]:


#4. Find the largest and smallest number from a given list
list1 =[6,5,9,8,7]
orderedlist =sorted(list1)
x=slice(0,1)
y=slice(4,5)
print("smallest number is:",orderedlist[x])
print("largest number is:",orderedlist[y])


# In[52]:


#5. Create a new list which contains the specified numbers after removing the even numbers from a
#predefined list. 
list1 =[2,3,4,5,6,7]
list2 =[i for i in list1 if i%2!=0]
print(list2)
    


# In[66]:


#6. Create a list of elements such that it contains the squares of the first and last 5 elements between
#1 and30 (both included).
import random
randomlist = []

for i in range(1,6):
    randomlist.append(i*i)
for i in range(6,25):
     randomlist.append(i)
for i in range(25,31):
    randomlist.append(i*i)
print(randomlist)


# In[74]:


#7. Write a program to replace the last element in a list with another list.
list1=[1,3,5,7,9,10]
list2=[2,4,6,8]
count=len(list1)
list=list1.pop(count-1)
print(list1+list2)


# In[78]:


"""
8. Create a new dictionary by concatenating the following two dictionaries:
Sample input: a={1:10,2:20} b={3:30,4:40}
Expected output: {1:10,2:20,3:30,4:40}
"""
a={'1':10,'2':20} 
b={'3':30,'4':40}
res={**a,**b}
print(res)


# In[82]:


"""
9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
and n(both 1 and n included).
Sample input: n=5
Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

"""
a=int(input("enter a number that want to be printed for dict:"))
d = dict()

for x in range(1,a+1):
    d[x]=x*x

print(d)


# In[92]:


"""
10. Write a program which accepts a sequence of comma-separated numbers from console and
generates a list and a tuple which contains every number in the form of string.
Sample input: 34,67,55,33,12,98
Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
"""
a=int(input("enter number of numbers to be in list:"))
d=dict()
for i in range(1,a+1):
    list=input("enter the numbers in the list:")
    d[i]=list
print(d.values())
print(tuple(d.values()))
    


# In[ ]:





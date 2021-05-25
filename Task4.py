#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a program to reverse a string
a=input("enter string to be reversed:")
b=a[::-1]
print(b)


# In[ ]:


#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
#letters.
a="abcSdefPghijQkl"
l,u = 0,0
for i in a:
    if (i>='a'and i<='z'):
        l=l+1                 
    if (i>='A'and i<='Z'):
        u=u+1          
print('Lower case: ',l)
print('Upper case: ',u)


# In[ ]:


#3. Create a function that takes a list and returns a new list with unique elements of the first list.
def unique(list):
  x = []
  for a in list:
    if a not in x:
      x.append(a)
  return x
print(unique([1,2,2,3]))


# In[3]:


#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.
a=[i for i in input().split('-')]
a.sort()
print('-'.join(a))


# In[5]:


#5. Write a program that accepts a sequence of lines as input and prints the lines after making all
#characters in the sentence capitalized.
a=input("enter the sequence of lines:")
print(a.upper())


# In[9]:


#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.
def strsum(a,b):
    s=int(a)+int(b)
    return s
num1=str(input("enter first integral:"))
num2=str(input("enter second integral:"))
add=strsum(num1,num2)
print(add)


# In[22]:


"""
7. Define a function that can accept two strings as input and print the string with the maximum length
in the console. If two strings have the same length, then the function should print both the strings line
by line.
"""
def maxlen(a,b):
    a=input("enter first string:")
    b=input("enter second:")
    if len(a)>len(b):
        print("maximaum is:",a)
    if len(a)==len(b):
        print(a,b)
    if len(b)>len(a):
        print(b)
maxlen(a,a)

    


# In[39]:


#8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).
def tup():
    l=list()
    for a in range(1,21):
        l.append(a**2)
    print(tuple(l))
tup()


# In[42]:


#9. Write a function called showNumbers that takes a parameter called limit. It should print all the
#numbers between 0 and limit with a label to identify the even and odd numbers
def showNumbers(limit):
 for i in range(0,limit+1):
    print(i,end=" ")
    if(i%2==0):
        print("EVEN")
    else:
        print("ODD")

limit=int(input("Enter limit:"))
showNumbers(limit)


# In[44]:


#10. Write a program which uses filter() to make a list whose elements are even numbers between 1
#and 20 (both included)
def filter():
    l=list()
    for i in range(1,21):
        if (i%2==0):
            l.append(i)
    print(l)
filter()
        


# In[69]:


"""
11. Write a program which uses map() and filter() to make a list whose elements are squares of even
numbers in [1,2,3,4,5,6,7,8,9,10].
Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
numbers in the filtered list. Use lambda() to define anonymous functions.

"""
def filter():
    l=list()
    for i in range(1,11):
        if (i%2==0):
            l.append(i)
    return l
eve_num = map(lambda x: x**2, filter())
 
print(eve_num)


# In[72]:


#12. Write a function to compute 5/0 and use try/except to catch the exceptions
try:
    5/0
except:
    ZeroDivisionError
    print("its a zdiverror")


# In[77]:


#13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
import functools
functools.reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7], 0)


# In[88]:


"""
14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
Make sure to use only higher order functions.

"""
def multpl(a):
    if a%7==0:
        print("multiple of 7")
a=int(input("enter number to check:"))
def check(a):
    if a%3!=0:
        print("not divisible by 3")
    else:
        print("divisible by 3")
    return multpl(a)
check(a)


# In[93]:


"""
15. Write a program in Python to multiply the elements of a list by itself using a traditional function
and pass the function to map() to complete the operation.
"""
list=map(lambda x: x*x,[1, 2, 3])
print(list)


# In[96]:


"""
16. What is the output of the following codes:
(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)
sol: it returns the finally loop value, 2

(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()
sol: it returns the finally loop, after f
after f?

"""


# In[ ]:





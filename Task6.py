#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1. Write a program in Python to find out the character in a string which is uppercase using list
#comprehension.
s="Jnana"
a = [char for char in s if char.isupper()]
print(a)


# In[14]:


"""
2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
"""
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
a={students[i]:subjects[i] for i in range(len(students))}
print(str(a))
x=zip(students,subjects)
print(tuple(x))


# In[23]:


#3. Learn More about Yield, next and Generators
def randgen():
    for i in range(0,5):
        i+=1
        print("this is ",i)
        yield i
a=randgen()
next(a)
next(a)
next(a)


# In[25]:


"""
4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training”
"""
string=("Consultadd Training")
print(string[::-1])


# In[26]:


#5. Write an example on decorators.
def cap(text):
    return text.upper()
print(cap('jnana'))
capi=cap
print(capi('jnana'))


# In[ ]:





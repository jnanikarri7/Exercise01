#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
1. Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
Access list: [1, 2, 3, 4]Access list: [600, 700]
Access list: [100, 300, 500, 600, 800]
Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
Access list: [10]
Access list: [ ]

"""
lists= [[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]]
print(lists[0][5][0:4])
print(lists[0][6:8])
print(lists[0][0:10:2])
print(lists[0][::-1])
print(lists[0][5][5][0])
lists= []
print(lists)


# In[ ]:


#2. Create a list of thousand numbers using range and xrange and see the difference between each
#other.
import sys
lists=[*range(1,1001,1)]
print(lists)
#xrange is not availble in python3


# In[ ]:


#3. How Tuple is beneficial as compared to the list?
#Sol: Tuple is immutable when compared to lists, so can directly taken as keys for dict.

#4. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print
#the number which is divisible by 3 and is a multiple of 2.
lists=[*range(1,101,1)]
for i in lists:
    if i%2==0 and i%3==0:
        print(i)


# In[ ]:


#5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.
lists=[input("enter the string to be reversed:")]
print(lists[::-1])


# In[ ]:


#6. Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length.
lists="hello my name is jnan"
x=lists.split()
l=len(x)
for i in range(0,l):
    if len(x[i])%2==0:
        print(x[i])


# In[ ]:


"""
7. Write a program in python to print the pair of numbers whose sum is equal to the result
number that is let's say 8.
x=[1,2,3,4,5,6,7,8,9,-1]
"""
arr=[1,2,3,4,5,6,7,8,9,-1]
def getpairs(arr, n, target):
 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                print(arr[i],arr[j])
                
getpairs(arr,10,8)

             


# In[ ]:


"""
8. Write a program in Python to complete the following task:
Create two lists such as even_list and odd_list
Ask user to enter a number in the range of 1,50 and make sure if the entered number is
even, append it to the even_list and if the entered number is odd append it to the odd_list.
Keep that in mind you can only add 5 items in each list
Make sure once you enter all the 5 elements, calculate the sum of the list and return the
maximum of the list.

"""
evenlist=[]
oddlist=[]
    
for i in range(1,11):
    a=int(input("enter 10 numbers in range 1-50:"))
    if a%2==0:
        evenlist.append(a)
    if a%2!=0:
        oddlist.append(a)
print("evnlist:",evenlist,"sum:",sum(evenlist),"max value:",max(evenlist))
print("oddlist:",oddlist,"sum:",sum(oddlist),"max value:",max(oddlist))
    


# In[23]:


"""
9. Write a program to find out the occurrence of a specific character from an alphanumeric string.
Sample input: 12abcbacbaba344ab
Expected output: a=5 b=5 c=2
NOTE: Make sure to avoid counting the occurrence of numeric values in the string.
"""
import numpy as np
def Freq(str) :
     
    n = len(str)
     
    freq = np.zeros(26, dtype = np.int)
 
    for i in range(0, n) :
        freq[ord(str[i]) - ord('a')] += 1

    for i in range(0, n) :

        if (freq[ord(str[i])- ord('a')] != 0) :
             
            print (str[i], freq[ord(str[i]) - ord('a')],
                                                end = " ")

            freq[ord(str[i]) - ord('a')] = 0
         

str = "abcbacbabaab"
Freq(str)
    
    


# In[75]:


#10. Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10).
tp = (1,2,3,4,5,6,7,8,9,10)
lists = list()
for i in range(0,10):
    if tp[i]%2 == 0:
        lists.append(tp[i])

tp2 = tuple(lists)
print(tp2)




# In[ ]:





# In[ ]:





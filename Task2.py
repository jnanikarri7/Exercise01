#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
1. Write a program in Python to perform the following operation:
If a number is divisible by 3 it should print “Consultadd” as a string
If a number is divisible by 5 it should print “Python Training” as a string
If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
string.
"""
a=int(input("enter a number:"))
if a%3==0:
    print("Consultadd")
else:
    print("not div by 3")
if a%5==0:
    print("Python Training")
else:
    print("not div by 5")
if a%3==0 and a%5==0:
    print("Consultadd-Python Training")
else:
    print("not div by 3 and 5")


# In[ ]:


"""
2. Write a program in Python to perform the following operator based task:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.

"""
a=int(input("choose from option1-5:"))
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if a==1:
    result=num1+num2
    print(result)
if a==2:
    result=num1-num2
    print(result)
if a==3:
    result=num1/num2
    print(result)
if a==4:
    result=num1*num2
    print(result)
if a==5:
    b=int(input("enter first number for avg:"))
    c=int(input("enter second number for avg:"))
    result=(b+c)/2
    print(result)
if result<0:
    print("NEGATIVE")


# In[ ]:


#3. Write a program in Python to implement the given flowchart.

a=10
b=20
c=30
avg=(a+b+c)/3
print("average of no:",avg)
if avg>a and avg>b and avg>c:
    print("average is higher than a,b,c")
if avg>a and avg>b:
    print("average is higher than a,b")
if avg>a and avg>c:
    print("average is higher than a,c")
if avg>b and avg>c:
    print("average is higher than b,c")
if avg>a:
    print("average is higher than a")
if avg>b:
    print("average is higher than b")
if avg>c:
    print("average is higher than c")


# In[ ]:


"""
4. Write a program in Python to break and continue if the following cases occurs:
If user enters a negative number just break the loop and print “It’s Over”
If user enters a positive number just continue in the loop and print “Good Going”
"""   
a=int(input("enter positive number:"))

while a>0:
    if a>0:
        continue
        print("keep going")
while a<0:
    if a<0:
        break
print("its over")


# In[ ]:


#5. Write a program in Python which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200.

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
     print(i)


# In[ ]:


"""
6. What is the output of the following code examples?
x=123
i = 0
count = 0
 for i in x:
print(i)
sol: gives error since x=123; int object is not iterable
b. i = 0
while i < 5:
 print(i)
 i += 1
 if i == 3:
    break
 else:
    print("error")
sol:
0
error
1
error
2
c. count = 0
while True:
    
    print(count)
    count += 1
    if count >= 5:
     Break
sol: 0 1 2 3 4 
"""


# In[ ]:


#8. Write a program that accepts a string as an input from the user and calculate the number of digits
#and letters. 
a=str(input("enter the string to br counted:"))
numbers = sum(c.isdigit() for c in a)
letters = sum(c.isalpha() for c in a)
print("numbers",numbers)
print("letters",letters)


# In[ ]:


"""
9. Read the two parts of the question below: 
Write a program such that it asks users to “guess the lucky number”. If the correct number is
guessed the program stops, otherwise it continues forever.
Modify the program so that it asks users whether they want to guess again each time. Use two
variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
The program continues as long as a user has not answered “no” and has not guessed the correct
number)
"""
correct = 5
while 1>0:
 a=int(input("guess the lucky number:"))
 if a==5:
    break
 if a!=5:
    continue


# In[ ]:


correct = 5
answer=input("do you want to guess yes/no:")
if str(answer)== 'yes':
    count=1
else:
    count=0
while count>0:
 a=int(input("guess the lucky number:"))
 if a==5:
    break
 if a!=5:
    answer=input("do you want to guess yes/no:")
    if str(answer)== 'yes':
        count=1
    else:
        count=0
        break


# In[6]:


"""
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as
counter=1
While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.
"""
correct=5
count=1
while count<=5:
    a=int(input("start guessing the number, you have 5 choices:"))
    count+=1
    b=int(input("start guessing the number, you have 4 choices:"))
    count+=1
    c=int(input("start guessing the number, you have 3 choices:"))
    count+=1
    d=int(input("start guessing the number, you have 2 choices:"))
    count+=1
    e=int(input("start guessing the number, you have last choice:"))
    count+=1
    continue
while count>=5:
    if a==5 or b==5 or c==5 or d==5 or e==5:
        print("good guess")
        break
    else:
        print("game over")
        break
        


# In[18]:


"""
11. In the previous question, insert break after the “Good guess!” print statement. break will terminate
the while loop so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”.
"""
correct=5
count=1
while count<=5:
    a=int(input("start guessing the number, you have 5 choices:"))
    count+=1
    if a==5:
        print("good guess")
        break
    b=int(input("start guessing the number, you have 4 choices:"))
    count+=1
    if b==5:
        print("good guess")
        break
    c=int(input("start guessing the number, you have 3 choices:"))
    count+=1
    if c==5:
        print("good guess")
        break
    d=int(input("start guessing the number, you have 2 choices:"))
    count+=1
    if d==5:
        print("good guess")
        break
    e=int(input("start guessing the number, you have last choice:"))
    count+=1
    if e==5:
        print("good guess")
        break
else:
        print("Sorry but that was not very successful")
    


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1:- Input a string of odd length (minimum 9 characters), print a string made of the 3 middle characters from input string.(eg :- if input is abcdefghi, answer should be def)

str1=input("Please Enter your string: ")
if (len(str1)) % 2 ==0:
    print("condition violated")
elif int(len(str1)<9):
    print("condition violated")
else:
    length=int(len(str1)/2)
    str2=str1[length-1:length+2]
    print(str2)


# In[4]:


#2:- Calculate the sum and average of first n natural numbers
# a. using for loop


sum=0
n=int(input("Enter limit:"))
for i in range(0,n):
    sum=sum+i
    avg=sum/n
print("The sum of first {} numbers are {} and average is {}".format(n,sum,avg))
    


# In[18]:


#2:- Calculate the sum and average of first n natural numbers
# b. using while loop

sum=0
i=0
n=int(input("Please Enter The Limit : "))
while i<n:
    sum+=i
    avg=sum/n
    i+=1
print("The sum of first {} numbers are {} and average is {}".format(n,sum,avg))


# In[7]:


#3:- Accept list of 5 float numbers as input from user using loop and store values

list= []
print("Enter elements:")
for i in range(5):
    element=float(input())
    list.append(element)
print(list)


# In[8]:


#4:- Print the following pattern
#a) 

rows=5
for i in range(6):
    for j in range(i):
        print(j+1,end=' ')
    print("")


# In[9]:


#4:- Print the following pattern
#b) 

rows=5
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("")


# In[24]:


#5:- input a number, count and print the total number of digits in that number using while loop

length=0
num=int(input("Enter Number:"))
n=num
while num>0:
    length+=1
    num=num//10
print("The number of digits in {} are {}".format(n,length))


# In[16]:


#6:- Given two lists. Create a third list by picking an odd-index element from the first list and even index elements from second.
#listOne = [3, 6, 9, 12, 15, 18, 21]
#listTwo = [4, 8, 12, 16, 20, 24, 28]

listOne=[3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]

oddindex=listOne[1::2]
print("Odd index")
print(oddindex)
print("")

evenindex=listTwo[0::2]
print("Even index")
print(evenindex)
print("")

listThree=oddindex+evenindex
print("Third list :",listThree)


# In[14]:


#7:- program to get the smallest number from a list.

lst=[12,43,15,3,61]
k=lst[0]
for i in range(1,len(lst)):
    if lst[i]<k:
        k=lst[i]
print(k) 


# In[15]:


#8:- Reverse the following list using for loop and range [ do not use reverse or reversed like functions]
# list1 = [10, 20, 30, 4, 50]

list1=[10,20,30,4,50]
lst=[]
k=len(list1)
for i in range(k-1,-1,-1):
    lst.append(list1[i])
print(lst)


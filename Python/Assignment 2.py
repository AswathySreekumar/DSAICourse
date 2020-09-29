#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Q1: Modify the first item (22) of a list inside a following tuple to 222
#tuple1=(11,[22,33],44,55)
#expected output:
#tuple1=(11,[222,33],44,55)


tuple1=(11,[22,33],44,55)
lst1=list(tuple1)
lst1[1][0]=222
tuple(lst1)


# In[42]:


#Q2: Count the number of occurences of item 50 from a tuple
#tuple1=(50,10,60,70,50)

tuple1=(50,10,60,70,50)
count=0
l1=list(tuple1)
for i in l1:
    if i==50:
        count+=1
count


# In[40]:


# Q3: Write a Python program to convert a list to a tuple

lst1=[10,20,30,40,50,60]
tuple(lst1)


# In[27]:


#Q4: Returns a new set with all items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=set1.union(set2)
set3


# In[1]:


#Q5: Merge following two Python dictionaries into one
#dict1={'Ten':10,'Twenty':20,'Thirty':30}
#dict2={'Thirty':30,'Fourty':40,'Fifty':50}

def mergeDict(dict1,dict2):
    dict3={**dict1,**dict2}
    print(dict3)

dict1={'Ten':10,'Twenty':20,'Thirty':30}
dict2={'Thirty':30,'Fourty':40,'Fifty':50}
mergeDict(dict1,dict2)


# In[11]:


#Q6: Given a Python dictionary, Change Brad’s salary to 8500
#SampleDict={
 #   'emp1':{'name':'jhon','salary':7500},
  #  'emp2':{'name':'Emma','salary':8000},
   # 'emp3':{'name':'Brad','salary':6500}
    #       }

SampleDict={
    'emp1':{'name':'jhon','salary':7500},
    'emp2':{'name':'Emma','salary':8000},
    'emp3':{'name':'Brad','salary':6500}
           }

SampleDict['emp3']['salary']=8500
SampleDict


# In[37]:


#Q7: Rename key city to location in the following dictionary
#sampleDict={
#   "name":"Kelly",
#   "age":25,
#   "salary":8000,
#   "city":"New York"
#}

sampleDict={
   "name":"Kelly",
   "age":25,
   "salary":8000,
   "city":"New York"
}
oldkey='city'
newkey='location'
sampleDict[newkey]=sampleDict.pop(oldkey)
sampleDict


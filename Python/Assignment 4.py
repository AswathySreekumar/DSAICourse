#!/usr/bin/env python
# coding: utf-8

# #Q1 : create a txt file, enter multiple lines of text. read this file line by line and store it into a list. Apply exception handling technique

# In[3]:


get_ipython().run_cell_magic('writefile', 'readfl.txt', 'Line 1\nLine 2\nLine 3\nLine 4')


# In[5]:


op=open("readfl.txt")
op.seek(0)
lst=list(op.readlines())
print(lst)


# In[7]:


try:
    op1=open("readfl.txt")
    op1.write("Line5")
except Exception as err:
    print("Error:", err)


# #Q2: Write a Python program to write below list content to a file. Apply exception handling technique
# #color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# In[9]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
op1=open("colors.txt",'w')
for i in color:
    op1.write(i+"\n")
    
try:
    rd=open("colors.txt")
    lst1=rd.readlines()
    print(lst1[6])
except IndexError as error:
    print("index not found")


# #Q3 : create a txt file, enter multiple lines of text. remove newline characters from created file and print as a list. Apply exception handling techniques wherever possible

# In[11]:


try:
    v=open("file5.txt",'w+')
    v.write("Line 1\n")
    v.write("Line 2\n")
    v.write("Line 3\n")
    v.write("Line 4\n")
    v.write("Line 5\n")
    v.seek(0)
    lst=v.readlines()
    lst1=[]
    for i in lst:
        lst1.append(i.rstrip("\n"))
    print(lst1)
        
except:
    print("Error in Try")
    
else:
    print("Success")
    
finally:
    print("Successfully done the opertions")


# #Q4 : create a testfile1.txt file, enter multiple lines of text . Now copy contents of testfile1.txt to new file testfile22.txt. Apply exception handling techniques wherever possible

# In[13]:


try:
    op=open("testfile1.txt",'w+')
    op1=open("testfile22.txt",'w+')
    op.write("Line 1")
    op.write("Line 2")
    op.write("Line 3")
    op.write("Line 4")
    op.write("Line 5")
    op.seek(0)
    lst=op.readlines()    
    op1.write(str(lst))

    
except Exception as ex:
    print("Error in Try")
    
else:
    print("Done")
    
finally:
    print("Successfully copied the content")


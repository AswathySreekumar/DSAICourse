#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1: Write a function calculation() such that it can accept two variables as arguments and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

def calculation(var1,var2):
    add=var1+var2
    dif=var1-var2
    return(add,dif)

calculation(10,5)


# In[4]:


#Q2 : Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both,and if the salary is missing in function call it should show it as 9000

def showEmployee():
    empname=input("Employee Name:")
    sal=input("Salary:")
    print('Employee Name:',empname)
    if sal=="":
        print("Salary:9000")
    else:
        print("Salary:",sal)
        
showEmployee()


# In[5]:


#Q3 : Write a function called multipleLetterCount. This function takes in one parameter (a string) and returns a dictionary with the keys being the letters and the value being the count of the letter.
# Example output:
# multipleLetterCount('awesome')
# {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}

dict={}
def multipleLetterCount(str):
    for i in str:
        dict[i]=str.count(i)
    print(dict)
        
        
multipleLetterCount("awesome")  


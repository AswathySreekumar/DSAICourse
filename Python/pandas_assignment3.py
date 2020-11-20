#!/usr/bin/env python
# coding: utf-8

# In[71]:


import pandas as pd


# In[72]:


df01=pd.read_csv(r'https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df01


# In[73]:


#1. Get the Metadata from the above files.
df01.info()


# In[74]:


#2. Get the row names from the above files.
list(df01.index)


# In[81]:


#3. Change the column name from any of the above file and store the changes made permanently.
df01.rename(columns={'PUBLISH STATES':'Public states'},inplace=True)
df01


# In[82]:


#4. Change the names of multiple columns.
df02=df01.rename(columns={'WHO region':'WHO Region','Display Value':'Value'})
df02


# In[83]:


#5. Arrange values of a particular column in ascending order.
df01.sort_values('Year')


# In[84]:


#6. Arrange multiple column values in ascending order.
df01.sort_values(['Display Value','Numeric'],ascending=[True,True])


# In[85]:


#7. Make country as the first column of the dataframe.
df01.set_index('Country').head()


# In[86]:


#8. Get the column array using a variable
lst=df01.columns.values
lst


# In[87]:


#9. Get the subset rows 11, 24, 37
df01.iloc[[11,24,37]]


# In[88]:


#10. Get the subset rows excluding 5, 12, 23, and 56
df=df01.index.isin([5,12,23,56])
df04=df01[~df]
df04


# In[89]:


#11.find rows with NaN values
df01[pd.isnull(df01).any(axis=1)]


# In[90]:


#12. show rows from dataset 1 country = india with high income
df05=df01[df01['Country'].str.match('India')]
df06=df05[df05['World Bank income group'].str.match('High-income')]
df06


# In[ ]:





# In[91]:


df001=pd.read_csv(r'https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df001


# In[92]:


#1. Get the Metadata from the above files.
df001.info()


# In[93]:


#2. Get the row names from the above files.
list(df001.index)


# In[94]:


#3. Change the column name from any of the above file and store the changes made permanently.
df001.rename(columns={'STATION_NAME':'NAME_ST'},inplace=True)
df001


# In[95]:


#4. Change the names of multiple columns.
df002=df001.rename(columns={'TMAX':'T_MAX','TMIN':'T_MIN'})
df002


# In[96]:


#5. Arrange values of a particular column in ascending order.
df001.sort_values('DATE')


# In[97]:


#6. Arrange multiple column values in ascending order.
df001.sort_values(['TMAX','TMIN'])


# In[98]:


#8. Get the column array using a variable
lst1=df001.columns.values
lst1


# In[99]:


#9. Get the subset rows 11, 24, 37
df01.iloc[[11,24,37]]


# In[100]:


#10. Get the subset rows excluding 5, 12, 23, and 56
df0=df001.index.isin([5,12,23,56])
df004=df001[~df0]
df004


# In[101]:


#11.find rows with NaN values
df001[pd.isnull(df001).any(axis=1)]


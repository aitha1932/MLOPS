#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[3]:


db=pandas.read_csv('Salary_Data.csv')


# In[4]:


db


# In[6]:


db.info()


# In[7]:


x=db["YearsExperience"].values.reshape(30,1)


# In[8]:


x


# In[9]:


y=db["Salary"]


# In[10]:


y


# In[12]:


from sklearn.linear_model import LinearRegression


# In[13]:


model=LinearRegression()


# In[14]:


model.fit(x,y)


# In[15]:


model.coef_


# In[16]:


model.predict([[5.9]])


# In[20]:


model.predict([[9.6]])


# In[24]:


model.predict([[1.1]])


# In[25]:


#Accuracy
36187/39343*100

91% Accuracy
# In[26]:


#Y=C+WX
#C-INTERCEPT
model.intercept_


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv('F:/Python/Supermarket/supermarket.csv')


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.describe().round()


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df = df.drop(['Invoice ID', 'Date', 'Time'], axis = 1)


# In[10]:


df.head()


# In[11]:


df['gross margin percentage']


# In[12]:


df['gross margin percentage'].unique()


# In[13]:


df = df.drop(['gross margin percentage'], axis = 1)


# In[14]:


df.head()


# In[15]:


df['Gender'].value_counts()


# In[16]:


df.shape


# In[17]:


sns.countplot('Gender', data= df)


# In[18]:


gender_dummies = pd.get_dummies(df['Gender'])
gender_dummies.head()


# Joining original data frame (df) with gender dummies data frame (gender_dummies)

# In[19]:


df= pd.concat([df, gender_dummies], axis=1)


# In[20]:


df


# In[24]:


plt.figure(figsize =(12,8))


# In[27]:


plt.figure(figsize =(12,8))
sns.barplot(x = 'Product line', y = 'Female', data = df)


# In[26]:


plt.figure(figsize =(12,8))
sns.barplot(x = 'Product line', y = 'Male', data = df)


# Plotting Customers per city

# In[28]:


place_df = pd.DataFrame(df['City'].value_counts())


# In[29]:


place_df 


# In[30]:


sns.barplot(x= place_df.index, y=place_df['City'], palette = 'hot')


# In[31]:


payment_df = pd.DataFrame(df['Payment'].value_counts())
payment_df 


# In[32]:


sns.barplot(x =payment_df.index , y = payment_df.Payment)


# Getting Gross Income Plot for each product line

# In[33]:


plt.figure(figsize=(12,6))
sns.barplot(x=df['Product line'], y= df['gross income'])


# In[36]:


xdata = [0,1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,4))
sns.barplot(y = df['Product line'], x= df['Rating'])


# Total bill in each product line

# In[37]:


df.groupby('Product line')['Total'].sum()


# In[38]:


plt.figure(figsize = (12,6))
sns.barplot(x = df['Total'], y= df['Product line'])


# Exploring Quantity Column

# In[41]:


xdata = [1,2,3,4,5,6,7,8,9,10]
plt.figure(figsize = (12,6))
sns.distplot(df['Quantity'])


# In[44]:


quantity_df = pd.DataFrame(df['Quantity'].value_counts())


# In[45]:


quantity_df


# In[47]:


plt.figure(figsize = (12,6))
sns.barplot(x= quantity_df.index, y = quantity_df['Quantity'], palette = 'inferno')


# Plotting heatmap to check if any correlation between columns

# In[49]:


df.corr()


# In[50]:


sns.heatmap(df.corr())


# In[ ]:





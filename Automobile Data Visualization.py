#!/usr/bin/env python
# coding: utf-8

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


data=pd.read_csv('Automobile.csv')


# In[5]:


data.head()


# In[6]:


sns.distplot(data['city_mpg'])


# In[7]:


sns.displot(data['city_mpg'], kde = True, rug = True)


# In[8]:


sns.histplot(data['city_mpg'])


# In[9]:


sns.stripplot(data['city_mpg'])


# In[31]:


sns.set(color_codes= True)


# In[32]:


sns.jointplot(data['horsepower'], data['engine_size'])


# In[33]:


sns.jointplot(data['city_mpg'], data['horsepower'], kind = 'hex')


# In[34]:


sns.jointplot(data['city_mpg'], data['horsepower'], kind = 'scatter')
sns.jointplot(data['city_mpg'], data['horsepower'], kind = 'resid')


# In[35]:


sns.jointplot(data['city_mpg'], data['horsepower'], kind = 'reg')


# In[36]:


sns.jointplot(data['city_mpg'], data['horsepower'], kind = "kde")


# In[37]:


sns.pairplot(data[['city_mpg', 'horsepower', 'highway_mpg']])


# In[38]:


sns.jointplot(data['engine_size'], data['horsepower'])


# In[39]:


sns.pairplot(data[['city_mpg', 'horsepower', 'highway_mpg']], kind= "kde")


# In[40]:


sns.stripplot(data['fuel_type'], data['horsepower'], jitter = True)


# In[41]:


sns.swarmplot(data['fuel_type'], data['horsepower'])


# In[42]:


sns.boxplot(data['number_of_doors'], data['horsepower'], width = 0.5, whis = 1.5)


# In[43]:


sns.boxplot(data['number_of_doors'], data['horsepower'], hue=data['fuel_type'])


# In[44]:


sns.barplot(y =data['fuel_type'], x =data['horsepower'])


# In[45]:


sns.barplot(data['body_style'], data['horsepower'], hue= data['aspiration'])


# In[46]:


sns.barplot(data['body_style'], data['horsepower'], hue= data['engine_location'])


# In[47]:


sns.countplot(data['body_style'])


# In[48]:


sns.countplot(data['body_style'], hue= data['engine_location'])


# In[49]:


sns.pointplot(data['body_style'], data['engine_size'], hue=data["number_of_doors"], capsize = False)


# In[50]:


sns.factorplot(x = "fuel_type",
                y = "horsepower",
               hue = 'number_of_doors',
               col = 'engine_location',
                data = data,
                kind = "strip")


# In[51]:


sns.lmplot(x="horsepower", y="peak_rpm", data=data)


# In[52]:


sns.lmplot(x='horsepower', y='peak_rpm', data=data, hue='fuel_type')


# In[ ]:





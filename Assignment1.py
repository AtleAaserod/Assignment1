#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib as plt


# In[25]:


url = 'https://raw.githubusercontent.com/umaimehm/Intro_to_AI_2021/main/assignment1/Ruter_data.csv'


# In[33]:


df = pd.read_csv(url, sep=";")
df.head()


# In[60]:


df.info()

df["Passasjerer_Ombord"].plot.line()
df["Kjøretøy_Kapasitet"].plot.line()


# In[35]:


df.describe()


# In[69]:


df["Kommune"].value_counts().plot(kind='barh')


# In[55]:


df["Fylke"].value_counts().plot(kind='barh')


# In[70]:


df["Kjøretøy_Kapasitet"].value_counts().plot(kind='barh')


# In[71]:


df["Linjetype"].value_counts().plot(kind='barh')


# In[76]:


df["Passasjerer_Ombord"]=df["Passasjerer_Ombord"].clip(lower=0)
df["Passasjerer_Ombord"].value_counts()[:25].plot(kind='barh')


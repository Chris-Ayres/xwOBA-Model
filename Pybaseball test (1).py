#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pybaseball import statcast
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# In[2]:


stat_df = statcast(start_dt="2019-06-24", end_dt="2019-06-25")


# In[3]:


stat_df


# Using three years of data so that it is recent, but is still measured prior to the 2023 rule changes.

# In[4]:


three_year_data = statcast(start_dt="2020-07-23", end_dt="2022-11-05")


# Since I'm designing a process to find xwOBAcon, I'm only using balls in play.

# In[5]:


contact_data = three_year_data[three_year_data['description'] == 'hit_into_play']
contact_data


# Preliminary scatter plot of exit velocity and launch angle, colored by type of ball in play.

# In[6]:


contact_data = contact_data.dropna(subset = ['launch_angle', 'launch_speed'])


# In[8]:


fig, ax = plt.subplots()
plt.scatter(x = contact_data['launch_speed'], y = contact_data['launch_angle'],
           c = contact_data['woba_value'], cmap = 'coolwarm', s = 2)
ax.set_xlabel('Exit Velocity (mph)')


# In[9]:


from sklearn.metrics import confusion_matrix, f1_score, accuracy_score


# In[10]:


print(contact_data.columns)


# In[12]:


X = contact_data.iloc[:, 53:55]
Y = contact_data.iloc[:, 8]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 0, test_size = .2)


# In[18]:


classifier = KNeighborsClassifier(n_neighbors = 23, p = 2, metric = 'euclidean', )


# In[19]:


classifier.fit(X_train, Y_train)


# In[20]:


Y_pred = classifier.predict(X_test)


# In[21]:


cm = confusion_matrix(Y_test, Y_pred)
print(cm)


# In[22]:


print(accuracy_score(Y_test, Y_pred))


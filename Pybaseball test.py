#!/usr/bin/env python
# coding: utf-8

# In[39]:


from pybaseball import statcast
import matplotlib.pyplot as plt


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

# In[30]:


contact_data = contact_data.dropna(subset = ['launch_angle', 'launch_speed'])


# In[37]:


fig, ax = plt.subplots()
plt.scatter(x = contact_data['launch_speed'], y = contact_data['launch_angle'],
           c = contact_data['woba_value'], cmap = 'coolwarm', s = 2)
ax.set_xlabel('Exit Velocity (mph)')


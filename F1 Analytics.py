#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


results=pd.read_csv('C:\\Users\\bhuva\\OneDrive\\Desktop\\Python_P\\Datasets\\F1 Analytics\\results.csv')


# In[4]:


races=pd.read_csv('C:\\Users\\bhuva\\OneDrive\\Desktop\\Python_P\\Datasets\\F1 Analytics\\races.csv')
drivers=pd.read_csv('C:\\Users\\bhuva\\OneDrive\\Desktop\\Python_P\\Datasets\\F1 Analytics\\drivers.csv')
constructors=pd.read_csv('C:\\Users\\bhuva\\OneDrive\\Desktop\\Python_P\\Datasets\\F1 Analytics\\constructors.csv')


# In[5]:


df=pd.merge(results,races[['raceId','year','name','round']],on='raceId',how='left')


# In[6]:


df=pd.merge(df,drivers[['driverId','driverRef','nationality']],on='driverId',how='left')
df=pd.merge(df,constructors[['constructorId','constructorRef','name','nationality']],on='constructorId',how='left')


# In[7]:


df


# In[8]:


df.drop(['number','position','positionText','laps','fastestLap','statusId','resultId','raceId','driverId','constructorId'],axis=1,inplace=True)


# In[9]:


df.rename(columns={'rank':'fastestLapRank','name_x':'gpName','nationality_x':'driverNationality','name_y':'constructorName','nationality_y':'constructorNationality','driverRef':'driver'},inplace=True)


# In[10]:


df


# In[11]:


df=df[['year','gpName','round','driver','constructorName','grid','positionOrder','points','time','milliseconds','fastestLapRank','fastestLapTime','fastestLapSpeed','driverNationality','constructorNationality']]


# In[12]:


df


# In[13]:


df=df[df['year']!=2019]


# In[14]:


df


# In[15]:


df=df.sort_values(by=['year','round','positionOrder'],ascending=[False,True,True])


# In[16]:


df


# In[17]:


df.time.replace('\\N',np.nan,inplace=True)


# In[18]:


df


# In[19]:


df.milliseconds.replace('\\N',np.nan,inplace=True)
df.fastestLapRank.replace('\\N',np.nan,inplace=True)
df.fastestLapTime.replace('\\N',np.nan,inplace=True)
df.fastestLapSpeed.replace('\\N',np.nan,inplace=True)


# In[20]:


df


# In[21]:


df.milliseconds=df.milliseconds.astype(float)


# In[22]:


df.fastestLapRank=df.fastestLapRank.astype(float)
df.fastestLapSpeed=df.fastestLapSpeed.astype(float)


# In[23]:


df


# In[24]:


df.reset_index(drop=True,inplace=True)


# In[25]:


df


# In[26]:


print(df.shape)


# In[27]:


df.info()


# In[28]:


df.head(20)


# In[29]:


sb.set_palette('Set3')
plt.rcParams['figure.figsize']=10,6


# In[30]:


driverWinner=df.loc[df['positionOrder']==1].groupby('driver')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()


# In[31]:


driverWinner


# In[32]:


sb.barplot(data=driverWinner,y='driver',x='positionOrder',color='red',alpha=0.9)
plt.title('Most Grand Prix Wins')
plt.xlabel('Number of wins')
plt.ylabel('Driver')
plt.yticks([])


# In[33]:


top10Drivers=driverWinner.head(10)
print(top10Drivers)


# In[34]:


sb.barplot(data=top10Drivers,y='driver',x='positionOrder',color='green',alpha=0.9,linewidth=0.9,edgecolor='black')
plt.title('Most GP Wins')
plt.ylabel('Driver')
plt.xlabel('Number of wins')


# In[ ]:





# In[ ]:





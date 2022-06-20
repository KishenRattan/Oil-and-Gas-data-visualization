#!/usr/bin/env python
# coding: utf-8

# # Data Visualisation on Oil Well data

# In[1]:


# Data analysis on production wells to identify if the wells are productive


# In[2]:


# Libraries wich are used:


# In[3]:


pip install plotpy


# In[4]:


pip install openpyxl


# In[5]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np


# ## 1. Data collection
# ### Source of data is: www.equinor.com. The data has been made publicly available by Equinor

# In[6]:


df = pd.read_excel('./Volve production data.xlsx')


# In[7]:


import pandas as pd


# In[8]:


df.head()


# In[9]:


df.info()


# In[37]:


#Detecting outliers using Boxplot (for Bore Oil Vol)

import seaborn as sns
sns.boxplot(df['BORE_OIL_VOL'])


# In[38]:


# Position of the Outlier
print(np.where(df['BORE_OIL_VOL']>3000))


# In[44]:


# Detecting outliers using Scatterplot (for Bore Gas Vol in relation with Average Choke Size ) 
# Scatter plot
fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(df['BORE_GAS_VOL'], df['AVG_CHOKE_SIZE_P'])
 
# x-axis label
ax.set_xlabel('(====================)')
 
# y-axis label
ax.set_ylabel('(\\\\\\\\\\\\\\\\\\\\)')
plt.show()


# ## Overview of all null values(red) in heatmap.

# In[10]:


A= sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='turbo')
plt.xticks(rotation = 90, ha = 'right')


# In[11]:


import seaborn as sns


# In[12]:


from matplotlib import pyplot as plt


# In[13]:


df. isnull(). sum()


# # 2. Data processing

# ### Which types of wells are available in dataset

# In[14]:


df['WELL_TYPE'].unique()


# ##### There are 2 types of wells: WI and OP.^^^

# ## Filter data for producer type of wells

# In[15]:


##Filter and keep only the data for producer type wells
df_filtered =df[df['WELL_TYPE']=='OP']


# In[16]:


## Dropping the not usefull columns
df_filtered.drop(labels=['WELL_BORE_CODE',
                         'NPD_WELL_BORE_NAME',
                         'NPD_FIELD_CODE',
                         'NPD_FIELD_NAME',
                         'NPD_FACILITY_CODE',
                         'NPD_FACILITY_NAME',
                        'AVG_CHOKE_UOM',
                        'FLOW_KIND',
                        'WELL_TYPE'], axis=1)


# # 3. Data Analyzing

# In[17]:


# Create again heatmap to visualize processed data
sns.heatmap(df_filtered.isnull(),yticklabels=False,cbar=False,cmap='inferno')
plt.xticks(rotation = 90, ha = 'right')


# In[18]:


# In the heatmap above the colum "BORE_WI_VOL" is fully signifying null value because we filtered only the producing wells.


# In[19]:


# Below we see the data which are available for each well by code
# For each well code there are x values
df['NPD_WELL_BORE_CODE'].value_counts()


# In[20]:


# Below we see the oil production from all the wells (NPD_WELL_BORE_CODE) 
# in relation with BORE_OIL_VOL!
# ECDF Plot.
sns.ecdfplot(x='BORE_OIL_VOL',data=df_filtered, hue='NPD_WELL_BORE_CODE',palette=['r', 'g', 'b', 'y', 'brown', 'magenta'])
plt.show()


# #### In the ECDF plot above we can see that from: well 7405 40% data is zero Bore_OIL_VOL, well 7289 20% data is zero Bore_OIL_VOL and from well 5769 18% data is zero Bore_OIL_VOL. 

# In[21]:


pip install plotly==5.8.2


# In[ ]:





# In[22]:


# Let see the result in a scatterplot
df["NPD_WELL_BORE_CODE"] = df["NPD_WELL_BORE_CODE"].astype(str)
fig = px.scatter(df, x="DATEPRD", y="BORE_OIL_VOL",
                 color="NPD_WELL_BORE_CODE",
                 hover_name="NPD_WELL_BORE_CODE")
fig.show()


# In[23]:


fig = px.line(df_filtered, x="DATEPRD", y="BORE_OIL_VOL", color='NPD_WELL_BORE_CODE')
fig.show()


# In[24]:


#The above interactive line plot of Oil production data , shows that the most significant production is coming from the two wells namely #5599 and #5351

#Also in the above date wise production plot we clearly see that the well production value intermittently comes to zero value, which shows us that the well were regularly shut in. The same conclusion can also be verified from the on stream hours data available in the dataset.

#The above plot shows a declining oil production value for all the significantly producing wells and for the insignificant wells , the production volume was very much insignificant and at the same time their water production volume increased making them not viable economically. The water volume can be seen in the plot below


# In[25]:


fig = px.line(df_filtered, x="DATEPRD", y="BORE_WAT_VOL", color='NPD_WELL_BORE_CODE')
fig.show()


# In[26]:


fig = px.line(df_filtered, x="DATEPRD", y="BORE_GAS_VOL", color='NPD_WELL_BORE_CODE')
fig.show()


# In[27]:


sns.heatmap(df_filtered.corr(),square=True,cmap='RdYlGn')


# In[28]:





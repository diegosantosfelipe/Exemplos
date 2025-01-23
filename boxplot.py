#!/usr/bin/env python
# coding: utf-8

# In[53]:


#!/usr/bin/env python
# coding: utf-8

"""
    Description:
    Gera o boxplot de dados de precipitação mensal para o ano.

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[76]:


#Lê os dados e separa por mês

df_p1 = pd.read_csv('output_periodo1.csv', sep=";")
df_p2 = pd.read_csv('output_periodo2.csv', sep=";")

dfmes_p1_r1 = []
dfmes_p1_r2 = []
dfmes_p2_r1 = []
dfmes_p2_r2 = []
for i in range(12):
    dfmes_p1_r1.append(df_p1['precip_med_box_1'][df['mes'] == df['mes'][i]].values)
    dfmes_p1_r2.append(df_p1['precip_med_box_2'][df['mes'] == df['mes'][i]].values)
    dfmes_p2_r1.append(df_p2['precip_med_box_1'][df['mes'] == df['mes'][i]].values)
    dfmes_p2_r2.append(df_p2['precip_med_box_2'][df['mes'] == df['mes'][i]].values)
    
precip_11 = [dfmes_p1_r1[i] for i in range(12)]
precip_12 = [dfmes_p1_r2[i] for i in range(12)]
precip_21 = [dfmes_p2_r1[i] for i in range(12)]
precip_22 = [dfmes_p2_r2[i] for i in range(12)]


# In[77]:


#Plota o boxplot

#np.random.seed(19680801)

#fig, ax = plt.subplots()
#ax.set_title('Boxplot de precipitação mensal (2011-2023): Região 2')
#ax.set_ylabel('Precipitação mensal (mm)')
#ax.set_xlabel('Meses')

#bplot = ax.boxplot(precip_22, patch_artist=True)

#plt.show()


# In[78]:


#Plota o boxplot

np.random.seed(19680801)

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 10), sharey=True)

axs[0, 0].boxplot(precip_11)
axs[0, 0].set_title('Boxplot de precipitação mensal (1981-2010): Região 1')
axs[0, 0].set_ylabel('Precipitação mensal (mm)')
axs[0, 0].set_xlabel('Meses')

axs[0, 1].boxplot(precip_12)
axs[0, 1].set_title('Boxplot de precipitação mensal (1981-2010): Região 2')
axs[0, 1].set_ylabel('Precipitação mensal (mm)')
axs[0, 1].set_xlabel('Meses')

axs[1, 0].boxplot(precip_21)
axs[1, 0].set_title('Boxplot de precipitação mensal (2011-2023): Região 1')
axs[1, 0].set_ylabel('Precipitação mensal (mm)')
axs[1, 0].set_xlabel('Meses')

axs[1, 1].boxplot(precip_22)
axs[1, 1].set_title('Boxplot de precipitação mensal (2011-2023): Região 2')
axs[1, 1].set_ylabel('Precipitação mensal (mm)')
axs[1, 1].set_xlabel('Meses')


#fig.subplots_adjust(hspace=0.4)
plt.show()


# In[ ]:





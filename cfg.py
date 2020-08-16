#!/usr/bin/env python
# coding: utf-8

# In[61]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain 


# In[52]:


dic = {   '01/02/2020': [['a',1,0,1,0,0],['b',0,1,1,0,0],['c',1,1,1,0,1],['d',1,0,1,0,0],['e',0,1,0,1,0]],
          '10/03/2020': [['a',1,1,1,0,1],['b',0,1,0,0,0],['c',0,1,1,1,0],['d',1,0,0,1,0],['e',1,1,0,0,0]],
           '21/04/2020': [['a',0,0,1,0,1],['b',1,0,1,1,0],['c',0,1,0,1,1],['d',1,0,0,1,1],['e',0,1,1,1,1]],
           '15/05/2020': [['a',1,0,1,1,0],['b',0,1,1,0,0],['c',1,0,1,0,1],['d',1,1,1,0,1],['e',0,0,1,0,0]]
      }
dic


# In[86]:


tot = []
fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')
ctr = 0
# fig = plt.figure()
p = [(0,0),(0,1),(1,0),(1,1)]
for items in dic.items():
    if ctr>3:
        break
    (i,j) = p[ctr]
    ctr = ctr+1
    
    (date,l) = items
    df = pd.DataFrame(l)
    df = df.rename(columns={0: "name"})
    name = 'a'
    select_student = df.loc[df['name'] == name]
    select_student = select_student.loc[:, df.columns != 'name']
    print(list(select_student.iloc[0]))
    tot.append(list(select_student.iloc[0]))
    ax[i][j].bar(select_student.columns,list(select_student.iloc[0]),label = 'Yes',color = 'c')
    ax[i][j].set_title(date)

    
# tot = np.array(tot)
# tot = tot.flatten()
# print(tot)

# plt.bar(x,tot,label = 'Yes',color = 'c')
# # plt.bar(x2,tot,label = 'Yes',color = 'b')
# plt.xlabel('Questions')
# plt.ylabel('Answers')
# plt.title('Student Analysis')
# plt.legend()
# plt.show()


# In[50]:


for items in dic.items():
    (date,l) = items
    df = pd.DataFrame(l)
    df = df.rename(columns={0: "name"})
    select_student = df.loc[:, df.columns != 'name']
    add = df.loc[:, df.columns != 'name'].sum(axis=0)
    y = list(add)
    print(y)
    plt.bar(select_student.columns,y,label = 'Yes',color = 'c') # r color is Red
    plt.xlabel('Questions')
    plt.ylabel('Answers')
    plt.title('Student Analysis')
    plt.legend()
    plt.show()


# In[13]:


# lnp = np.array(l)
df = pd.DataFrame(l)
df = df.rename(columns={0: "name"})
df


# In[36]:


#for a particular student
name = 'a'
select_student = df.loc[df['name'] == name]
select_student = select_student.loc[:, df.columns != 'name']
print(select_student)
plt.bar(select_student.columns,select_student.iloc[0],label = 'Yes',color = 'r') # r color is Red
plt.xlabel('Questions')
plt.ylabel('Answers')
plt.title('Student Analysis')
plt.legend()
plt.show()


# In[44]:


#for all students
add = df.loc[:, df.columns != 'name'].sum(axis=0)
y = list(add)
print(y)

plt.bar(select_student.columns,y,label = 'Yes',color = 'r') # r color is Red
plt.xlabel('Questions')
plt.ylabel('Answers')
plt.title('Student Analysis')
plt.legend()
plt.show()


# In[ ]:





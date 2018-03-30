
# coding: utf-8

# In[3]:


# Assignment 3 - Part 1
# You have been given a barGraph.csv file. 
# Using the data of this file you have to draw a bar graph showing all 8 emotions corresponding to each business.

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('barGraph.csv')
opacity = .4
bwidth = .15
xlabels = data['Business'].values
i = 1
for l in xlabels:
    vals = data[data['Business'] == l].values
    yvals = vals[0][1:]
    index = np.arange(len(yvals))
    plt.bar(index + (i * bwidth), yvals, bwidth, alpha=opacity, label=l)
    i = i + 1

plt.xlabel('Emoticon')
plt.ylabel('Emotion Level')
plt.title('Business Emoticons')
plt.xticks(index + bwidth + .55, data.columns.values[1:])
plt.legend()
plt.tight_layout()
plt.rcParams["figure.figsize"] = [10, 20]
plt.show()


# In[2]:


data


# In[17]:


# Assignment 3 - Part 2
# Using the data present in barGraph.csv file generate pie-chart showing percentage of emotions 
# for each business.

labels = data['Business'].values
emoticons = data.columns.values[1:]
# print(labels, emoticons)

for e in emoticons[:1]:
    vals = data[e].values
    print(e, vals, vals.sum())
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# # Plot
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
 
# plt.axis('equal')
# plt.show()


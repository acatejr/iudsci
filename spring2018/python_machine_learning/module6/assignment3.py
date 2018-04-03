
# coding: utf-8

# In[66]:


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
plt.clf()
plt.cla()
plt.close()


# In[67]:


data


# In[68]:


# Assignment 3 - Part 2
# Using the data present in barGraph.csv file generate pie-chart showing percentage of emotions 
# for each business.

labels = data['Business'].values
emoticons = data.columns.values[1:]

for e in emoticons:
    vals = data[e].values
    if vals.sum() > 0:
        sizes = vals / vals.sum() * 100
        plt.figure()
        plt.title(e)
        plt.pie(sizes, labels = labels)
        plt.axis('equal')

plt.clf()
plt.cla()
plt.close()       


# In[69]:


# Assignment 3 - Part 3. Generate a word cloud of your favorite news article or story or anything. 
# This word cloud should contain words having 4 letters or more.
from wordcloud import WordCloud

text = open('words.txt').read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis("off")
# Code borrowed from course module instructions
wordcloud = WordCloud(background_color="white", max_words=2000,max_font_size=40, relative_scaling=.4).generate(text)
plt.figure()
plt.imshow(wordcloud)
# plt.axis("off")
plt.show()
plt.clf()
plt.cla()
plt.close()


# In[70]:


"""
Assignment 3 - Part 4
You have been given a file ReviewID.txt. It has 10646 records in it, each record is made up of two fields
separated by a colon: like AzSn8aTOyVTUePaIQtTUYA:es . The first field is review ID and the second field
is language in which reviews has been written. Read this file and create a bar graph showing the percentage
of the reviews written in a particular language. The aim of this problem is to generate a graph using which
we can do a comparative analysis of the languages used for writing reviews.
"""
review_data = pd.read_csv('ReviewID.txt', delimiter=':', header=None, names=['id', 'lang'])
review_data.head(10)

# Group by language
grouped_reviews = review_data.groupby(['lang']).count()
grouped_reviews.plot.bar()
plt.show()


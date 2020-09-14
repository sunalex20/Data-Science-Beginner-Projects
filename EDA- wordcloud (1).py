#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

data = pd.read_pickle('dtm.pkl')
data = data.transpose()
data.head()


# In[14]:


top_dict = {}
for c in data.columns:
    top = data[c].sort_values(ascending=False).head(3)
    top_dict[c]= list(zip(top.index, top.values))

top_dict


# In[15]:


from wordcloud import WordCloud

wc = WordCloud(background_color="white", colormap="Dark2",
               max_font_size=150, random_state=42)


# In[25]:


# Reset the output dimensions
import matplotlib.pyplot as plt
data_clean = pd.read_pickle('data_clean.pkl')

plt.rcParams['figure.figsize'] = [16, 6]

# Create subplots for each comedian
for index, text in enumerate(data.columns):
    wc.generate(data_clean.Text[text])
    
    plt.subplot(4, 5, index+1)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")

plt.show()


# In[ ]:





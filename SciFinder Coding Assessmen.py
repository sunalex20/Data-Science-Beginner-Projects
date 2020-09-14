#!/usr/bin/env python
# coding: utf-8

# In[113]:


import requests
from bs4 import BeautifulSoup
import pickle

def getUrlFromMain(url):
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    # grab article urls
    ArticleURLs = [a['href'] for a in soup.find(id='main-content').find_all('a', href = True)]
    
    for url in ArticleURLs[0::2]:
        URLs.append('https://www.nfl.com' + url);
    
    return URLs
#     print(URLs)
   
    
def scrapeTitle(url):
    page = requests.get(url).text
    soup2 = BeautifulSoup(page, 'lxml')
    
    #grab titles --works
    ArticleTitles = [h1.text for h1 in soup2.find(class_='d3-l-col__col-8 nfl-c-article__header').find_all('h1')]
    
    for title in ArticleTitles:
        titles.append(title);
        
#     print(titles)
    return titles
    

def scrapeDate(url):
    page = requests.get(url).text
    soup4 = BeautifulSoup(page, 'lxml')
    
    #scrape the date, add it to dates array 
    date = [span.text for span in soup4.find(class_='nfl-c-article__dates').find_all('span')]
    dates.append(date)
    
    
    
def scrapeText(link):
    page = requests.get(url).text
    soup3 = BeautifulSoup(page, 'lxml')
    
    #scrape text add it to texts array 
    textBlocks = [p.text for p in soup3.find(class_='nfl-c-article__container').find_all('p')]
    allText = ''
    
    for textBlock in textBlocks:
        allText = allText + textBlock + '\n' + '\n'
    
    texts.append(allText)
    


# In[126]:



#initializing variables, pass in the nfl all news url to get updated news organization
NFL = 'https://www.nfl.com/news/all-news'
URLs = []
titles = []
dates = []
texts = []

getUrlFromMain(NFL) #grabs urls of all the news articles displayed on news section


for url in URLs: #goes to each article webpage and scrapes title, text, and date
    scrapeText(url)
    scrapeTitle(url)
    scrapeDate(url)

#commands for checking lengths of arrays
    # for title, text in zip(titles, texts):
    #     print(title, "...", text)
    # print(zip(titles, texts))
    # print(len(URLs))
    # print(len(titles))
    # print(len(texts))
    # print(len(dates))

    
#some old cleaning trials,decided to use Alice Zhao's cleaning functions instead 
    # #cleaning titles 
    # cleanTitles = [title.replace('\n', '') for title in titles]
    # cleanTitles = [title.lstrip() for title in cleanTitles]
    # cleanTitles = [title.rstrip() for title in cleanTitles]

    # #cleaning Text
    # cleanTexts = [text.replace('\n', '') for text in texts]
    # cleanTexts = [text.lstrip() for text in cleanTexts]
    # cleanTexts = [text.rstrip() for text in cleanTexts]

    
#zipping data title:text format, print after------this was for checking if indices matched up
    #     titleText = zip(cleanTitles, texts)
    #     print(titleText) 

#zipping data together into url: title, text dictionary, print after
    #     data = dict(zip(URLs, titleText)) 
    #     print(data) 


#pickling data to storage in serialized format, preserves source data//////////////////!!!!!!!!!!!
for i, c in enumerate(cleanTitles):
    with open("articles2/" + c + ".txt", "wb") as file:
        pickle.dump(cleanTexts[i], file)


data = {}
for i, c in enumerate(cleanTitles):
    with open("articles2/" + c + ".txt", "rb") as file:
        data[c] = pickle.load(file)

#check if keys and values are what we want
data.keys()
next(iter(data.keys()))


# In[127]:


def combine_text(list_of_text):
    '''Takes a list of text and combines them into one large chunk of text.'''
    combined_text = ''.join(list_of_text)
    return combined_text

data_combined = {key: [combine_text(value)] for (key, value) in data.items()}
data_combined


# In[128]:


#convert to dataFrame
import pandas as pd


data_df = pd.DataFrame.from_dict(data_combined).transpose()
data_df.columns = ['Text']
data_df = data_df.sort_index()
data_df.shape


# In[129]:


import re
import string

#apply cleaning functions- copied this text from online as I had previously implemented cleaning specific to my texts, but chose to apply more
def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

round1 = lambda x: clean_text_round1(x)

#apply round 1 cleaning
data_clean = pd.DataFrame(data_df.Text.apply(round1))
data_clean


#specify second round of cleaning
def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

#apply round 2 
round2 = lambda x: clean_text_round2(x)

data_clean = pd.DataFrame(data_clean.Text.apply(round2))
data_clean


# In[131]:


dates = dates[0:-2] #for some reason, we occlude a few items, bringing total rows down to 22 so adjust dates
data_df['dates'] = dates
data_df


# In[132]:


data_df.to_pickle("corpus.pk1")


# In[135]:


from sklearn.feature_extraction.text import CountVectorizer #count vectorizing to allow for NLP

cv = CountVectorizer(stop_words='english')
data_cv = cv.fit_transform(data_clean.Text)
data_dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
data_dtm.index = data_clean.index
data_dtm

#pickle this new Document Term Matrix for later use
data_dtm.to_pickle("dtm.pkl")


# In[136]:


# Let's also pickle the cleaned data (before we put it in document-term matrix format) and the CountVectorizer object
data_clean.to_pickle('data_clean.pkl')
pickle.dump(cv, open("cv.pkl", "wb"))


# In[137]:


dates


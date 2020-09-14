# Data-Science-Beginner-Projects

# About the code

Some of the code in this project was borrowed from Alice Wong from the PyOhio demo @ https://www.youtube.com/watch?v=xvqsFTUsOmc&t=4763s, these include package methods such as those used with pickle, wordcloud, and sentiment analysis. 

I attempt to webscrape the NFL official news websites, searching through their news page to find url links to their articles. From these links, I then scrape each article page for the article title, date, and text. 

I then clean through this data by placing it in a dataframe and applying cleaning functions to prepare the text for NLP and sentiment analysis. I use wordcloud and follow Alice Wong's sentiment analysis frameworks to generate two visuals: one wordcloud of the top words in each article as a quick visual cue of streaming NFL events (such as injuries, names, quick facts), and the other a sentiment analysis with emotionality and subjectivity to gauge whether articles are biased and if which emotional valence they contain. 

## Motivations
* Give fantasy football players up-to-date rss streaming with additional useful features from official nfl website
  * Rather than scrolling through each article and reading them, users can quickly identify important information and assess its    usefulness, trustworthiness, and other valences 
* Generate an organized data format for news article data that can be manipulated to analyze for useful features

I chose this project to target Fantasy Football players and demonstrate the applliability of data science to diverse mediums. My code generates two useful features, a hot-text representation of article info and a sentiment analysis on that article. Thus players are aware of the important keywords and whether they should pay attention to them based on their subjectivity and emotionality score.

## Future Steps
A next step could be to evaluate articles for names, and emotionality, and streaming that data to help Fantasy football players decide how to adjust their lineups based off negative news and keywords such as names, injuries, duration of injury, expected return dates, etc. 



## Setup
Here are the steps you’ll need to take before the start of the tutorial:

### 1. Download Anaconda
I highly recommend that you download [the Python 3.7 version](https://www.anaconda.com/download/).

### 2. Download the Jupyter Notebooks
Clone or download this [Github repository](https://github.com/adashofdata/nlp-in-python-tutorial), so you have access to all the Jupyter Notebooks (.ipynb extension) in the tutorial. **Note the green button on the right side of the screen that says `Clone or download`.** If you know how to use Github, go ahead and clone the repo. If you don't know how to use Github, you can also just download the zip file and unzip it on your laptop.

### 3. Launch Anaconda and Open a Jupyter Notebook

*Windows:*
Open the Anaconda Navigator program. You should see the Jupyter Notebook logo. Below the logo, click Launch. A browser window should open up. In the browser window, navigate to the location of the saved Jupyter Notebook files and open 0-Hello-World.ipynb. Follow the instructions in the notebook.

*Mac/Linux:*
Open a terminal. Type ```jupyter notebook```. A browser should open up. In the browser window, navigate to the location of the saved Jupyter Notebook files and open 0-Hello-World.ipynb. Follow the instructions in the notebook.

### 4. Install a Few Additional Packages

There are a few additional packages we'll be using during the tutorial that are not included when you download Anaconda - wordcloud, textblob and gensim.

*Windows:*
Open the Anaconda Prompt program. You should see a black window pop up. Type `conda install -c conda-forge wordcloud` to download wordcloud. You will be asked whether you want to proceed or not. Type `y` for yes. Once that is done, type `conda install -c conda-forge textblob` to download textblob and `y` to proceed, and type `conda install -c conda-forge gensim` to download gensim and `y` to proceed.

*Mac/Linux:*
Your terminal should already be open. Type command-t to open a new tab. Type `conda install -c conda-forge wordcloud` to download wordcloud. You will be asked whether you want to proceed or not. Type `y` for yes. Once that is done, type `conda install -c conda-forge textblob` to download textblob and `y` to proceed, and type `conda install -c conda-forge gensim` to download gensim and `y` to proceed.

**above setup instructions credit belongs to Alice Wong @ https://github.com/adashofdata/nlp-in-python-tutorial

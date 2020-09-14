# Data-Science-Beginner-Projects
My first showcase repository- these are some of the first projects I've created!

###about the code
################################################################################
The code in this project was borrowed from Alice Wong from the PyOhio demo @ https://www.youtube.com/watch?v=xvqsFTUsOmc&t=4763s
This is my first time attempting a data science project, thus a lot of these steps were new to me, such as SciKitLearn, and wordcloud, etc. 

I attempt to webscrape the NFL offocial news websites, searching through their news page to find url links to their articles. From these links, I then scrape each article page for the article title, date, and text. 

I then clean through this data by placing it in a dataframe and applying cleaning functions to prepare the text for NLP and sentiment analysis. I use wordcloud and follow Alice Wong's sentiment analysis frameworks to generate two visuals: one wordcloud of the top words in each article as a quick visual cue of streaming NFL events (such as injuries, names, quick facts), and the other a sentiment analysis with emotionality and subjectivity to gauge whether articles are biased and if which emotional valence they contain. 


###project goals and motivating factors
################################################################################
I chose this project to give Fantasy Football players two useful features, a hot-text representation of article info and a sentiment analysis as secondary information on that article. Thus players are aware of the important keywords and whether they should pay attention to them. 

A next step could be to evaluate articles for names, and emotionality, and streaming that data to help Fantasy football players decide how to adjust their lineups based off negative news and keywords such as names, injuries, duration of injury, expected return dates, etc. 

All code was written and compiiled in Jupyter notebook

#!/usr/bin/env python
# coding: utf-8

# # ISTA 322 Homework 1
# 
# Welcome to your first homework!  This one is focused on just practicing some of the exercises covered in the last coding lesson.  There are also some more open-ended questions with elements that I didn't demonstrate in that lesson... they're structurally similar, but you might need to google a thing or two to figure out the correction function.  
# 
# You need to add your own code blocks to answer any of the coding questions.  Also, at the end of some sections I have a 'questions' section.  Add a text cell right below and enter your answers. 

# #Submission Instruction
# 
# 1) First create a copy of this notebook in your drive and rename it to "ISTA_322_F22_HW1_yourname". 
# 
# 2) When you are ready to submit. Prepare three files: the python file (File->Download->Download .py), the notebook file (File->Download->Download .ipynb), and **PDF** version of your notebook (**after running all cells**). 
# 
# 3) Create the directory with your name put all three files in it, ZIP, and submit in D2L. 
# 

# ## Loading and Importing
# 
# First thing you need to do is load up your packages and then bring in the data.  
# 
# This dataset contains daily values for Amazon's stock.  This includes opening, closing, high price, low price, and also the amount of stock traded. 

# In[797]:


import pandas as pd
# also import matplotlib.pyplot and numpy with the proper aliases
import numpy as np
import matplotlib.pyplot as plt


# In[798]:


# Bring in your data. You just need to run this cell.
price = pd.read_csv("https://docs.google.com/spreadsheets/d/1lCkFZhz-NGTuE1ZilzJA_ZYBZsbCSDpS2MllyGZWjX4/gviz/tq?tqx=out:csv")


# ## Exploring the whole dataset
# 
# Now make some code cells to explore the whole dataset.  I want you to do the following:
# 
# - Get the number of rows and columns
# - Get the datatypes of each column
# - Look at the first five rows
# - Look at the last five rows
# - Look at summary statistics

# In[799]:


# Get the number of rows and columns
price.shape


# There are 5852 rows and 7 columns in the price dataset.

# In[800]:


# Get the datatypes of each column
price.dtypes


# In[801]:


# Look at the first 5 rows
price.head(5)


# ### Questions
# Write down Pandas instruction to answer these queries.
# - How many rows are in this dataset?
# - Do any datatypes need to be converted?
# - What was the mean and all time high opening stock price?

# In[802]:


# Look at the last 5 rows
price.tail(5)


# In[803]:


# Look at the summary statistics
price.describe()


# Q1: [2 points] How many rows are in this dataset?
# 
# There are 5852 rows in the dataset.
# 

# In[804]:


# Do not change the function name
def price_number_of_row():
    cnt = price.count()
    return cnt ## replace this line with return of the correct statement


# As an example, I will provide the answer to this question:

# In[805]:


def price_number_of_row_key():
  return price.count();


# This is how I will check your code:

# In[806]:


score = {}


# In[807]:


if np.all(price_number_of_row() == price_number_of_row_key()):
  score['q1'] = 2;
else:
  score['q1'] = 0;


# In[808]:


score


# Question 2: [2 points] Convert the datatype of 'Date' to an appropriate type 

# In[809]:


def convert_date_type():
    price['Date'] = pd.to_datetime(price['Date'])


# I give you the grader statement for this one too: 

# In[810]:


convert_date_type()
if price.Date.dtype == "datetime64[ns]":
  score['q2'] = 2


# In[811]:


score


# Question 3: [2 points] What is the mean of all opening stock price?

# In[812]:


def mean_of_opening():
  dtype = price['Open'].mean()
  return dtype # replace this with the correct statement

# print(mean_of_opening())


# Question 4: [4 points] What is the daily min volume for trades after 2010 (including 2010-1-1) 

# In[813]:


def min_daily_volume_after_2010():
    # Hint first construct a new dataframe by limiting the price for dates greater than 2010
    vol_df = price[(price['Date'] >= '2010-01-01')]    
    return vol_df['Volume'].min() # Replace this with your answer

# print(min_daily_volume_after_2010())


# Question 5: [4 points] Make a new column called up_binom. The value of up_binom is 1 if the closing price of the stock is higher (>=) than opening price, and 0 otherwise. Then find the number days the stock closed higher than openning.
# 

# In[814]:


def number_of_green_days():
  price['up_binom'] = price['Close'] >= price['Open']
  return price['up_binom'].sum(); # Replace this with your answer

# print(number_of_green_days())


# Question 5 [4 points] Plot the Closing price of the stock after 2020. The x-axis is day and the y-axis is the Closing price. 
# Look at the examples here for more help https://matplotlib.org/stable/gallery/index.html)

# In[815]:


# plot
df = price[(price['Date'] >= '2020-01-01')]
plt.scatter(x = df['Date'].dt.dayofyear, y = df['Close']) # scatterplot
plt.xlabel('Day of Year') # give x label
plt.ylabel('Close (price)') # give y label
plt.show() 


# Question 6: [4 points] If you had bought 1000$ worth Amazon stock (assume you could have fraction of stock too) on 2000-1-1 at opening, how much money would you have had on 2020-1-1 at closing?
# 

# In[816]:


# I'm going to make your life easier and set the date column you created as the index.
# This will make searching and extracting the values much easier
price = price.set_index('Date')

def market_value(buy_date, sell_date):
    price_df = price.loc[buy_date: sell_date]
    buy_close = price_df.iloc[0]['Close']
    sell_close = price_df.iloc[-1]['Close']
    shares = 1000 / buy_close
    close_val = shares * sell_close
    # profit = close_val - 1000
    # print(buy_close, shares, close_val, profit)
    # return profit
    return close_val

print(market_value('2000-1-1', '2020-1-1'))


# ## JSON
# 
# The last part of the assignment will have you working with some basic JSON data.  The URL links to a JSON file with stats on every episode of the TV show Silicon Valley
# 

# In[817]:


# First just run this to import the data
import requests
url = 'http://api.tvmaze.com/singlesearch/shows?q=Silicon Valley&embed=episodes'
sv_json_obj = requests.get(url)
sv_json = sv_json_obj.json()


# ### Viewing your JSON
# 
# Now just to look at what's in the JSON a bit
# 
# - Make a code cell that just calls the JSON we named above. 
# - Also run the .keys() function on the object.

# In[818]:


# Make code cell that call JSON
sv_json


# In[819]:


# Run the .keys() function on the object.
sv_json.keys()


# ### Questions
# 
# Based on these responses, what keys are present in the JSON.  More importantly, are there any keys that don't get returned by .keys()?

# In[820]:


# First, you can see the structure after moving down a level into '_embedded'
sv_json['_embedded']


# Some keys present in the json are id, url, name, type, and language.  There are keys that don't get returned by the .keys() function.  Some of those include airdate, airtime, airstamp.

# Question 7: [4 points] Get the day the show premiered. 

# In[821]:


def get_airdate_first_episode():
  premiered_day = sv_json['premiered']  
  return premiered_day; #replace this with the correct statements 

# print(get_airdate_first_episode())


# Question 8: [4 points] Get the summary of a specific episode.

# In[822]:


def get_summary(season, episode):
    summary = None
    for ep in sv_json['_embedded']['episodes']:
        episode_number = ep['number']
        episode_season = ep['season']  
        episode_summary = ep['summary']
        if episode_number == episode and episode_season == season:
            # print(season, episode, episode_season, episode_number, episode_summary)
            summary = episode_summary

    return summary;

print(get_summary(2, 4))


# In[ ]:





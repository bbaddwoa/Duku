
"""
Created on Thu Apr 15 01:51:29 2021

@author: Adwoa Osei-Yeboah

Using pandas read_html to Web Scrape Data for Data Science

"""

import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup 
import os
import pandas as pd
import numpy as np


pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)





# STEP 1: GET THE DATAFRAME
#********************************


# Scraping Team stat

url_team = 'https://sports.yahoo.com/ncaaw/teams/albany/stats'

# Read HTML webpage into pandas
#       --> Using pd.read_html() functioin to read HTML webpage

df = pd.read_html(url_team, header = 0)
team = df[0]    # Albany Great Danes Team




# Scraping Player 1 stat   #---> Game Log for 2020  All Season 
url_player1 = 'https://sports.yahoo.com/ncaaw/players/61478/gamelog?selectedTable=0'
df_P1 = pd.read_html(url_player1, header = 1)
player1 = df_P1[0]          # Helen Haegerstrand 

# Date was replaced NaN when scraped. Below is the right order from top to bottom
DATE = ' Feb 23, Feb 22, Feb 7, Feb 6, Jan 31, Jan 30, Jan 24, Jan 23, Jan 17, Jan 16, Dec 22, Dec 20, Dec 19, Dec 15, Dec 13, Dec 11'




# Scraping Player 2 stat     #---> Game Log for 2020   All Season
url_player2 = 'https://sports.yahoo.com/ncaaw/players/57827/gamelog?selectedTable=0'
df_P2 = pd.read_html(url_player2, header = 1)
player2 = df_P2[0]          # Lucia Decortes 

# Date was replaced NaN when scraped. Below is the right order from top to bottom
#DATE = ' Mar 7, Feb 28 , Feb 23, Feb 22, Feb 7, Feb 6, Jan 31, Jan 30, Jan 24, Jan 23, Jan 17, Jan 16, Dec 22, Dec 20, Dec 19, Dec 15, Dec 13, Dec 11'





# STEP 2: CLEANING THE DATA 
#********************************

# Player 1
# Date was replaced NaN when scraped. Below is the right order from top to bottom
#DATE = 'Mar 7, Feb 28 , Feb 23, Feb 22, Feb 7, Feb 6, Jan 31, Jan 30, Jan 24, Jan 23, Jan 17, Jan 16, Dec 22, Dec 20, Dec 19, Dec 15, Dec 13, Dec 11'

# replacing the date column
player1.loc[0, 'Date'] = '7-Mar-2020'
player1.loc[1, 'Date'] = '28-Feb-2020'
player1.loc[2, 'Date'] = '23-Feb-2020'
player1.loc[3, 'Date'] = '22-Feb-2020'
player1.loc[4, 'Date'] = '7-Feb-2020'
player1.loc[5, 'Date'] = '6-Feb-2020'
player1.loc[6, 'Date'] = '31-Jan-2020'
player1.loc[7, 'Date'] = '30-Jan-2020'
player1.loc[8, 'Date'] = '24-Jan-2020'
player1.loc[9, 'Date'] = '23-Jan-2020'
player1.loc[10, 'Date'] = '17-Jan-2020'
player1.loc[11, 'Date'] = '16-Jan-2020'
player1.loc[12, 'Date'] ='22-Dec-2020'
player1.loc[13, 'Date'] ='20-Dec-2020'
player1.loc[14, 'Date'] ='19-Dec-2020'
player1.loc[15, 'Date'] ='15-Dec-2020'
player1.loc[16, 'Date'] ='13-Dec-2020'
player1.loc[17, 'Date'] ='11-Dec-2020'


# replacing '-' with 0
player1.replace('-', 0)
player2.replace('-', 0)



# Player 2

# replacing the date column
player2.loc[0, 'Date'] = '7-Mar-2020'
player2.loc[1, 'Date'] = '28-Feb-2020'
player2.loc[2, 'Date'] = '23-Feb-2020'
player2.loc[3, 'Date'] = '22-Feb-2020'
player2.loc[4, 'Date'] = '7-Feb-2020'
player2.loc[5, 'Date'] = '6-Feb-2020'
player2.loc[6, 'Date'] = '31-Jan-2020'
player2.loc[7, 'Date'] = '30-Jan-2020'
player2.loc[8, 'Date'] = '24-Jan-2020'
player2.loc[9, 'Date'] = '23-Jan-2020'
player2.loc[10, 'Date'] = '17-Jan-2020'
player2.loc[11, 'Date'] = '16-Jan-2020'
player2.loc[12, 'Date'] ='22-Dec-2020'
player2.loc[13, 'Date'] ='20-Dec-2020'
player2.loc[14, 'Date'] ='19-Dec-2020'
player2.loc[15, 'Date'] ='15-Dec-2020'
player2.loc[16, 'Date'] ='13-Dec-2020'
player2.loc[17, 'Date'] ='11-Dec-2020'


# STEP 3: Creating a csv file for the dataset
#********************************

team.to_csv(r'C:\Users\16122\Documents\Data_Science\Luke_Class\PracticeQ_\Individual_Project\export_team.csv' , index=False, header=True)
player1.to_csv(r'C:\Users\16122\Documents\Data_Science\Luke_Class\PracticeQ_\Individual_Project\export_player1.csv' , index=False, header=True)
player2.to_csv(r'C:\Users\16122\Documents\Data_Science\Luke_Class\PracticeQ_\Individual_Project\export_player2.csv' , index=False, header=True)


# STEP 4: Reading the csv file
#********************************

team_csv = pd.read_csv('export_team.csv')
player1_csv = pd.read_csv('export_player1.csv')
player2_csv = pd.read_csv('export_player2.csv')






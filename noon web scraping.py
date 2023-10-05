#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import pandas as pd


# In[3]:


#this website wont run code until i changed headers with new user-agent
URL = 'https://www.noon.com/egypt-en/iphone-15-pro-256gb-natural-titanium-5g-with-facetime-middle-east-version/N53432933A/p/?o=d27c789444e2bfdf'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

page =requests.get(URL,headers=headers)
soup1= BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),'html.parser')

# scraping the title
title = soup2.find(class_="sc-66b023ec-17 hiHNhw").get_text()
title=title.strip()
print(title)

#scraping the price
r=soup2.find(class_="priceNow").get_text()
t=r.split('\n')
price=t[4].strip()
print(price)

#creating a variable that gives the day
today=datetime.date.today()


# In[4]:


#creating a table
import csv
header = ['Title', 'Price', 'Day']
data = [title , price, today]
with open('noon_scraper.csv', 'w', newline='',encoding='UTF8') as f :
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[5]:


df=pd.read_csv(r'C:\Users\Omar Mohamed\noon_scraper.csv')
df.head()


# In[49]:


#appinding data to the table using a+ insted of w
with open('noon_scraper.csv', 'a+', newline='',encoding='UTF8') as f :
    writer = csv.writer(f)
    
    writer.writerow(data)


# In[55]:


#automating the procecss eveyday 
def pricerecoder():
    RL = 'https://www.noon.com/egypt-en/iphone-15-pro-256gb-natural-titanium-5g-with-facetime-middle-east-version/N53432933A/p/?o=d27c789444e2bfdf'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

    page =requests.get(URL,headers=headers)
    soup1= BeautifulSoup(page.content,"html.parser")
    soup2=BeautifulSoup(soup1.prettify(),'html.parser')

        # scraping the title
    title = soup2.find(class_="sc-66b023ec-17 hiHNhw").get_text()
    title=title.strip()


    #scraping the price
    r=soup2.find(class_="priceNow").get_text()
    t=r.split('\n')
    price=t[4].strip()
    
    #creating a variable that gives the day
    today=datetime.date.today()
    
    import csv
    header = ['Title', 'Price', 'Day']
    data = [title , price, today]
    
    with open('noon_scraper.csv', 'a+', newline='',encoding='UTF8') as f :
        writer = csv.writer(f)
    
        writer.writerow(data)


# In[ ]:


#atoumatic checker 86400 is the sec in a day
while (True):
    pricerecoder()
    time.sleep(86400)


# In[ ]:





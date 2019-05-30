#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
import time
import pymongo


# In[6]:


executable_path = {"executable_path":"/Users/nyaha/class/chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)


# In[8]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[9]:


html = browser.html
soup = bs(html, "html.parser")


# In[10]:


news_title = soup.find("div", class_="content_title").text
news_paragraph = soup.find("div", class_="article_teaser_body").text
print(f"Title: {news_title}")
print(f"Para: {news_paragraph}")


# In[11]:


url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
browser.visit(url_image)


# In[12]:


from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
print(base_url)


# In[13]:


xpath = "//*[@id=\"page\"]/section[3]/div/ul/li[1]/a/div/div[2]/img"


# In[14]:


results = browser.find_by_xpath(xpath)
img = results[0]
img.click()


# In[15]:


html_image = browser.html
soup = bs(html_image, "html.parser")
img_url = soup.find("img", class_="fancybox-image")["src"]
full_img_url = base_url + img_url
print(full_img_url)


# In[ ]:


#Mars Weather


# In[16]:


url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[17]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")
#temp = soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
print(mars_weather)
#temp


# In[18]:


#Mars Facts


# In[19]:


url_facts = "https://space-facts.com/mars/"


# In[20]:


table = pd.read_html(url_facts)
table[0]


# In[21]:


df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[22]:


mars_html_table = df_mars_facts.to_html()
mars_html_table = mars_html_table.replace("\n", "")
mars_html_table


# In[23]:


url_hem= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url_hem)


# In[27]:


import time 
html = browser.html
soup = BeautifulSoup(html, 'html.parser')
mars_hemis=[]


# In[28]:


for i in range (4):
    time.sleep(5)
    images = browser.find_by_tag('h3')
    images[i].click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial = soup.find("img", class_="wide-image")["src"]
    img_title = soup.find("h2",class_="title").text
    img_url = 'https://astrogeology.usgs.gov'+ partial
    dictionary={"title":img_title,"img_url":img_url}
    mars_hemis.append(dictionary)
    browser.back()


# In[29]:


print(mars_hemis)


# In[ ]:





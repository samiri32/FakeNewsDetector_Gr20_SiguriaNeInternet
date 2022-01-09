# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:54:55 2022

@author: HP
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

data=[]
dataFrame = pd.DataFrame(data, columns =['lajmi'])



html_text = requests.get('https://kallxo.com/').text
soup = BeautifulSoup(html_text, 'lxml')
categories = soup.find('div', class_ = "menu_left_items")
categories = categories.find_all('li')

for category in categories:
    category_link = category.find('a')['href']

    html_text = requests.get(category_link).text
    soup = BeautifulSoup(html_text, 'lxml')
    divs_content = soup.find_all('div', class_="post_item")
    for div_content in divs_content:
        link = div_content.find('a')['href']
        html_text = requests.get(link).text
        soup = BeautifulSoup(html_text, 'lxml')
        title = soup.find('h1',class_='single_article__title').text
        content = None
        if "krypometer" in link:
            content = soup.find_all('div', class_ = "article_content focused_content")[2].find_all('p')
        else:
            content = soup.find('main', class_ = "single_article__main article_content").find_all('p')
        _content=""
        for con in content:
            _content += con.text
        _content = _content.replace("\n", "")
        lajmi = (title+"\n" + _content).replace("/REL", "")
        dictionary = {'lajmi': lajmi}
        dataFrame = dataFrame.append(dictionary, ignore_index=True)
    if "teknologji" in category_link: break
dataFrame.to_csv('ScrapAndWriteToCSV.csv', index=False, mode='w')


    
    

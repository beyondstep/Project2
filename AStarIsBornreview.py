from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import re
import csv
driver = webdriver.Chrome(r'C:\Users\Bird_\Desktop\selenium\chromedriver.exe')
movies_list = ['https://www.rottentomatoes.com/m/halloween_2018',
'https://www.rottentomatoes.com/m/a_star_is_born_2018']

csv_file = open('review.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
news_dict['reviews'] = 'reviews'
writer.writerow(news_dict.values())
for url in movies_list:
    driver.get(url)
    news_dict = {}
    audiencereview = driver.find_element_by_xpath('//section[@id = "audience_reviews"]/div/div[2]/a')
    audiencereview.click()
    time.sleep(2)
    second_page = driver.find_element_by_xpath('//div[@style = "display:inline-block; float:right"]/a[2]')
    second_page.click()
    time.sleep(2)
    index = 2
    while index <= 171:
        try:
            print("scraping Page Number" + str(index))
            index = index + 1
            reviews = driver.find_elements_by_xpath('//div[@class = "review_table"]/div/div[2]/div[2]/div').text
            next_button = driver.find_element_by_xpath('//div[@id="reviews"]/div[4]/a[2]')
            next_button.click()
            time.sleep(10)
        except Exception as e:
            print(e)
            break
    news_dict['reviews'] = reviews
    writer.writerow(news_dict.values())
driver.close()
csv_file.close()
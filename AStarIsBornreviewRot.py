from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import re
import csv
driver = webdriver.Chrome(r'C:\Users\Bird_\Desktop\selenium\chromedriver.exe')
movies_list = ['https://www.rottentomatoes.com/m/a_star_is_born_2018',
    'https://www.rottentomatoes.com/m/charm_city_2018']
#create csv file
csv_file = open('Rotreview.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
#create dictionary
news_dict = {}
#create column for dictionary
news_dict['review'] = 'review'
#add all title column created above to the first row of the csv file
writer.writerow(news_dict.values())
#retrieve movie title, critic score, audience score
for url in movies_list:
    driver.get(url)
    #always start with new dict
    news_dict = {}
#scrape movie title
    audiencereview = driver.find_element_by_xpath('//section[@id = "contentReviews"]/div/div[2]/a')
    audiencereview.click()
    time.sleep(10)
    page2 = driver.find_element_by_xpath('//div[@class = "row review_table_row"]/div')
    page2.click()
#Look at movie info box and extract all the information
    review_content = driver.find_elements_by_xpath('//div[@class="row review_table_row"]')
    for review in review_content:
        try:
            reviews = review.find_element_by_xpath('.//div[@class = "review_desc"]/div').text
            print(reviews)
        except:
            pass
        try:
            next_button = review.find_element_by_xpath('//*[@id="reviews"]/div[2]/div[5]/a[2]')
            next_button.click()
        except:
            continue
    news_dict['review'] = reviews
    writer.writerow(news_dict.values())
driver.close()
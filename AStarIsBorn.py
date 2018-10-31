from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import re
import csv
driver = webdriver.Chrome(r'C:\Users\Bird_\Desktop\selenium\chromedriver.exe')
movies_list = ['https://www.rottentomatoes.com/m/pick_of_the_litter',
    'https://www.rottentomatoes.com/m/charm_city_2018']
#create csv file
csv_file = open('movieinfo.csv6', 'w', encoding='utf-8')
writer = csv.writer(csv_file)
#create dictionary
news_dict = {}
#create column for dictionary
news_dict['title'] = 'title'
news_dict['genre'] = 'genre'
news_dict['critic_score'] = 'critic_score'
news_dict['audience_rating'] = 'audience_rating'
news_dict['director'] = 'director'
news_dict['studio'] = 'studio'
#add all title column created above to the first row of the csv file
writer.writerow(news_dict.values())
#retrieve movie title, critic score, audience score
for url in movies_list:
    driver.get(url)
    #always start with new dict
    news_dict = {}
#scrape movie title
    title = driver.find_element_by_xpath('//section[@id="newsSection"]/h2/em').text
    print(title)
#scrape critic score
    critic_meter = driver.find_elements_by_xpath('//div[@class="tab-pane active"]')
    for criticscore in critic_meter:
        critic_score = criticscore.find_element_by_xpath('//span[@class="meter-value superPageFontColor"]/span').text
        print(critic_score)
#scrape audience score  
    audience_meter = driver.find_elements_by_xpath('//div[@class="col-sm-8 col-xs-12 audience-panel"]')
    for audiencescore in audience_meter:
        audience_score = audiencescore.find_element_by_xpath('//span[@class="superPageFontColor"]').text
        print(audience_score)
        print("*" * 50)
#change to audience review page
#audiencereview = driver.find_element_by_xpath('//section[@id = "audience_reviews"]/div/div/a').get_attribute('href')
    audiencereview = driver.find_element_by_xpath('//section[@id = "contentReviews"]/div/div[2]/a')
    audiencereview.click()
    time.sleep(10)
#Look at movie info box and extract all the information
    movie_info = driver.find_elements_by_xpath('//div[@class="col col-left hidden-xs"]/section/div')
    for info in movie_info:
        #Scrape genre
        genre = info.find_element_by_xpath('//div[@class = "bottom_divider"]/ul/li/a/span').text
        print(genre)
    #Scrape Director
        director = info.find_element_by_xpath('//div[@class = "bottom_divider"][1]/ul/li[3]/a').text
        print(director)
    #Scrape studio
        studio = info.find_element_by_xpath('.//div[@class = "bottom_divider"]/ul/li[6]').text
        print(studio)
        print("*"*50)
    reviews = driver.find_elements_by_xpath('//div[@class = "row review_table_row"]')
 
    news_dict['title'] = title
    news_dict['critic_score'] = critic_score
    news_dict['audience_score'] = audience_score
    news_dict['genre'] = genre
    news_dict['director'] = director
    news_dict['studio'] = studio
    writer.writerow(news_dict.values())
driver.close()
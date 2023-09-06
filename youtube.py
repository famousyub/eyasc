from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()

driver.get('https://www.youtube.com/watch?v=hhYZVt_VSAw')

driver.execute_script('window.scrollTo(1, 500);')

#now wait let load the comments
time.sleep(20)

driver.execute_script('window.scrollTo(1,3000 );')


comments_youtube=[]
comment_div=driver.find_element(By.XPATH, '//*[@id="contents"]')
comments=comment_div.find_elements(By.XPATH,'//*[@id="content-text"]')
for comment in comments:
    comments_youtube.append(comment.text)

for i in comments_youtube:
    print(i)


comments_dict = {'Comments_youtube':comments_youtube}
comments_youtube_df = pd.DataFrame(comments_dict)
print(comments_youtube_df)

print(comments_youtube_df.shape)
comments_youtube_df.to_csv(r'./comments_youtube.csv')









SCROLL_PAUSE_TIME = 3

# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    
titles = driver.find_elements(By.ID, "video-title")
views = driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')
images = driver.find_elements(By.XPATH,'//*[@id="dismissible"]/ytd-thumbnail/a/yt-img-shadow/img')
data = []
for i, j, k in zip(titles, views, images ):
    data.append([i.text, j.text, k.get_attribute('src')])
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Title', 'views', 'Thumbnail'])
df.to_csv('youtube_videos_details.csv')

driver.quit()
# from bs4 import BeautifulSoup
# from selenium import webdriver
# driver = webdriver.Chrome()
# url = 'https://www.reddit.com/r/DunderMifflin/comments/mf1y4j/makes_it_all_worth_it/'
# driver.get(url)
# html =  BeautifulSoup(driver.page_source, "html.parser")
# result = html.find_all("p",{"class":"_1qeIAgB0cPwnLhDF9XSiJM"})
# for item in result:
#     print(item.text)



import praw
import pandas as pd

user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
reddit_read_only = praw.Reddit(client_id="ogaAC0VEVOITWRw53JOEeg",		 # your client id
							client_secret="XYK1JFrt7_whi4KeXN4ROkjdNmjm7w",	 # your client secret
							user_agent="webscrapping")	 # your user agent

reddit_read_only.read_only = True
subreddit = reddit_read_only.subreddit("redditdev")

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

subreddit = reddit_read_only.subreddit("Python")

for post in subreddit.hot(limit=5):
	print(post.title)
	print()


posts = subreddit.top("month")
# Scraping the top posts of the current month

posts_dict = {"Title": [], "Post Text": [],
			"ID": [], "Score": [],
			"Total Comments": [], "Post URL": []
			}

for post in posts:
	# Title of each post
	posts_dict["Title"].append(post.title)
	
	# Text inside a post
	posts_dict["Post Text"].append(post.selftext)
	
	# Unique ID of each post
	posts_dict["ID"].append(post.id)
	
	# The score of a post
	posts_dict["Score"].append(post.score)
	
	# Total number of comments inside the post
	posts_dict["Total Comments"].append(post.num_comments)
	
	# URL of each post
	posts_dict["Post URL"].append(post.url)

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)

import pandas as pd

top_posts.to_csv("TopPosts.csv", index=True)


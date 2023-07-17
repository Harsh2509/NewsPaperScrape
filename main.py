from news_extract import *
from news_nlp import *
from news_scrape import *
import time

print()
print("Hi all! Welcome to Media bias detection project")
print("-Harsh")
print("***********************************************************")


content_string = get_content_string('https://www.nytimes.com/section/technology')
# print(content_string)
start_indices, end_indices = find_occurrences(content_string)
# print(start_indices)
# print(end_indices)
url_list = get_all_urls(start_indices, end_indices, content_string)
# print(url_list)

for url in url_list:
    print("Article URL: " + str(url))
    article_summary = summarize_article(url)
    findSentiment(article_summary)
    print("***********************************************************")
    print()
    time.sleep(4)
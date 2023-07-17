import requests
from bs4 import BeautifulSoup as soup

def get_content_string(url):
    page = requests.get(url)    #sends get request to the given url
    page_soup = soup(page.content, 'html.parser')
    # print(page_soup)

    containers = page_soup.find_all("script", {"type": "application/ld+json"})
    # print(container)
    article_list = []

    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)

    content_string = article_list[0]

    article_index = content_string.index('itemListElement')
    content_string = content_string[article_index+18:]
    return content_string


def find_occurrences(content_string):
    start_indices = []
    end_indices = []
    for i in range(len(content_string)):
        if content_string.startswith("https://www.nytimes.com/2023", i):
            start_indices.append(i)
        if content_string.startswith(".html", i):
            end_indices.append(i+5)
    return start_indices, end_indices


def get_all_urls(start_indices, end_indices, content_string):
    url_list = []
    for i in range(len(start_indices)):
        url_list.append(content_string[start_indices[i]:end_indices[i]])
    return url_list



# content_string = get_content_string('https://www.nytimes.com/section/technology')
# print(content_string)
# start_indices, end_indices = find_occurrences(content_string)
# print(start_indices)
# print(end_indices)
# url_list = get_all_urls(start_indices, end_indices, content_string)
# print(url_list)

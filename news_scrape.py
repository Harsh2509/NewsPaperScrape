from newspaper import Article
# import nltk


def summarize_article(url):
    article = Article(url)

    article.download()
    article.parse()

    article.download("punkt")
    article.nlp()

    # print("Author: " + str(article.authors))

    date = article.publish_date
    # print("Publish Date: " + str(date.strftime('%d/%m/%Y')))
    #
    # print("Top image URL: " + str(article.top_image))

    image_string = "All Images: "
    for image in article.images:
        image_string += '\n\t' + image
    # print(image_string)
    #
    # print()
    # print("A Quick Article Summary")
    # print("-----------------------------------------")
    # print(article.summary)
    return article.summary
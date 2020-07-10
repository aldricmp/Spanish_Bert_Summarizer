# News article catcher using newspaper3k
# Gets news site's articles and categories from front page (NOT FINISHED!)
# Gets article's title, authors, date, text, main image, social media  and movie clips

import newspaper
from newspaper import Article


def get_news_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article


# cnn_paper = newspaper.build('https://www.milenio.com', memoize_articles=False)
# print(cnn_paper.size())
#
# for article in cnn_paper.articles:
#     print(article.url)
# for category in cnn_paper.category_urls():
#     print(category)
#
# print(cnn_paper.brand)
# print(cnn_paper.description)
#
#
# first_article = cnn_paper.articles[0]
# first_article.download()
# # print(first_article.html)
#
# first_article.parse()
# print('TÍTULO: ' + first_article.title)
# print('IMAGEN: ' + first_article.top_image)
# print('TEXTO= '+first_article.text)
# print('AUTORES: ' + str(first_article.authors))
# print('IMAGENES: ' + str(first_article.images))
# print('URL: ' + first_article.url)
#
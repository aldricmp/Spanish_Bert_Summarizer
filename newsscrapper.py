# News scrapper
import requests
from bs4 import BeautifulSoup
import numpy as np
import newscatcher as nc
import time


# Load content from url, selection of news media site
def get_news_from_url(url):
    body=''
    tweet_html=''
    news_article=''
    video_html=''
    instagram_html=''

    if url.find('milenio.com') != -1:
        news_article = nc.get_news_article(url)
        body, tweet_html, video_html, instagram_html = news_scrapper_milenio(url)
    else:
        news_article = nc.get_news_article(url)
        body = str(news_article.text)
    return news_article, body, tweet_html, video_html, instagram_html


# Milenio news scrapper
def news_scrapper_milenio(url):
    final_article = ''
    final_tweet = ''
    final_video = ''
    final_instagram = ''
    tweet_html = []
    video_html = []
    instagram_html = []
    # Beautiful Soup initialization
    article = requests.get(url)
    article_content = article.content
    # Get html code from Body
    soup_article = BeautifulSoup(article_content, 'html.parser')
    body = soup_article.find('div', class_='body-content')

    if body:
        # Get Videos
        video_html += ['https://www.youtube.com/watch?v=' + str(video['data-reference'])
                       for video in body.find_all('div', class_='holder-container')
                       if video['data-provider'] == 'camus.media.youtube_provider']
        video_html += ['https://www.youtube.com/watch?v=' + str(video['video-id'])
                       for video in body.find_all('div', class_='camus-youtube video-item')]
        video_html += ['https://www.youtube.com/watch?v=' + str(video['video-id'])
                       for video in body.find_all('div', class_='camus-youtube')]

        video_html = list(dict.fromkeys(video_html))

        final_video = ' '.join(video_html)
    # Get html from Article Body
    body = soup_article.find('div', itemprop='articleBody')
    if body:
        # Get Tweets and remove them from Body
        tweet_val = body.find_all('blockquote', class_='twitter-tweet')
        if tweet_val:
            for tweet in body.find_all('blockquote', class_='twitter-tweet'):
                tweet_html.append(str(tweet))
                tweet.decompose()
            final_tweet = ' '.join(tweet_html)

        # Get Instagram posts and remove them from Body
        instagram_val = body.find_all('blockquote', class_='instagram-media')
        if instagram_val:
            for instagram in body.find_all('blockquote', class_='instagram-media'):
                instagram_html.append(str(instagram))
                instagram.decompose()
            final_instagram = ' '.join(instagram_html)

    # Get text from paragraphs, headers and lists tags

    if body:
        for tag in body.find_all('div', class_='nd-rnd-media'):
            tag.decompose()
        stripped_article = BeautifulSoup(''.join(str(body)), 'html.parser')

        x = stripped_article.find_all(['p', 'h2', 'li', 'blockquote'])
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
    # Return features as string
    return final_article, final_tweet, final_video, final_instagram
#EXAMPLE LINKS:
# Time Measure
# tic=time.time()
# news_scrapper_milenio('https://www.milenio.com/internacional/ivanka-trump-celebra-visita-amlo-unidos')
# news_scrapper_milenio('https://www.milenio.com/videos/politica/reunion-profundizara-mas-nuestra-amistad-dice-ivanka-trump')
# news_scrapper_milenio('https://www.milenio.com/politica/amlo-visita-presidente-mexico-aterriza-washington')
# news_scrapper_milenio('https://www.milenio.com/politica/comunidad/semaforo-naranja-cdmx-esteticas-reabren-citas-escalonadas')
# news_scrapper_milenio('https://www.milenio.com/estilo/viajes/grupo-vidanta-lanza-programa-estandares-extraordinarios')
# news_scrapper_milenio('https://www.milenio.com/espectaculos/famosos/luis-miguel-ex-novia-cuenta-como-fue-su-romance-con-el-cantante')
# toc=time.time()
# print(toc-tic)

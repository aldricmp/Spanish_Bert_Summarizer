# Word Cloud Generator
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image


def generate_wordcloud(words):
        mask = np.array(Image.open("images/mask.png"))
        wordcloud_mex = WordCloud(background_color="white", mode="RGBA", max_words=1000, mask=mask).generate(words)
        image_colors = ImageColorGenerator(mask)
        plt.figure(figsize=[5, 3])
        plt.imshow(wordcloud_mex.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        wordcloud_mex.to_file('images/flag_cloud.png')
        return 'images/flag_cloud.png'

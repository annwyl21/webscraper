import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from htmlpages.ws_html import web_scraper
from jspages.ws_js import web_scraper_js

def create_CVwordcloud():

    with open('./my_cv.txt', 'r') as f:
        my_cv = f.read()

    stopwords = set(STOPWORDS)
    stopwords.update(['course', 'introduction', 'various', 'developed', 'site', 'sought', 'learned', 'project', 'using', 'coding', 'symptom', 'create', 'symptoms', 'given', 'created', 'use'])

    wc = WordCloud(max_words=500,
                relative_scaling=0.5,
                #mask=mask,
                background_color='black',
                stopwords=stopwords,
                margin=2,
                random_state=7,
                contour_width=2,
                contour_color='orange',
                colormap='Oranges').generate(my_cv)
    colors = wc.to_array()
    plt.figure()
    plt.imshow(colors, interpolation="bilinear")
    plt.axis('off')
    plt.savefig('wordCloud.png')
    plt.show()

# web_scraper()
web_scraper_js()
create_CVwordcloud()

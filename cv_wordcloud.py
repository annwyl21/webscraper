import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import web_scraper as ws

def create_CVwordcloud():

    with open('./wordcloud/my_cv.txt', 'r') as f:
        my_cv = f.read()

    stopwords = set(STOPWORDS)
    stopwords.update(['course', 'introduction', 'various', 'developed', 'site', 'sought', 'learned', 'project', 'using', 'coding', 'symptom'])

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

# ws.web_scraper()
create_CVwordcloud()
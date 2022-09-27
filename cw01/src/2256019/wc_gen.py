# For fun and create Word Cloud.
# from a piece of text. 
import pandas as pd 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("handbook.txt", sep=' ')
text = ' '.join( str(cat) for cat in df.Review)
word_cloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="salmon",
        colormap="Pastel1",
        collocations=False,
        stopwords=STOPWORDS,
        ).generate(text)

plt.imshow(word_cloud)
plt.axis("off")
plt.show()
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.book import *

def createWordCloud(inputText):
    voc = inputText.vocab()
    word_string = [(w + ' ') * voc[w] for w in voc.keys()]
    word_string = ' '.join(word_string)

    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000).generate(word_string)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

createWordCloud(text1)
createWordCloud(text2)
createWordCloud(text3)
createWordCloud(text4)
createWordCloud(text5)
createWordCloud(text6)
createWordCloud(text7)
createWordCloud(text8)
createWordCloud(text9)

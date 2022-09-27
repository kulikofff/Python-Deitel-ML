
'''
from textblob import TextBlob
from textblob import Word
from pathlib import Path
from textblob.sentiments import NaiveBayesAnalyzer
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator)
import nltk
nltk.download('omw-1.4')
import nltk
from nltk.corpus import stopwords

###1
text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)
print(blob, blob.sentences, blob.words, blob.tags)
#Extraction of nominal constructions:
print(blob.noun_phrases)

#Analysis of emotion:
text1 = "This project is risky, but I love it. Tomorrow looks like bad weather - we shall not check it. I miss you!"
blob1 = TextBlob(text1)
print()
print(f'Sentiment analisys: {text1}')
print(f'Sentiment analisys of the whole text: {blob1.sentiment}')
print('Translation of sentences:')
for sentence in blob1.sentences:
    print(sentence.sentiment)

#Analysis of emotion with translation of deep-translator:
text2 = "Это прекрасно! Большое спасибо. Я к Вам больше никогда не приду, потому что ваш сервис крайне плох! Ужасно, катастрофа! Потрясающий сервис."
translated = GoogleTranslator(source='auto', target='en').translate(text2)
print()
print(f'Sentiment analisys with translate: {translated}')
blob2 = TextBlob(translated)
print(f'Sentiment analisys of the whole text: {blob2.sentiment}')
print('Sentiment analisys of sentences:')
for sentence in blob2.sentences:
    print(sentence.sentiment)


#Analysis with NaiveBayesAnalyzer(imho, better result):
print()
blob3 = TextBlob(translated, analyzer=NaiveBayesAnalyzer())
print(f'Sentiment analisys NaiveBayesAnalyzer: {blob3.sentiment}')
print('Sentiment analisys of sentences NaiveBayesAnalyzer:')
for sentence in blob3.sentences:
    print(sentence.sentiment)

#singular and plural
index = Word('index')
print()
print(index.pluralize())
animals = TextBlob('dog cat fish bird').words
print(animals.pluralize())

#Spellchecking
word = Word('theyr')
print()
print(word.spellcheck())
print(word.correct())

#Lemmatization
word = Word('varieties')
print()
print(word.stem())
#print(word.lemmatize()) - didn't work:(((

#frequency of words
blob = TextBlob(Path('RomeoAndJuliet_cut.txt').read_text())
print()
print(blob.word_counts['juliet'], blob.word_counts['romeo'], blob.word_counts['thou'], blob.words.count('joy'), blob.noun_phrases.count('lady capulet'))

#definitions
text2 = Word('счастливый')
translated2 = Word(GoogleTranslator(source='auto', target='en').translate(text2))
print(translated2)
print(translated2.definitions)

#synonym
print()
print(translated2.synsets)
synonyms = set() #deletes duplicates
for synset in translated2.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())
print(synonyms)

#antonym
ant = translated2.synsets[0].lemmas()
print(ant[0].antonyms())

#ignore stopwords and N-grams
nltk.download('stopwords')
stops = stopwords.words('english')
stops1 = stopwords.words('russian')
print(stops, stops1)

blob4 = TextBlob('Today is a beautiful day. Tomorrow looks like bad weather.')
print()
print([word for word in blob4.words if word not in stops])
print(blob4.ngrams())
print(blob4.ngrams(n=5))


#Visualization

from pathlib import Path
from textblob import TextBlob
import matplotlib.pyplot as plt
from operator import itemgetter
import pandas as pd
blob = TextBlob(Path('RomeoAndJuliet_cut.txt').read_text())
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

items = blob.word_counts.items()
items = [item for item in items if item[0] not in stop_words]
print(items)


sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print()
print(sorted_items)
print()
top20 = sorted_items[1:21]
print(top20)


df = pd.DataFrame(top20, columns=['word', 'count'])
axes = df.plot.bar(x='word', y='count', legend=False)
plt.gcf().tight_layout()
plt.show()


#Word Cloud
from pathlib import Path
import imageio.v2 as imageio
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = Path('RomeoAndJuliet_cut.txt').read_text()
mask_image = imageio.imread('mask_heart.png')
wordcloud = WordCloud(colormap='prism', mask=mask_image, 
    background_color='white')
wordcloud = wordcloud.generate(text)
wordcloud = wordcloud.to_file('RomeoAndJulietHeart.png')

plt.imshow(wordcloud)
plt.show()

#Evaluation of readability
from pathlib import Path
text = Path('RomeoAndJuliet_cut.txt').read_text()
from textatistic import Textatistic
readability = Textatistic(text)
print(readability.dict())
'''

#recognition of named entities
#https://spacy.io/usage
#pip uninstall flask
#pip install flask
#python -m spacy download en
#python -m spacy download en_core_web_sm
import spacy

spacy.prefer_gpu()
nlp = spacy.load("en_core_web_sm")

document = nlp('In 1994, Tim Berners-Lee founded the ' + 
                'World Wide Web Consortium (W3C), devoted to ' +
                'developing web technologies')

for entity in document.ents:
    print(f'{entity.text}: {entity.label_}')

# comparison of text
from pathlib import Path

document1 = nlp(Path('RomeoAndJuliet_cut.txt').read_text())
document2 = nlp(Path('LICENSE.txt').read_text())
print(document1.similarity(document2))
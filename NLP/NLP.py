
###!!!Load python.exe NLP.py!!!###  

from textblob import TextBlob
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator)
###1
text = "Today is a beautiful day. Tomorrow looks like bad weather."
blob = TextBlob(text)
print(blob, blob.sentences, blob.words, blob.tags)
#Extraction of nominal constructions
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

#Analysis of emotion with translation of deep-translator.

text2 = "Это прекрасно! Большое спасибо. Я к Вам больше никогда не приду, потому что ваш сервис крайне плох!"
translated = GoogleTranslator(source='auto', target='en').translate(text2)
print()
print(f'Sentiment analisys with translate: {translated}')
blob2 = TextBlob(translated)
print(f'Sentiment analisys of the whole text: {blob2.sentiment}')
print('Translation of sentences:')
for sentence in blob2.sentences:
    print(sentence.sentiment)
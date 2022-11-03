from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
#https://keras.io/api/layers/core_layers/embedding/
from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import load_model
from clearml import Task, Logger

#Clear ML credentials
task = Task.init(
    project_name='IMDB', 
    task_name='Task1', 
    tags=['IMDB','Sequential'])


'''
imdb = imdb.load_data()
print('Type of dataset:')
print(type(imdb))
print()
print('Input dataset:')
print(imdb)
print()
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
'''
#Loading
number_of_words = 1000
#number_of_words = 30000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=number_of_words)

'''
#Coding of words
word_to_index = imdb.get_word_index()
print(word_to_index['milk'])

index_to_word = {index: word for (word, index) in word_to_index.items()}

print([index_to_word[i] for i in range(1, 88)])
print(' '.join([index_to_word.get(i - 3, '?') for i in X_train[124]]))
print(y_train[124])
'''
#Cut of train

words_per_review = 200
#words_per_review = 1600
X_train = pad_sequences(X_train, maxlen=words_per_review)
X_test = pad_sequences(X_test, maxlen=words_per_review) 
print(X_train.shape, X_test.shape)


X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, random_state=11, test_size=0.20)
print(X_test.shape, X_val.shape)
rnn = Sequential()

rnn.add(Embedding(input_dim=number_of_words, output_dim=128, input_length=words_per_review))
rnn.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
rnn.add(Dense(units=1, activation='sigmoid'))
rnn.compile(optimizer='adam',
            loss='binary_crossentropy', 
            metrics=['accuracy'])

print(rnn.summary())
#Train model
rnn.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
#rnn.save('imdb_rnn_30k_1600.h5')
rnn.save('imdb_rnn_1k_200.h5')


task.close()

'''
#Load trained model
#rnn = load_model('imdb_rnn.h5')
rnn = load_model('imdb_rnn_30k_1600.h5')
loss, accuracy = rnn.evaluate(X_test, y_test)
print(loss)
print(accuracy)

#Test your text and convert words to indexes
#https://stackoverflow.com/questions/51363709/how-to-predict-sentiment-analysis-using-keras-imdb-dataset

import nltk
nltk.download('punkt')
from nltk import word_tokenize
#from keras.preprocessing import sequence
#https://stackoverflow.com/questions/72314364/missing-function-keras-sequence-pad-sequences-from-tensorflow-library
from keras.utils import data_utils
word2index = imdb.get_word_index()
test=[]
for word in word_tokenize( "this film is great"):
     test.append(word2index[word])

test=data_utils.pad_sequences([test],maxlen=words_per_review)
print(test)

print(rnn.predict(test))
'''
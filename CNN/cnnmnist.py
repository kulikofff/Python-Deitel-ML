from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten, MaxPooling2D
from tensorflow.keras.utils import plot_model
from IPython.display import Image
from tensorflow.keras.models import load_model
sns.set(font_scale=2)

'''
mnistds = mnist.load_data()
print('Type of dataset:')
print(type(mnistds))
print()
print('Input dataset:')
print(mnistds)
print()
'''

(X_train, y_train), (X_test, y_test) = mnist.load_data()

'''
index = np.random.choice(np.arange(len(X_train)), 24, replace=False)
figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(16, 9))
for item in zip(axes.ravel(), X_train[index], y_train[index]):
    axes, image, target = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([]) # remove x-axis tick marks
    axes.set_yticks([]) # remove y-axis tick marks
    axes.set_title(target)
plt.tight_layout()
plt.show()
'''
X_train = X_train.reshape((60000, 28, 28, 1)) 
X_test = X_test.reshape((10000, 28, 28, 1))

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#print(X_test.shape)
#print(y_train.shape)
'''
cnn = Sequential()
cnn.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
cnn.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))
#One dimension
cnn.add(Flatten())

cnn.add(Dense(units=128, activation='relu'))
cnn.add(Dense(units=10, activation='softmax'))
print(cnn.summary())

plot_model(cnn, to_file='convnet.png', show_shapes=True, show_layer_names=True)

#https://keras.io/optimizers/ https://keras.io/losses/
cnn.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

cnn.save('mnist_cnn.h5')
'''
#Load and test model


cnn = load_model('mnist_cnn.h5')
loss, accuracy = cnn.evaluate(X_test, y_test)
print(loss)
print(accuracy)

print(y_test[0])
predictions = cnn.predict(X_test)

for index, probability in enumerate(predictions[0]):
    print(f'{index}: {probability:.10%}') 


images = X_test.reshape((10000, 28, 28))
incorrect_predictions = []

for i, (p, e) in enumerate(zip(predictions, y_test)):
 predicted, expected = np.argmax(p), np.argmax(e)
 
if predicted != expected:
    incorrect_predictions.append(
        (i, images[i], predicted, expected))

print(len(incorrect_predictions))

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(16, 12))
for axes, item in zip(axes.ravel(), incorrect_predictions):
    index, image, predicted, expected = item
    axes.imshow(image, cmap=plt.cm.gray_r)
    axes.set_xticks([]) # remove x-axis tick marks
    axes.set_yticks([]) # remove y-axis tick marks
    axes.set_title(
        f'index: {index}\np: {predicted}; e: {expected}')
plt.tight_layout()
plt.show()

def display_probabilities(prediction):
    for index, probability in enumerate(prediction):
        print(f'{index}: {probability:.10%}')

print(display_probabilities(predictions[495]))
print(display_probabilities(predictions[583]))
print(display_probabilities(predictions[625]))
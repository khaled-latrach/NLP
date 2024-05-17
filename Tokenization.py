import tensorflow as ts
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    'I love my dog',
    'I love my cat'
]

tokenizer = Tokenizer(num_words = 0)
tokenizer.fit_on_texts(sentences)
word_index  = tokenizer.word_index
print(word_index)
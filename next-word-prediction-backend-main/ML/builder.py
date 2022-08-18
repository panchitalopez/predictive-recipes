#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys

# path where the script is executing
C_PATH = sys.argv[0]
C_PATH = C_PATH.split("/")
del C_PATH[-1]
C_PATH = "/".join(C_PATH) +"/data/"
sys.stderr.write(sys.executable+" || "+C_PATH)
sys.stdout=open(C_PATH+'log.txt','w+');

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
import pickle
import numpy as np
import os




# In[9]:


file = open(C_PATH+"data.txt", "r", encoding = "utf8")

# store file in list
lines = []
for i in file:
    lines.append(i)

# Convert list to string
data = "" 
for i in lines:
  data = ' '. join(lines) 

#replace unnecessary stuff with space
#   #new line, carriage return, unicode character --> replace by space

#remove unnecessary spaces 
data = data.split()
data = ' '.join(data)


# In[10]:


tokenizer = Tokenizer(oov_token=1)
tokenizer.fit_on_texts([data])
# saving the tokenizer for predict function
pickle.dump(tokenizer, open(C_PATH + 'token.pkl', 'wb'))

sequence_data = tokenizer.texts_to_sequences([data])[0]


# In[11]:


vocab_size = len(tokenizer.word_index) + 1
PREDICT_INP=2 # number of words taken as input to predict the next word


# In[12]:


sequences = []

for i in range(PREDICT_INP, len(sequence_data)):
    words = sequence_data[i-PREDICT_INP:i+1]
    sequences.append(words)
    
sequences = np.array(sequences)


# In[15]:


X = []
y = []

for i in sequences:
    X.append(i[0:PREDICT_INP])
    y.append(i[PREDICT_INP])
    
X = np.array(X)
y = np.array(y)

y = to_categorical(y, num_classes=vocab_size)


# In[16]:


model = Sequential()
model.add(Embedding(vocab_size, 10, input_length=PREDICT_INP))
model.add(LSTM(1000, return_sequences=True))
model.add(LSTM(1000))
model.add(Dense(1000, activation="relu"))
model.add(Dense(vocab_size, activation="softmax"))


# In[17]:


from tensorflow.keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(C_PATH+"next_words.h5", monitor='loss', verbose=1, save_best_only=True)
model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))
model.fit(X, y, epochs=70, batch_size=64, callbacks=[checkpoint])
sys.stderr.write("done building!");


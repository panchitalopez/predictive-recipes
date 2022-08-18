"""
Group 4: Naima Mamataz and Panchita Lopez-Li 
This file preprocesses the sample input text, tokenizes, creates, trains, and builds the predictive model. 
"""
import string
import numpy as np
from nltk.tokenize import word_tokenize # Separates phrase/sentence into individual words 
import tensorflow as tf # ML library
from tensorflow import keras # ML library 
from tensorflow.keras.preprocessing.text import Tokenizer  # Tokenizes values
from tensorflow.keras.models import Sequential # Creates Sequential Model 
from tensorflow.keras.utils import to_categorical # Converts vectors into binary classification
from tensorflow.keras.layers import Embedding, LSTM, Dense # Creates LSTM layers 
from tensorflow.keras.optimizers import Adam # Uses Adam optimizer 
from tensorflow.keras.callbacks import ModelCheckpoint # Implemented to save model file 
from tensorflow.keras.models import load_model # Starts prediction 
import itertools as it # increments count 
import pickle # saves tokenizer file
from tensorflow.keras.preprocessing.sequence import pad_sequences # Pads sequences 


############################### PRE-PROCESSING THE MODEL #######################################
# Loading/opening the data from the sample txt file (this is the pancake.txt file), reading it in 
# Closing it to get ready to work with this file

file_name = 'pancakes.txt'
file = open(file_name, 'rt', encoding = 'utf-8')
text = file.read()

# Splitting into individual words 
tokens = word_tokenize(text)
# Splitting by whitespace 
new = text.split() 

# Removing punctuation with the string.punctuation file from the string module 
# Mapping one set of chars to another, translating, then removing it.
remove_punctuation = str.maketrans("","", string.punctuation)
new_txt = [i.translate(remove_punctuation) for i in new]

# Changing all of the text to lowercase 
for i in range(len(new_txt)):
    new_txt[i] = new_txt[i].lower()
list(new_txt) 

############################### TOKENIZING THE MODEL #######################################
'''
Sources: 
https://datascience.stackexchange.com/questions/93651/reason-for-adding-1-to-word-index-for-sequence-modeling
https://www.tensorflow.org/text/tutorials/nmt_with_attention 
'''

# Tokenizing with Keras Tokenizer 
tokenizer = Tokenizer()

# Creates and updates the vocabulary index based on a list of strings/text and accounts
# for word frequency 
tokenizer.fit_on_texts([new])

# Saves the tokenized file by storing the object data to the file 
# The object data to be stored in this case is the tokenizer,
# Then, the serialized_token.pkl to be opened 
# It is stored in write-binary(wb) mode 
pickle.dump(tokenizer, open('token.pkl','wb'))

# Function using the Keras library to convert text to sequence of integers
# Tokenizes the vocabulary index from the first item (0th position) to transform the text into a series of sequences 
text_to_int = tokenizer.texts_to_sequences([new])[0]

# The tokenizer.word_index starts at index 1 and the token IDs are assigned incrementally 
# so must account for the last token ID from the zero to the first position of the sequence
input_vocab_size = len(tokenizer.word_index)+1

# Takes user input for after how many words should a prediction be formed. 
# This in turn will help determine the number of sequences 
# Created an empty list to later append the matrices for predictions
new_list = []
num_of_words = int(input("After how many words do you want a prediction to occur? Please enter a number: "))

# Iteration: the next word will be predicted depending on the number of words the user has inputted
# Cycles through the entirety of the sequence of integers and increments 
# Appends the new sequences to a new list and prints 
for word in range(num_of_words,len(text_to_int)):
    input_range = text_to_int[word-num_of_words:word+1]
    new_list.append(input_range)
print(new_list)

# Converting list into array for predictions 
new_list = np.array(new_list) 

# Input & output values for matrix classification in identifying the independent value (input)
# and dependent value (output)
pred_input = []
pred_output = []

# Appending first words and last word
for i in new_list:
    pred_input.append(i[0:num_of_words])
    pred_output.append(i[num_of_words])

# Converting into array
pred_input = np.array(pred_input)
pred_output = np.array(pred_output)

'''
Ex from documentation:
a = tf.keras.utils.to_categorical([0, 1, 2, 3], num_classes=4)
https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical
'''
# Converting class vectors into binary class matrix
# num_classes is a parameter that defines how many outputs that the classifier has
pred_output = tf.keras.utils.to_categorical(pred_output, num_classes=input_vocab_size)


############################### CREATING THE MODEL #######################################
''' Documentation: 
https://stackoverflow.com/questions/47262955/how-to-import-keras-from-tf-keras-in-tensorflow
https://stats.stackexchange.com/questions/241985/understanding-lstm-units-vs-cells
https://keras.io/guides/working_with_rnns/
https://www.kaggle.com/code/kmkarakaya/lstm-output-types-return-sequences-state/notebook
https://keras.io/api/layers/core_layers/dense/
https://wandb.ai/lavanyashukla/visualize-models/reports/How-to-stack-multiple-LSTMs-in-keras---VmlldzoxOTg2MTY
'''

def Create_model():
    LSTM_val = int(input("Please input number of layers for LSTM. If you have a higher number of unique parameters, size up! "))
    # Creating the LSTM layers with a Sequential model 
    model = Sequential()
    # The embedding layer enables the conversion of each word into a fixed length vector of defined size 
    # which will help to represent words in a better way with reduced dimensions.
    # Embedding takes in three arguments: size of vocab in text data, size of vector space for embedding, and length of input sequences 
    model.add(tf.keras.layers.Embedding(input_dim = input_vocab_size, output_dim = 12, input_length=num_of_words))
    # The LSTM layer learns long-term dependencies between the time steps in the time series and sequence data
    # Returns the number of layers as well as all hidden states except the last one. If we were to put false, it would only return the last output
    # which would be a 2D layer, which isn't good for the following LSTM layer. 
    model.add(tf.keras.layers.LSTM(LSTM_val, return_sequences=True))
    model.add(tf.keras.layers.LSTM(LSTM_val))
    # The Dense layer implements the operation: output = activation(dot(input,kernel)+bias). 
    # From research, the average dense units are 256~:  
    model.add(tf.keras.layers.Dense(256, activation="relu"))
    # The generated softmax activation will be dependent on the vocabulary size of the sample text. 
    model.add(tf.keras.layers.Dense(input_vocab_size, activation="softmax"))
    model.summary()
    print(model.summary())
    # Asks user for number of epoches 
    epoch_value = int(input('Enter the epoch value, remember the higher the epoch #, the higher the prediction accuracy will be!: '))
    # Asks user how many batches to input
    batch_value = int(input("Enter the batch size, remember the larger the batch size, the less time to train, but also the less accurate it will be: "))
    
    ############################### TRAINING THE MODEL #######################################
    '''
    Documentation:
    https://stackoverflow.com/questions/47902295/what-is-the-use-of-verbose-in-keras-while-validating-the-model
    https://keras.io/api/models/model/
    https://keras.io/api/callbacks/model_checkpoint/
    '''
    # Saving the model file, and the parameters are:
    # Monitor measures the model's total loss value and
    # Verbose displays progress bar. 
    # If the epoch displays a value worse than the last epoch, it will start from the better value again. 
    checkpoint = ModelCheckpoint("predicting_next.h5", monitor='loss', verbose=1, better_value=True)
    
    # Compiles the model with Adam optimizer due to quick computation times and combines properties from other 
    # optimizer, also updates data iteratively based on the training data. 
    # However, - can be replaced with optimizer of personal preference
    # Default learning rate is set to 0.001
    model.compile(loss="categorical_crossentropy", optimizer=Adam(learning_rate=0.001))
    
    # To fit the model, parameters: 
    # Passes over the input and output variables(a single tensor -- in this case pred_input, pred_output)
    # The number of epoches decided by the user 
    # The batch size decided by the user
    # Construction of callback: in this instance, the only callback needed is checkpoint
    model.fit(pred_input, pred_output, epochs=epoch_value, batch_size=batch_value, callbacks=[checkpoint])
    # Calls the create model function
Create_model()  

######################################## PREDICTION FOR MODEL  ######################################## 
"""
https://www.marktechpost.com/2019/09/13/deep-learning-with-keras-part-6-textual-data-preprocessing/
https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences
https://machinelearningknowledge.ai/keras-tokenizer-tutorial-with-examples-for-fit_on_texts-texts_to_sequences-texts_to_matrix-sequences_to_matrix/
"""
# Loads and opens the model and tokenizer
model = load_model('predicting_next.h5')
tokenizer = pickle.load(open('token.pkl', 'rb'))

# Predictive model that converts the user's input and then it predicts the next word 
# Takes three parameters: model (the last best model that was saved in the h5 file), 
# the tokenizer (the Keras library tokenizer), and the user_input(the words inputted by user)
def Predictive_Model(model, tokenizer, user_input): 
  # Tokenizes the user input from the first item (0th position) to transform the text into a series of sequences
  text_to_seq = tokenizer.texts_to_sequences([user_input])[0]
  # Uses pad_sequence from TF library to make all transformed sequences to an equivalent length using padding, and setting
  # the maximum length to be the length of the sequence that the user input in the beginning of the program. 
  text_to_seq = pad_sequences([text_to_seq], maxlen = num_of_words,truncating='pre')
  # Uses the created model from earlier that was fitted and trained via Keras library to make a prediction 
  predict_x = model.predict(text_to_seq)
  # Finds the maximum float value from the previous predictions
  pred_word_ind = np.argmax(predict_x)
  # Uses index_word(uses the index location from the dictionary to locate the next word) and tokenizes it. 
  pred_word = tokenizer.index_word[pred_word_ind]
  # Prints out and returns the previously entered words along with the new predicted word 
  print(user_input, " " ,pred_word)
  return(pred_word)


# Allows for user to input their recipe step for prediction by the model
for i in it.count():
    # Allows user to input recipe step 
    user_input = input("Enter your recipe step: ")
    # Splits the phrase the user entered by whitespace, allowing it to become individual words
    user_input = user_input.split(" ")
    # Takes the last specific number of words the user wanted for the words to be predicted. 
    # Ex: If the user wanted the sixth word to be predicted and entered more than five words,
    # it would take in the last five words entered. 
    user_input = user_input[-num_of_words:]
    # Prints the user input
    print(user_input)
    # Prints the recipe steps (dependent on how many times the user continues to input information)
    print ("Step #:", i)
    # Calls the predictive model function
    Predictive_Model(model, tokenizer, user_input)

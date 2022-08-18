#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import sys
# path where the script is executing
C_PATH = sys.argv[0]
C_PATH = C_PATH.split("/")
del C_PATH[-1]
C_PATH = "/".join(C_PATH) +"/data/"
sys.stderr.write(sys.executable+" || "+C_PATH)

from tensorflow.keras.models import load_model
import numpy as np
import pickle


# Load the model and tokenizer
model = load_model(C_PATH+'next_words.h5')
tokenizer = pickle.load(open(C_PATH+'token.pkl', 'rb'))

def Predict_Next_Words(model, tokenizer, text):

  sequence = tokenizer.texts_to_sequences([text])
  sequence = np.array(sequence)
  pd = model.predict(sequence)[0]
  preds_index = np.argpartition(pd,-5)[-5:]
  preds_values = pd[preds_index].tolist()

  preds_index = preds_index.tolist()
  
  #sort the indices based on the prediction weight
  preds_index = [x for _,x in sorted(zip(preds_values,preds_index))]
  prediction = tokenizer.sequences_to_texts([preds_index])
  
  prediction = prediction[0].split(" ")
  prediction.reverse()
  print(",".join(prediction))


while(True):
    text = input()

    try:
        text = text.strip().split(" ")
        text = text[-2:]

        Predict_Next_Words(model, tokenizer, text)

    except Exception as e:
        sys.stderr.write(e)
        print("#error#")
        continue

    sys.stdout.flush()

Our group set out to write a predictive text model for recipes using Natural Language Processing and Recurrent Neural Networks (LSTM architecture) that would predict the instructions of a typed recipe. This program can also be used for other predictive models. 


After our demo on Wednesday, we added more features to allow more of a personalized experience for the user. This is an analyzation of the result of the script: 
Here, the user chose for the predictive word to be printed after 4 words. 
You can see the words are transformed into sequences show in 5 parts: [ 1stword, 2ndword, 3rdword, 4thword, 5thword ] 

![Words to Sequences:](results/No.Word_Seq.jpeg) 

The selected numbers of layers for the LSTM layer was 1,000. 

![Model Layers:](results/ModelLayers.jpeg)

The selected number of epochs were 100 and the batch size was set to 32. 

As you can see, the initial loss value (this loss value is equivalalent the mean squared error for regression and the log loss for classification) 
was quite high: 5.618. 

![Epoch Results:](results/EpochResults.jpeg)

After the 100 epochs of 32 batch size was run, it drastically decreased to 0.0557. 
We also obtained a few almost completely accurate results: 

![A more accurate predictive result: ](results/PredictiveResults.jpeg)

And also less accurate ones depending on the overall words entered into the program: 

![Some less predictive results: ](results/PredictiveResults2.jpeg)

The results are also dependent on the sample file that the user puts in. If the dataset was smaller and contained less diverse vocabulary, then the prediction would be more accurate. Thank you for reading and we hope you enjoyed! 

___________________________________________________________________________________________________________________________________________________________

How to run the predictive text model: 
** Make sure to install the following libraries that we included in the beginning of predictivemodel.py file: Tensorflow, Keras, numpy, etc.** 
1) cd into LSTM-Predictive-Model directory
2) Run: python3 predictivemodel.py 

___________________________________________________________________________________________________________________________________________________________

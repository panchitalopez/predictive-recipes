After our demo on Wednesday, we added more features to allow more of a personalized experience for the user. Here is an analyzation of the result of the program: 


Here, the user chose for the predictive word to be printed after 4 words. 
You can see the words are transformed into sequences show in 5 parts: [ 1stword, 2ndword, 3rdword, 4thword, 5thword ] 

[! Number of Sequences](Number of Words to Sequence.jpeg) 

The selected numbers of layers for the LSTM layer was 1,000. 
The selected number of epochs were 100 and the batch size was set to 32. 

As you can see, the initial loss value (this loss value is equivalalent the mean squared error for regression and the log loss for classification) 
was quite high: 5.618. 

After the 100 epochs of 32 batch size was run, it drastically decreased to 0.0557. 

We obtained a few almost completely accurate results and also less accurate ones depending on the overall words entered into the program. 



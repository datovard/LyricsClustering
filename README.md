# LyricsClustering

This is a repo where you can find all the files used in the coding example of unsupervised tagging of song lyrics as described in the article 'Unsupervised Tagging of Spanish Lyrics Dataset
Using Clustering' by Fabio Leonardo Parra and Elizabeth León

## Files

### cleanLyrics.py

This file takes the lyrics and clean them, eliminates words with two or less characters and removes the words that are found in a banned words list. 

### processPOS.py

This file takes the files that were processed with *Part-of-Speech*(*POS*) using [Freeling Software](http://nlp.lsi.upc.edu/freeling/demo/demo.php) and creates the processed words with the frequencies that each one have in it's lyrics file

### cleanStopwords.py

This file cleans the words that have been already processed in the *Lyrics Feature Extraction* of *Part-of-Speech*(*POS*) removing all stopwords found in each lyrics file, using an standard stopwords list found in the NLTK package

### calculateTDIDF.py

This file takes every word in every document and calculates it's weights using the TD-IDF function, it creates a weight matrix in a mat file called totalWeights.mat.

![alt text](https://github.com/datovard/LyricsClustering/blob/joagranadosme/Images/equation.JPG "TD-IDF equation")

Where `tf(d)` is the number of times that term `t` appears in document `d` and `df(t)`
is the number of documents in the collection that term `t` occurs in.

## Running the .mat file

Just have to run the vcluster mode with Cluto with this command:

```
./vcluster {Path to project}/files/Weighted/totalWeights.mat 7 -clmethod=rbr -crfun=h2
```
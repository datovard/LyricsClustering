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

## Exercise

You already have the lyrics processed with a POS software, so you don't have to pre-process any lyrics with cleanLyrics.py and processPOS.py for this example.

You have to do this in order to get a test of the clustering process:

##### 1. Clean the POS processed lyrics with the cleanStopwords.py
##### 2. Got to write the TF-IDF equation into the calculateTFIDF.py file
##### 3. Get the .mat file running the calculateTFIDF.py file
##### 4. Run the clustering in Cluto with the vcluster (See below for help)
##### 5. Take the resulting file and put the clustering array into the checkBestWords.py file
##### 6. Run the checkBestWords.py file to see the clusters and you can name them as you wish!



## Running the .mat file

Just have to run the vcluster mode with Cluto with this command:

```
./vcluster {Path to project}/files/Weighted/totalWeights.mat 7 -clmethod=rbr -crfun=h2
```
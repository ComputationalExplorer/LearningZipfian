# LearningZipfian

# Objective
Observe graphically Zipf's law based on articles sampled from Wikipedia, for various languages
 
Obtain estimates for : 
 i) the proportion of the texts (cummulative word frequency) covered by the most frequent 100 words, and 
 ii) the number of words required to reach the 50% threshold

# Methodology

For each language considered : 
1) Sample randomly 1000 article titles per language.
2) Extract the text of the articles 
3) Tokenize the article into words and store them to a dictionnary for counting
4) Order the results and store the 5000 most frequent words to file, along with their count.


# Results

|Language	| First 100 words (%)	| Estimated number to cover 50%| Number unique words| 
| :---| ---	| --- | ---: | 
|English|41.8|262|38 709|
|Swedish|53.91|72|14 121|
|German|39.95|387|65 376|
|French|45.79|173|48 704|
|Russian|25.54|1 742|78 933|
|Spanish|45.17|207|45 398|
|Italian|39.86|323|51 474|
|Polish|27.12|1 314|60 572|
|Persian|41.53|227|31 501|
|Arabic|25.35|1 208|64 559|
|Czech|27.73|1 405|66 669|
|Turkish|21.62|1 387|41 099|
|Hebrew|18.86|2 136|86 149|
|Estonian|23.35|1 711|50 747|
|Hindi|64.33|25|6 414|
|Icelandic|38.03|442|38 731|
|Swahili|41.97|207|21 108|
|Mongolian|21.7|992|43 005|

# Running the code

Launch 'wiki_words.py' : Stores a sample of article names under Then generates word lists (the first 5000 are stored)

Launch 'summary_table.py' : Generates a table of the results, by language, based on the files generated by 'wiki_words.py' and stores it to the file 

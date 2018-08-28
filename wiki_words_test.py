# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 21:49:33 2018

@author: Pierre-Alexandre Tremblay
"""

import wikipedia
import itertools
from collections import defaultdict
from gensim.corpora.dictionary import Dictionary
#from nltk.tokenize import word_tokenize 
from nltk.tokenize.nist import NISTTokenizer
import nltk
nltk.download('punkt')

# For installation instructions, see : https://pypi.org/project/wikipedia/
nb_pages = 1000
min_token_size = 4
top_n_words = 5000
# 18 languages, in order of nb of wikipedia pages (as of 2018-08-21)
language_codes = ['en','sv','de','fr','ru','es','it','pl','fa','ar','cs','tr','he','et','hi','is','sw','mn'] 
langs_any_token_size = language_codes 
encoding = 'utf-8'
output_path = './results/'
nist = NISTTokenizer()

def extract_wiki_sample_article_names(language_code, nb_pages):
    filename_pages =  output_path +'sample_articles_' + language_code + '.txt'
    wikipedia.set_lang(language_code)
    
    sample_articles_names = set([]) # Build a set (of unique article names)
    while (len(sample_articles_names) < nb_pages):
        sample_articles_names |= set(wikipedia.random(pages=nb_pages)) # Union of sets
    
    sample_articles_names = list(sample_articles_names)
    outputfile_pages = open(filename_pages, 'w', encoding=encoding)
    i=0
    for name in sample_articles_names:
        i += 1
        outputfile_pages.write(str(i) + ';' + name + '\n')
        
    outputfile_pages.close()
    return sample_articles_names


def extract_tokenized_articles(articles_names, lang):
    articles = []
    for i in range(0, nb_pages):
        # Show where we're at, in case it's long
        if i % 100 == 0:
            print(i)
        
        try:
            pp = wikipedia.page(articles_names[i])
        except Exception as e:
            # Just try again (ex: if problem with disambiguation)
            continue
        
        # Tokenize and preprocess
        tokens = nist.international_tokenize(pp.content)
       # tokens = word_tokenize(pp.content)
       
        print(pp.content)
        print("Basic tokens")
        print(tokens)
        if (lang in langs_any_token_size):
            large_tokens = tokens
        else:
            large_tokens = [t for t in tokens if len(t) >= min_token_size]
        lower_tokens = [t.lower() for t in large_tokens]
        print("Lower")
        print(lower_tokens)
        alpha_only = [t for t in lower_tokens if t.isalpha()]
        print("Alpha")
        print(alpha_only)
        articles.append(alpha_only)
    return articles

def write_word_frequencies_to_file(tokenized_articles, language_code):
    # Count words using the gensim library
    dictionary = Dictionary(tokenized_articles)
    corpus = [dictionary.doc2bow(article) for article in tokenized_articles]
    
    total_word_count = defaultdict(int)
    corpus_word_count = 0
    for word_id, word_count in itertools.chain.from_iterable(corpus):
        total_word_count[word_id] += word_count
        
    corpus_word_count = sum(total_word_count.values())
    sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True) 
    
    # Write info to file
    dict_size = len(dictionary)
    cummul = 0
    idx = 1
    filename_freq = output_path + 'word_freq_' + language_code + '.txt'
    outputfile_freq = open(filename_freq, 'w', encoding=encoding)
    outputfile_freq.write('\nTotal nb of words: ' + str(dict_size) + '\n')
    for word_id, word_count in sorted_word_count[:min(top_n_words, dict_size)]:
        frac = (100 * word_count / corpus_word_count)
        cummul += frac
        output_string = str(idx) + ';'+ dictionary.get(word_id) + ';'+str(word_count)+";"+str(round(frac, 2)) +';'+ str(round(cummul, 2)) +'\n'
        outputfile_freq.write(output_string)
        idx += 1
        
    outputfile_freq.close()

# Main loop
for lang in language_codes:
    sample_articles_names = extract_wiki_sample_article_names(lang, nb_pages)
    tokenized_articles = extract_tokenized_articles(sample_articles_names, lang)
    write_word_frequencies_to_file(tokenized_articles, lang)
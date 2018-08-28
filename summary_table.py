# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 06:28:20 2018

@author: Admin
"""
from os import listdir
import csv
 
#filepath = 'C:/Users/tremp/Downloads/LearningZipfian/LearningZipfian'
output_path = './results/'
filename_freq_start = 'word_freq_'
summary_filename = 'summary.txt'

language_codes = ['en',	'sv',	'de',	'fr',	'ru',	'es',	'it',	'pl',	'ja',	'zh',	'fa',	'ar',	'cs',	'tr',	'he',	'et',	'hi',	'is',	'sw',	'mn']
languages = ['English',	'Swedish',	'German',	'French',	'Russian',	'Spanish',	'Italian',	'Polish',	'Japanese',	'Chinese',	'Persian',	'Arabic',	'Czech',	'Turkish',	'Hebrew',	'Estonian',	'Hindi',	'Icelandic',	'Swahili',	'Mongolian']

lang_dict = dict(zip(language_codes, languages))
output_dict = dict()

def number_with_thousands_space_separator(value):
    return '{:,}'.format(value).replace(',', ' ')

summary_file = open(output_path + summary_filename, 'w')
summary_file.write('|Language	| First 100 words (%)	| Estimated number to cover 50% | Number unique words| \n')
summary_file.write('| :---| ---	| --- | ---: | \n')


lang_code_pos = len(filename_freq_start)

for f in listdir(output_path):
    if (f.startswith(filename_freq_start) & f.endswith('txt')):
        
        lang_code = f[lang_code_pos:lang_code_pos+2]
        with open(output_path + f, encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter = ';')
            first100freq = 0
            estim_for_50pct = 0
            total_unique_words = 0
            idx = 0
            for row in csv_reader:
          #      print(row)
          #      print(len(row))

        #        row_split = str(row).split(';')
               # print(type(row))
            #   if (len(row) == 1):
                # Chekc for unique words count     
                if idx == 1:
                    row_split = row[0].split(':')
                    total_unique_words = int(row_split[1])
                # Check for frequencies
                if (len(row) > 3):
                    if (int(row[0]) == 100):
                        print(row)
                        first100freq = float(row[4])
                    if (float(row[4]) > 50) & (estim_for_50pct == 0):
                        estim_for_50pct = int(row[0])
               # print(row)
                idx += 1
            output_row = '|' + lang_dict[lang_code]
            output_row +=  '|' + str(first100freq)
            output_row +=  '|' + number_with_thousands_space_separator(estim_for_50pct)
            output_row +=  '|' + number_with_thousands_space_separator(total_unique_words)
            output_row += '|\n'
            output_dict[lang_code] = output_row
            
            csvfile.close();           

for lang in language_codes:
    if lang in output_dict:
        summary_file.write(output_dict[lang])
         
        
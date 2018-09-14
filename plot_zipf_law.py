# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 06:32:23 2018

@author: Pierre-Alexandre Tremblay
"""
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

# Labels
date_filename = 'zipf_data_en.csv'
fig_filename = 'zipf_law_en.png'
x_colname = 'Log10(Rank)'
y1_colname = 'Log10(Freq-OS)'
y2_colname = 'Log10(Freq-IS)'

# Get the data
word_freq_data = pd.read_csv(date_filename, sep=';')
df = word_freq_data[0:1000]
df[[x_colname, y1_colname]] = df[[x_colname, y1_colname]].apply(pd.to_numeric)

# Regressions
valid_indices = np.logical_not(np.isnan(df[y1_colname].values))
slope_oos, intercept_oos, r_value_oos, p_value_oos, std_err_oos = stats.linregress(df[x_colname].values[valid_indices], df[y1_colname].values[valid_indices])
slope_is, intercept_is, r_value_is, p_value_is, std_err_is = stats.linregress(df[x_colname].values, df[y2_colname].values)

# Draw figure
fig, ax1 = plt.subplots()
fig.set_size_inches(8, 8)

sns.regplot(x=x_colname, y=y1_colname, data = df, label = 'OoS estimates', color='b',  line_kws = {'label':"y={0:.2f}x+{1:.2f}".format(slope_oos, intercept_oos)}) 
sns.regplot(x=x_colname, y=y2_colname, data = df, label = 'IS estimates', color='r',  line_kws = {'label':"y={0:.2f}x+{1:.2f}".format(slope_is, intercept_is)}) 

ax1.set_ylabel('Log10(Freq)')
ax1.legend()
plt.show()

# Save it 
fig.savefig(fig_filename)
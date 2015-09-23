# ipython --pylab
# ipython --pylab < 62.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)

#names
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

#total_births.tail()

#total_births.plot(title='Total births by sex and year')


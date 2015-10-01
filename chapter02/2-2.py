# ipython --pylab
# 2.2 숙제. p52
# path ch02
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movielens/movies.dat', sep='::', header=None, names=mnames)

users[:5]
ratings[:5]
movies[:5]
ratings

data = pd.merge(pd.merge(ratings, users), movies)
data
data.ix[0]
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
mean_ratings[:5]
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]
active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles

mean_ratings = mean_ratings.ix[active_titles]
mean_ratings

# TODO

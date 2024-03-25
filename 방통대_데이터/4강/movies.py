import pandas as pd

movies_df = pd.read_csv("movies.csv", index_col="movieId")

print(movies_df.info())
print(movies_df.head())
print(movies_df.shape)

print(movies_df.describe())
print(movies_df['genres'].describe())

df = pd.DataFrame({'title':['My Movie (2099)'], 'genres':['Adventure']}, index = [200000])
new_movies = pd.concat([movies_df, movies_df], axis=1)

print(new_movies.info())

print(pd.melt(movies_df).head())
print(movies_df.pivot(columns='genres').tail())

print(movies_df[movies_df.genres == 'Western'])
print(movies_df[movies_df.genres.str.contains('Western')].title)



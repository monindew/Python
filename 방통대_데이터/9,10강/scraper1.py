import requests
from bs4 import BeautifulSoup
import pandas as pd


response = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250", headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(response.content, 'html.parser')

# movie_list = soup.find('ul', class_='ipc-metadata-list')
# print (movie_list.prettify())

# movie_title_list = movie_list.find_all('h3', class_='ipc-title__text')
# print (movie_title_list[0].prettify())

# movie_ratings = movie_list.find_all(class_='ipc-rating-star')
# print(movie_ratings[0].get_text())

movie_infos = soup.find_all('div', class_='cli-children')
print(movie_infos[0].prettify())

df = pd.DataFrame(columns=['rank','title', 'rating'])

i = 0
for info in movie_infos:
    rank_title = info.find('h3', class_='ipc-title__text')
    rank = rank_title.text.split('. ')[0]
    rank = int(rank)
    title = rank_title.text.split('. ')[1]
    rating = info.find(class_='ipc-rating-star').text

    df.loc[i] = [rank, title, rating]
    i += 1

print(df.head())

df.to_csv('imdb.csv')
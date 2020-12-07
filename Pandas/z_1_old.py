import pandas as pd

data = pd.read_csv('ratings.csv')
maxx = data['movieId'].max() # сколько у нас фильмов 

max_rauting_id =0 # максимальный рейтинг данного фильма (это среднее арефметическое)
max_rauting = 0 # максимальный рейтинг для сравнения (это среднее арефметическое )
max_movi = 0 # фильм с максимальным рейтингом
    
for movi in range(maxx): # ищем каждый фильм

    sort = data.query("movieId ==", movi)
    max_rauting_id = sort[["movieId"]].mean(axis=1)
    if max_rauting_id > max_rauting:
        max_rauting = max_rauting_id
        max_movi = movi
        
print ("фильм с максимальным рейтингом с id",max_movi)

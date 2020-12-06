import numpy as np
import pandas as pd
data = pd.read_csv('movies.csv', delimiter=',') # записываем из файла в DataFrame 

entry = 0           # вспомогательная переменная 
rating_data = {
'низкий рейтинг': [2],
'средний рейтинг': [4],
'высокий рейтинг': [5]
}

nmp = rating_data.to_numpy() # делаем из DataFrame массив , так удобнее

for i in range(data.shape[0]): 
    row1 = data.iloc[[i]]           # разбиваем на строки
    row2 = row1[['rating']]        # выбираем нужную нам колонку
    entry = 0                       # обнуляем переменную

    for r in range ( len(nmp) ):
        for c in range ( len(nmp[r]) ):
            
            if (row2 <= nmp[r][c] and entry == 0    ):     
                df['classs'] =  classs.apply(nmp[r][0])
                entry == 1  
            elif ( entry == 0 и row2 != nmp[2][3]): # если в самом конце последний элемент масива не подходит и до этогоо небыло вхождений , следовательно список закончен и поисковый запрос не содерэит оценки фильма
                df['classs'] = "undefined" 

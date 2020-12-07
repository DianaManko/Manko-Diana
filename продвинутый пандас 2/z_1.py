import pandas as pd

data = pd.read_csv('ratings.csv')
maxx = data['userId'].max() # сколько пользователей
time = [0]*maxx
for man in range(maxx): # идем по каждому пользователю
    
    ball=0
    
    sort = data.query("userid = ",man)      
    
    if sort.rows >= 100:
        min_time = sort[sort.userId == man and sort.timestamp == sort.timestamp.min()]
        max_time = sort[sort.userId == man and sort.timestamp == sort.timestamp.max()]
        time[man] = max_time - min_time
        
print ("средняя продолжительност ьжизни ", sum(time)/len(time))
        
    
        

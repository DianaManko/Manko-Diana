queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]
two = 0
three = 0
i=0
while i < len(queries):
    #print (queries[i])
    if len(queries[i].split()) > 2:
        three += 1
    else :
        two += 1 
    i+=1
print (' ')
print ('Поисковых запросов, содержащих 2 слов(а):',(two/len(queries))*100,'%') 
print ('Поисковых запросов, содержащих 3 слов(а):',(three/len(queries))*100,'%')

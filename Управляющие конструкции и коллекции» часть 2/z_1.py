ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}
user_1 = ids ['user1']
set_res_1 = set(user_1) 
print("Результат",end = " : { ") 
list_res_1 = (list(set_res_1))
for item_1 in list_res_1: 
    print(item_1,end = ", ")
user_2 = ids ['user2']
set_res_2 = set(user_2)  
list_res_2 = (list(set_res_2))
for item_2 in list_res_2: 
    print(item_2,end = ", ")
user_3 = ids ['user3']
set_res_3 = set(user_3) 
list_res_3 = (list(set_res_3))
for item_3 in list_res_3: 
    print(item_3,end = ", ")
print ('}')



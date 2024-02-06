'''
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
'''
import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

# var.1
lst_r = []
lst_h = []
for element in lst:
    if element == 'robot':
        lst_r.append(1)
        lst_h.append(0)
    else:
        lst_h.append(1)
        lst_r.append(0)

if list[0] == 'robot':
    md = {'robot': lst_r, 'human': lst_h}
else:
    md = {'human': lst_h, 'robot': lst_r}

onehot_data = pd.DataFrame(md)
print()
print(onehot_data)
print()

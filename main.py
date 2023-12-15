# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

# С использованием get_dummies
print(f'\n{"-"*20} One Hot c get_dummies {"-"*20}\n')
print(pd.get_dummies(data, dtype=int).rename(columns={'whoAmI_human': 'human', 'whoAmI_robot': 'robot'}))

# Без использования get_dummies
print(f'\n{"-"*20} One Hot без get_dummies {"-"*20}\n')
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
data.fillna(0, inplace=True)
data[['human', 'robot']] = data[['human', 'robot']].astype(int)
data.drop('whoAmI', axis=1, inplace=True)
print(data)

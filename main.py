import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(f'{data}\n')
data.loc[data['whoAmI'] == 'human', 'human'] = '1'
data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
data.fillna(value='0', inplace=True)
del data['whoAmI']
print(data)
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
data = pd.DataFrame({'whoAmI':lst})

one_hot_data = pd.DataFrame(data=data, columns=['human', 'robot'])
one_hot_data.loc[data['whoAmI'] == 'human', 'human'] = True
one_hot_data.loc[data['whoAmI'] != 'human', 'human'] = False
one_hot_data.loc[data['whoAmI'] == 'robot', 'robot'] = True
one_hot_data.loc[data['whoAmI'] != 'robot', 'robot'] = False
print(one_hot_data)
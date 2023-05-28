import pandas as pd
purchases = pd.read_csv('/datasets/returned.csv')
purchases['total'] = purchases['first'] + purchases['repeated']
purchases['repeated_share'] = purchases['repeated'] / purchases['total']
purchases = purchases.sort_values('repeated_share', ascending=False)
print(purchases.sort_values('repeated_share', ascending=False))
# print(purchases)
# User ID и куки

import pandas as pd
logs = pd.read_csv('/datasets/logs.csv')
print(logs.head())

import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
print('Уникальных email:', len(logs.email.unique()))
print('Уникальных User ID:', len(logs.user_id.unique()))

import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

print(logs.source.unique())

#Вы обнаружили NaN и None
import pandas as pd

hogwarts_points = pd.read_csv('/datasets/hogwarts_points.csv')
hogwarts_points = hogwarts_points.fillna('Гриффиндор')
print(hogwarts_points)

import pandas as pd

hogwarts_points = pd.read_csv('/datasets/hogwarts_points.csv')
hogwarts_points['faculty_name'] = hogwarts_points['faculty_name'].fillna(value='Гриффиндор')
print('Сумма баллов учеников:', hogwarts_points.points.sum())# сумма значений столбца 'points'
print('Сумма баллов факультетов:', hogwarts_points.groupby('faculty_name').points.sum().sum())# сгруппируйте по столбцу 'faculty_name'
# сложите значения столбца 'points' этой группировки методом sum()
# и примените метод sum() к результату
print('Кубок получает', hogwarts_points.groupby('faculty_name')['points'].sum().idxmax())


import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['user_id'].count()#общее количество визитов из каждого источника
print(visits)

import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['user_id'].count() # количество визитов
purchase = logs.groupby('source')['purchase'].sum() # количество покупок

conversion = purchase / visits# поделите количество покупок на количество визитов
print(conversion)
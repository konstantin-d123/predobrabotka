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
purchase = logs.groupby('source')['purchase'].sum()# количество покупок для каждого источника
print(purchase)

import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')

visits = logs.groupby('source')['user_id'].count() # количество визитов
purchase = logs.groupby('source')['purchase'].sum() # количество покупок

conversion = purchase / visits# поделите количество покупок на количество визитов
print(conversion)

#Логические выражения в атрибуте loc
import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

rows = data['Новая функция'] == '+'
print(data.loc[rows])


import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
rows = data['Статья'] == '+'
print(data.loc[rows])

import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

print(data.loc[data['Новая функция'] == '+', 'Имя'])

import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

data.loc[data['Эксперимент'] == '+', 'Роль'] = 'экспериментатор'
print(data)


import pandas as pd

data = pd.read_csv('/datasets/projects.csv')
# print(data)
print(data.loc[data['Эксперимент'] == '+', 'Имя'])
# print(data.loc[data['Новая функция'] == '+', 'Имя'])

import pandas as pd

data = pd.read_csv('/datasets/projects.csv')

data.loc[data['Новая функция'] != '+', 'Новая функция'] = '-'
print(data)

#Работа с пропусками в категориальных переменных
import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']}) #запишите ваш код сюда
print(logs_grouped)

import pandas as pd

logs = pd.read_csv('/datasets/logs.csv')
logs['email'] = logs['email'].fillna(value='')
logs.loc[logs['source'] == 'None', 'source'] = 'email'

logs_grouped = logs.groupby('source').agg({'purchase': ['count', 'sum']})

logs_grouped['conversion'] = logs_grouped['purchase']['sum'] / logs_grouped['purchase']['count']
print(logs_grouped)

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')
age_avg = metrica['age'].mean()
metrica.age=metrica.age.fillna(age_avg)
print(metrica.head(10))

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')
time_avg = metrica.time.mean()#запишите среднее время просмотра
print(time_avg)

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')
desktop_data = metrica.loc[metrica.device_type == 'desktop']
#print(desktop_data.head())
desktop_data_time_avg=desktop_data.time.mean()
print(desktop_data_time_avg)
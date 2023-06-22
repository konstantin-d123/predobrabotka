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

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')

desktop_data = metrica[metrica.device_type=='desktop']

print(desktop_data.head(5))

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')

mobile_data = metrica[metrica.device_type=='mobile']

print(mobile_data.head(5))

import pandas as pd

metrica = pd.read_csv('/datasets/metrica_data.csv')

mobile_data = metrica[metrica.device_type=='mobile']

mobile_data_time_avg=mobile_data.time.mean()
print(mobile_data_time_avg)

import pandas as pd

data = pd.read_excel(
    '/datasets/seo_data.xlsx', sheet_name='traffic_data'
)

print(data.head())

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')

print(data.source.unique())

import pandas as pd

subcategory_dict = pd.read_excel(
    '/datasets/seo_data.xlsx', sheet_name='subcategory_ids'
)

print(subcategory_dict.head())

import pandas as pd

category_dict = pd.read_excel(
    '/datasets/seo_data.xlsx', sheet_name='category_ids'
)

print(category_dict.head())

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data.info()

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
pd.to_numeric(transactions.id)

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions.id = pd.to_numeric(transactions.id, errors='coerce')

print(transactions.tail())

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')
transactions.info()

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')

transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

transactions.info()

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')

print(transactions.amount.sum())

import pandas as pd

transactions = pd.read_excel('/datasets/ids.xlsx')
transactions['id'] = pd.to_numeric(transactions['id'], errors='coerce')
transactions['amount'] = pd.to_numeric(transactions['amount'], errors='coerce')
transactions_per_category = transactions .groupby('category')['amount'].sum() # Рассчитайте сумму продаж для каждой категории
print(transactions_per_category)

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')

print(data.loc[964,:])

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')

print('Количество строк:', data.shape[0])
print(data[data['subcategory_id'] == 'total'])

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data = data[data['subcategory_id'] != 'total']
print(data[data['subcategory_id'] == 'total'])

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data = data[(data['subcategory_id'] != 'total')]
data['visits'] = pd.to_numeric(data['visits']).astype('int')
data.info()

import pandas as pd

data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
data = data[(data['subcategory_id'] != 'total')]
data['visits'] = data['visits'].astype('int')
print(data.groupby('source')['visits'].sum())

#Методы Pandas для работы с датой и временем
import pandas as pd

position = pd.read_csv('/datasets/position.csv')

print(position.head(15))

import pandas as pd

position = pd.read_csv('/datasets/position.csv')

position.info()

import pandas as pd

position = pd.read_csv('/datasets/position.csv')

position['timestamp'] = pd.to_datetime(
    position['timestamp'],
    format='%Y-%m-%dT%H:%M:%S'
)
print(position.head())

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(position['timestamp'], format='%Y-%m-%dT%H:%M:%S')

position.info()

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(
    position['timestamp'], format='%Y-%m-%dT%H:%M:%S'
)

print(position.sort_values(by='level', ascending=False))

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(
    position['timestamp'], format='%Y-%m-%dT%H:%M:%S'
)

position['month'] = pd.DatetimeIndex(position['timestamp']).month
print(position.head())

import pandas as pd

position = pd.read_csv('/datasets/position.csv')
position['timestamp'] = pd.to_datetime(
    position['timestamp'], format='%Y-%m-%dT%H:%M:%S'
)
position['month'] = pd.DatetimeIndex(position['timestamp']).month
print(position.groupby('month')['level'].mean())

position = [
    ['2019-05-01', '6'],
    ['2019-05-02', '5'],
    ['2019-05-03', '5'],
    ['2019-05-04', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', '4'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]
count_lines = 0

for row in position:
    count_lines =  count_lines+1# допишите ваш код здесь
print(count_lines)


position = [
    ['2019-05-01', '6'],
    ['2019-05-02', '5'],
    ['2019-05-03', '5'],
    ['2019-05-04', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', '4'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]

count_lines = 0
total_position = 0

for row in position:
    count_lines += 1
    level = int(row[1]) #в этой переменной сохраните позицию в выдаче
    total_position = total_position + level#сложите все позиции в этой переменной
print(total_position / count_lines)

position = [
    ['2019-05-01', '- 6'],
    ['2019-05-02', '+5'],
    ['2019-05-03', ' 5'],
    ['2019-05-04', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', 'Error 5'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]
count_lines = 0
total_position = 0

for row in position:
        count_lines += 1
        level = int(row[1]) #в этой переменной сохраните позицию в выдаче
        total_position += level #сложите все позиции в этой переменной
print(total_position / len(position))

position = [
    ['2019-05-01', '- 6'],
    ['2019-05-02', '+5'],
    ['2019-05-03', ' 5'],
    ['2019-05-04', '4'],
    ['2019-05-05', '5'],
    ['2019-05-06', '5'],
    ['2019-05-07', '4'],
    ['2019-05-08', 'Error 5'],
    ['2019-05-09', '3'],
    ['2019-05-10', '3'],
]

count_lines = 0
wrong_lines_content = []

for row in position:
    try:
        count_lines += 1
        level = int(row[1])

    except:
        wrong_lines_content.append(row)
print('Количество измерений', count_lines)
print('Некорректные строки', wrong_lines_content)

#Метод merge()
import pandas as pd
data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids')
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')
print(data_subcategory.head(10))

import pandas as pd
data = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='subcategory_ids')
category_dict = pd.read_excel('/datasets/seo_data.xlsx', sheet_name='category_ids')
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')
data_final = data_subcategory.merge(category_dict, on='category_id', how='left')
print(data_final.head(10))

# Сводные таблицы
import pandas as pd
data_final = pd.read_csv('/datasets/data_final.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
print(data_pivot.head(10))

import pandas as pd
data_final = pd.read_csv('/datasets/data_final.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']
print(data_pivot.head(10))

import pandas as pd
data_final = pd.read_csv('/datasets/data_final.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

print(data_pivot.sort_values(by='ratio', ascending=False).head(10))

import pandas as pd
data_final = pd.read_csv('/datasets/data_final.csv')
data_pivot = data_final.pivot_table(index=['category_name', 'subcategory_name'], columns='source', values='visits', aggfunc='sum')
data_pivot['ratio'] = data_pivot['organic'] / data_pivot['direct']

print(data_pivot.sort_values(by='ratio', ascending=False).tail(10))

#Лаборатория ручного поиска дубликатов
import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
# ваш код здесь
print(stock['item'].duplicated().sum())


import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
print(stock['item'].value_counts())

import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')

xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock =  stock.drop_duplicates (subset=['item'], keep='first')# удалите строки с дубликатами в столбце 'item'
# выведите всю таблицу stock на экран
print(stock)

import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')

xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock = stock.drop_duplicates(subset=['item'], keep='first')
stock = stock.reset_index(drop=True)  # восстановите индексы с помощью reset_index(drop=True)
# выведите stock на экран
print(stock)

import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock = stock.drop_duplicates(subset=['item'], keep='first')
stock = stock.reset_index(drop=True)

# замените значение в ячейке с количеством смартфонов Xiaomi
stock.loc[0, 'count'] = xiaomi
# выведите таблицу stock на экран
print(stock)

import pandas as pd

stock = pd.read_excel('/datasets/stock.xlsx', sheet_name='storehouse')
xiaomi = stock[stock['item'] == 'Смартфон Xiaomi Redmi 6A 16GB']['count'].sum()
huawei = stock[stock['item'] == 'Смартфон HUAWEI P30 lite']['count'].sum()

stock = stock.drop_duplicates(subset=['item'], keep='first')
stock = stock.reset_index(drop=True)

stock.loc[0, 'count'] = xiaomi
# замените значение в ячейке с количеством смартфонов Huawei
stock.loc[3, 'count'] = huawei
# выведите таблицу stock на экран
print(stock)

import pandas as pd

support = pd.read_csv('/datasets/support.csv')
print(support.head(10))
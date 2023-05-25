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
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt # some imports to set up plotting
data=pd.read_excel('trainingbase50000_clear.xlsx')
UK=data[data['Country']=='United Kingdom']
nonUK=data[data['Country']!='United Kingdom']
print(data.groupby(['Country']).count())
# График англии и других стран
# fig, ax = plt.subplots()
# ax.bar((1,2),(len(UK),len(nonUK)))
# ax.set_facecolor('seashell')
# fig.set_facecolor('floralwhite')
# for axis in [ax.xaxis, ax.yaxis]:
#     axis.set_major_locator(ticker.MaxNLocator(integer=True))
# ax.set_xlabel('Англия и другие страны')
# ax.set_ylabel('Количество заказов')
# plt.title('Количество заказов в разных странах')
# plt.show()
# l=data[(data['Country'] == 'France')|(data['Country'] == 'EIRE')|(data['Country'] == 'Germany')| (data['Country'] == 'Spain')|(data['Country'] == 'Belgium')]
# print(l)
# print(data.dtypes)
# print(data.info)
# data.rename(columns={'Unnamed: 0':'firstnumber'},inplace=True)
# del data['firstnumber']
# print(data.columns)
# print(data.describe())
# list_of_countries=data['Country'].unique()
data['ordersum']=data['Quantity']*data['UnitPrice']
s=(data['ordersum'].describe() & data['Country']=='United kingdom')
z=(data['ordersum'].describe & data['Country']!='United kingdom')
print(type(s))
# fig, ax = plt.subplots()
# ax.bar((1,2),(len(s),len(z)))
# ax.set_facecolor('seashell')
# fig.set_facecolor('floralwhite')
# for axis in [ax.xaxis, ax.yaxis]:
#     axis.set_major_locator(ticker.MaxNLocator(integer=True))
# ax.set_xlabel('Англия и другие страны')
# ax.set_ylabel('Сумма заказов')
# plt.title('сортиросвка по сумме заказов')
# plt.show()
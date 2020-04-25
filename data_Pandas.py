import pandas as pd

dataframe = pd.read_csv('datos.csv')
filtro = dataframe['SALARIO']>1500
dataframe2 = dataframe[filtro]
array = dataframe2.values

print(dataframe)
print(dataframe.describe())
print(dataframe[['NOMBRE','APELLIDOS']])
print(dataframe['SALARIO']>1500)
print(dataframe2)
print(dataframe2.values)
print(array)
print(array[(0,0),(0,1)])

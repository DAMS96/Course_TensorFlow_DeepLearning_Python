import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

datos = np.random.randint(0,100,(100,4))
dataframe = pd.DataFrame(data = datos, columns =['c1','c2','c3','etiqueta'])
x = dataframe[['c1','c2','c3']]
y = dataframe['etiqueta']

#Entrenamiento
#dividir un conjunto de datos de Entrenamiento y test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)
# print(datos)
# print(dataframe)
print(x)
print(y)
print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print(y_test.shape)

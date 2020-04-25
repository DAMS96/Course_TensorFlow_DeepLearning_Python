import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = (0,1,2,3,4,5,6,7,8)
# y = (0,1,2,3,4,5,6,7,8)
# plt.plot(x,y,'g*')
# plt.title('TItulo del grafico')
# plt.xlabel('eje de los valores x')
# plt.ylabel('eje de los valores y')
# plt.show()

array = np.arange(0,50).reshape(10,5)
print(array)
plt.imshow(array)
plt.colorbar()
plt.show()

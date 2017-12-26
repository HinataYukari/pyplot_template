import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display

#reading data
data_1 = pd.read_csv('score1.csv')
data_2 = pd.read_csv('score2.csv')
data_3 = pd.read_csv('score3.csv')

'''
display(df)
'''

#x_axis
x = data_1.iloc[:,0].astype(int)
#y_axis
y1 = data_1.iloc[:,1].astype(float)
y2 = data_2.iloc[:,1].astype(float)
y3 = data_3.iloc[:,1].astype(float)

#ideal curve (y = ax^3)
xlast = x[len(x)-1]
ylast = yc[len(yc)-1]
k = ylast / (xlast ** 3)
x_new = np.arange(0, xlast, 10)
y_ideal = (np.array(x_new)**3)*k


plt.plot(x, y1, 'co', label = "Datapoint")
plt.plot(x_new, y_ideal, label = "$y = kx^3(k = {})$".format(k), color = 'm', linestyle = '-')

#two graphs
plt.figure(figsize = (10,6))

#first graph
plt.subplot(121)
y11 = data_1.iloc[:,1].astype(float)
y21 = data_2.iloc[:,1].astype(float)
y31 = data_3.iloc[:,1].astype(float)

plt.xlabel("x")
plt.ylabel("y")
plt.title("first")
plt.legend()

#second graph (log scale)
plt.subplot(122)
plt.xscale("log")
y12 = data_1.iloc[:,2].astype(float)
y22 = data_2.iloc[:,2].astype(float)
y32 = data_3.iloc[:,2].astype(float)

plt.plot(x,y12, label = "Method 1")
plt.plot(x,y22, label = "Method 2")
plt.plot(x,y32, label = "Method 3")

plt.xlabel("x'")
plt.ylabel("y'")
plt.title("second")
plt.legend()

#saving image
plt.savefig("matrix_c.png",format = 'png', dpi=300)
plt.show()

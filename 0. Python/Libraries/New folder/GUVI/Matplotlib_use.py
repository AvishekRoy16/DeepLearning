import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
x = np.random.random((10,1))
print(x)

#plt.plot(x)
#plt.plot(x,'*')
plt.plot(x,'*-')
plt.show()

x = np.linspace(0, 10, 100)
y = np.power(x, 0.5)
plt.plot(x,y)
plt.show()

sns.set()
sns.lineplot(x,y)
plt.show()

data = pd.read_csv('survey.csv')
print(data.head())

#ax = sns.scatterplot(x = "year", y = "value", data=data)
#plt.show()




#import scipy as sp
import matplotlib.pylot as plt

import pandas as pd
data=pd.read_csv("scratch3.csv")
data['bedrooms'].value_counts().plot(kind='bar')
plt.title('number of bedrooms')
plt.xlabel('bedrooms')
plt.ylabel('count')
plt.show()

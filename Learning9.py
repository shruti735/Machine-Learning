import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
data = sp.genfromtxt("Scatterdatafile.tsv", delimiter="\t")
print(data)
print(data.shape)
x = data[:, 0]
y = data[:, 1]
fp1 = 11
fp2 = 22
np.mean(x)
np.mean(y)
f1 = sp.poly1d(fp1)
fx = sp.linspace(0,x[-1],1000)
plt.plot(fx,f1(fx),linewidth=4)
plt.legend(["d=%i" % f1.order],loc ="upper left")
f2 = sp.poly1d(fp2)
fx = sp.linspace(0,x[-1],1000)
plt.plot(fx,f2(fx),linewidth=4)
plt.legend(["d=%i" % f2.order],loc ="upper right")
plt.scatter(x,y)
plt.title("WEb T")
plt.xlabel("Time")
plt.ylabel("Hits")
plt.xticks()
plt.autoscale(tight=True)
plt.grid()
plt.show()
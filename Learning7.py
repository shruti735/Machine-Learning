import matplotlib.pyplot as plt
import scipy as sp
data = sp.genfromtxt("Webtraffic2.tsv", delimiter="\t")
print(data)
print(data.shape)
x = data[:, 0]
y = data[:, 1]
plt.scatter(x,y)
plt.title("WEb T")
plt.xlabel("Time")
plt.ylabel("Hits")
plt.xticks()
plt.autoscale(tight=True)
plt.grid()
plt.show()
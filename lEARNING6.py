import scipy as sp
data = sp.genfromtxt("Webtraffic2.tsv", delimiter="\t")
print(data)
print(data.shape)
x = data[:, 0]
y = data[:, 1]
print(x)
print(y)
print(sp.sum(sp.isnan(y)))
x1= x[~sp.isnan(x)]
y1= y[~sp.isnan(y)]
print(x1)
print(y1)
#data santization
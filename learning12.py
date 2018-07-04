#descrptive linear reg
#estimate mean variance

#cal list of no
def mean(values):
    return sum(values) / float(len(values))

#cal variance
def variance(values, mean):
    return sum([(x - mean) * 2 for x in values])

#cal covariance
def covariance(x, mean_x,y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

#calculate mean & variance
dataset = [[1,1],[2,3],[4,3],[3,2],[5,5]]
x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
mean_x , mean_y = mean(x), mean(y)
var_x,var_y = variance(x, mean_x), variance(y, mean_y)
print('x stats : mean =%.3f variance =%.3f' % (mean_x,mean_x))
print('y stats : mean =%.3f variance =%.3f' % (mean_y,mean_y))

covar = covariance(x, mean_x,y,mean_y)
print('covariance : %.3f' % (covar))




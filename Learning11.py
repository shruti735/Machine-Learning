import numpy as np
import matplotlib.pyplot as plt
def estimate_coef(x,y):
    print(x)
    print(y)
    n = np.size(x)
    print("Size - ",n)
    m_x, m_y = np.mean(x), np.mean(y)
    print("Mean x- ",m_x,"Mean y - ",m_y)
    SS_xx = np.sum(y * x - n * m_y *m_x)
    SS_xy = np.sum(x * x - n * m_x * m_x)
    print(SS_xx)
    print(SS_xy)
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 *m_x

    return b_0,b_1
#regression coeff

def plot_regression_line(x,y,b): #actual point
    plt.scatter(x,y,color="m",marker = "o", s=30)
    #predicted response vector
    y_pred = b[0] + b[1] * x
    #reg line plot
    plt.plot(x,y_pred,color = "g")
    #putting labels

    plt.xlabel('x')
    plt.ylabel('y')

    #func to show plot
    plt.show()

def main():
    #observations
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])

    #estimated coeff

    b = estimate_coef(x,y)
    print("estimated coeff are - \nb_0 ={} \
          \nb_1 = {}".format(b[0],b[1]))

    #plot reg line
    plot_regression_line(x,y,b)

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
def TriangularDistribution(a, b, c, data):
    # TODO
    pdf = [0]*len(data)
    for i in range(len(data)):
        if data[i] < a:
            pdf[i] = 0
        elif data[i] < c:
            pdf[i] = 2*(data[i]-a)/((b-a)*(c-a))
        elif data[i] == c:
            pdf[i] = 2/(b-a)
        elif data[i] <= b:
            pdf[i] = 2*(b-data[i])/((b-a)*(b-c))
        else:
            pdf[i] = 0
    cdf = [0]*len(data)
    for i in range(len(data)):
        if data[i] <= a:
            cdf[i] = 0
        elif data[i] <= c:
            cdf[i] = (data[i]-a)**2/((b-a)*(c-a))
        elif data[i] < b:
            cdf[i] = 1-(b-data[i])**2/((b-a)*(b-c))
        else:
            cdf[i] = 1
    mean = (a+b+c)/3
    variance = (a**2+b**2+c**2-a*b-a*c-b*c)/18
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Triangular Distribution')
    axs[0].plot(data, pdf, marker='o')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('Probability')
    axs[1].plot(data, cdf, marker='*')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('Cumulative Probability')
    plt.show()
    plt.savefig('triangular_distribution.svg', format='svg')
    return (mean, variance)
a = 100
b = 50000
c = 20000
data = range(1, 60001)
result = TriangularDistribution(a, b, c, data)
print(result)
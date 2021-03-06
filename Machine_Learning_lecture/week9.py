import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

data = pd.read_csv('./ML_week9_data.csv')

class LinearRegression: 
    def fit(self, X, Y):
        X = np.array(X).reshape(1, -1);
        Y = np.array(Y).reshape(1, -1);
        x_shape = X.shape
        num_var = x_shape[0]
        self.weight = np.random.normal(0, 1, (num_var, 1))
        self.bias = np.random.rand(1)
        self.num_iteration = 50

        for t in range(self.num_iteration):
            N = x_shape[1]
            self.delta_W = 2/N * (np.sum(np.multiply(((np.matmul(self.weight, X) + self.bias) - Y), X)))
            self.delta_bias = 2/N * (np.sum(((np.matmul(self.weight, X) + self.bias) - Y)))
            self.weight -= 0.1 * self.delta_W
            self.bias -= 0.1 * self.delta_bias
        return self.weight, self.bias

    def predict(self, X):
        print(self.weight)
        product = np.matmul(self.weight, np.array(X).reshape(1, -1)) + self.bias
        return product.reshape(-1)

    
reg = LinearRegression()

x = (data['Weight'] - data['Weight'].mean()) / data['Weight'].std()
y = (data['Height'] - data['Height'].mean()) / data['Height'].std()

'''
x = (data['Weight'] - data['Weight'].min()) / (data['Weight'].max() - data['Weight'].min())
y = (data['Height'] - data['Height'].min()) / (data['Height'].max() - data['Height'].min())
'''

params = reg.fit(x[:-180], y[:-180])
pred = reg.predict(np.array(x[-180:]))

plt.scatter(x[-180:], y[-180:])
plt.plot(x[-180:], pred, 'red')
#plt.text(0.35, 0.08, 'gradient, min-max, iteration: 50')
#plt.savefig('gradient_min-max_iteration_50.png')
plt.text(-0.65, -2.6, 'gradient, Z-score, iteration: 50')
#plt.savefig('gradient_Z-score_iteration_50.png')
import numpy as np
import matplotlib.pyplot as plt

def gradiend_descent(X_array, Y_array, y_predict):
	partial_derivative_1 = sum(y_predict - Y_array)
	partial_derivative_2 = sum(X_array * (y_predict - Y_array))
		
	return partial_derivative_1, partial_derivative_2

def linear_regression(X_array, Y_array):
	teta_1 = 10
	teta_2 = 10
	gama = 0.0001
	epsilon = 1
	i = 0
	while i < 1000 and epsilon > gama: 
		y_predict = (teta_2 * X_array) + teta_1
		partial_derivative_1, partial_derivative_2 = gradiend_descent	(X_array, Y_array, y_predict)
		
		teta_1 = teta_1 - gama * partial_derivative_1
		teta_2 = teta_2 - gama * partial_derivative_2
		
		cost_error = cost(Y_array, y_predict)
		epsilon = max(abs(partial_derivative_1), abs(partial_derivative_2))
		print(f'Cost {i}: {cost_error}')
		print(f'Epsilon {i}: {epsilon}')
		i += 1
		
	return teta_1, teta_2
	
def cost(Y_array, y_predict):
	cost = np.sum((y_predict - Y_array)**2)
	return cost

def display(X_array,Y_array, x_points, y_points):
	plt.plot(x_points ,y_points)
	plt.scatter(X_array, Y_array, color="red")
	plt.show()
	
def function(x_points, teta_1, teta_2):
	result = teta_1 + teta_2 * x_points
	return result
	
	
def main():
	data = np.load('XYdata.npz')
	X_array, Y_array = data['array_1'], data['array_2']

	teta_1, teta_2 = linear_regression(X_array, Y_array)
	print("teta 1:", teta_1, "teta 2:", teta_2)
	
	x_points = np.linspace(-1, 11, 50)
	y_points = function(x_points, teta_1, teta_2)
	display(X_array, Y_array, x_points ,y_points)
	
	
if __name__ == "__main__":
    main()


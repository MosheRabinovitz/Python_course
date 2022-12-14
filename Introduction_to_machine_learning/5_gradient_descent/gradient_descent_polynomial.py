import numpy as np
import matplotlib.pyplot as plt

#Calculating the values of the gradients
def gradient_descent(X_array, Y_array, y_predict):
	partial_derivative_1 = sum(y_predict - Y_array)
	partial_derivative_2 = sum(X_array * (y_predict - Y_array))
	partial_derivative_3 = sum((X_array **2) * (y_predict - Y_array))
		
	return partial_derivative_1, partial_derivative_2, partial_derivative_3


#Algorithm for Gradient Descent
def polynomial_regression(X_array, Y_array):
	#Initializing teta, learning rate and epsilon
	teta_1 = 10
	teta_2 = 10
	teta_3 = 10
	learning_rate = 0.0001
	epsilon = 1
	
	i = 0
	while i < 20000 and epsilon > learning_rate: 
		y_predict = (teta_3 * X_array **2) + (teta_2 * X_array) + teta_1
		partial_derivative_1, partial_derivative_2, partial_derivative_3 = gradient_descent(X_array, Y_array, y_predict)
		
		teta_1 = teta_1 - learning_rate * partial_derivative_1 * 2/len(X_array)
		teta_2 = teta_2 - learning_rate * partial_derivative_2 * 2/len(X_array)
		teta_3 = teta_3 - learning_rate * partial_derivative_3 * 2/len(X_array)
		
		cost_error = cost(Y_array, y_predict)
		epsilon = max(abs(partial_derivative_1), abs(partial_derivative_2), abs(partial_derivative_3))
		print(f'Cost {i}: {cost_error}')
		print(f'Epsilon {i}: {epsilon}')
		i += 1
		
	return teta_1, teta_2, teta_3


# Calculating the loss or cost
def cost(Y_array, y_predict):
	cost = sum((y_predict - Y_array)**2)
	return cost


# Plotting the original points and the regression line
def display(X_array, Y_array, x_array, y_array):
	plt.plot(x_array, y_array)
	plt.scatter(X_array, Y_array, color="red")
	plt.show()


# Calculate the values of the y_coordinates according to teta we received in the polynomisl_regression
def function(array, teta_1, teta_2, teta_3):
	result = np.zeros(len(array))
	result = teta_1 + teta_2 * array + teta_3 * array ** 2
	return result
	
	
def main():
	data = np.load('XYdata.npz')
	X_array, Y_array = data['array_1'], data['array_2']

	teta_1, teta_2, teta_3 = polynomial_regression(X_array, Y_array)
	print("teta 1:", teta_1, "teta 2:", teta_2, "teta 3:", teta_3)
	
	#crate new points to get the regression line
	x_array = np.linspace(0, 10, 50)
	y_array = function(x_array, teta_1, teta_2, teta_3)
	
	display(X_array, Y_array, x_array, y_array)
	
	
if __name__ == "__main__":
    main()


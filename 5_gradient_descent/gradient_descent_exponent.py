import math
import numpy as np
import matplotlib.pyplot as plt


#Calculating the vector of the gradients
def gradient_descent(X_array, Y_array, y_predicted):
	partial_derivative = np.zeros(2)
	for i in range(2):
		partial_derivative[i] = sum((X_array **i) * (y_predicted - Y_array) * 2/len(X_array))
	return partial_derivative


# Reduce the exponent to polynomial function
def exponent_regrision(X_array, Y_array):
	min_y = min(Y_array)	
	Y_array += abs(min_y) +2 if min_y < 0 else 0

	#log_y_array = np.log(Y_array)
	
	iterations = int(input("Enter number for iterations: "))
	teta = polynomial_regression(X_array, Y_array, iterations)
	
	return teta, min_y


#Algorithm for Gradient Descent
def polynomial_regression(X_array, Y_array, iterations=2000):

	#Initializing teta, learning rate ,epsilon and iterations
	teta = np.array([1] * 2)
	learning_rate = 10**-5
	epsilon = 1
	iterations = iterations
	
	i = 0
	while i < iterations and epsilon > learning_rate: 
		y_predicted = np.zeros(len(X_array))
		for j in range(2):
			y_predicted += teta[j] * X_array **j
		partial_derivative = gradient_descent(X_array, Y_array, y_predicted)
		teta = teta - learning_rate * partial_derivative
		
		error_cost = cost(Y_array, y_predicted)
		epsilon = max(abs(partial_derivative))
		coefficient = coefficient_of_determination(Y_array, y_predicted)
		# Printing the parameters for each iteration
		print(f'Cost {i}: {error_cost}')
		print(f'Epsilon {i}: {epsilon}')
		print(f'coefficient_of_determination: {coefficient}')
		
		i += 1
	
	return teta


# Calculating the loss or cost
def cost(Y_array, y_predicted):
	cost = sum(2/len(Y_array) * (y_predicted - Y_array)**2)
	return cost


#Calculate the Coefficient of Determination
def coefficient_of_determination(Y_array, y_predicted):
	mean = np.mean(Y_array)
	ss_res = sum((Y_array - y_predicted)**2)
	ss__tot = sum((Y_array - mean)**2)
	coefficient_of_determination = 1 - ss_res/ss__tot
	return coefficient_of_determination


# Plotting the original points and the regression line
def display(X_array, Y_array, x_array, y_array):
	plt.plot(x_array, y_array, color="black", linewidth=2)
	plt.scatter(X_array, Y_array, color="red")
	plt.xticks()
	plt.yticks()
	plt.show()


# Calculate and convert to exponent function the values of the y_coordinates according to teta_vactor we received in the polynomisl_regression
def exp_function(array, teta, x):
	result = np.zeros(len(array))
	for j in range(len(array)):
		for i in range(len(teta)):
			result[j] += np.exp(teta[i] * array[j]**i)
		result[j] -= x
	return result


def main():
	data = np.load('XYdata.npz')
	X_array, Y_array = data['array_1'], data['array_2']
	teta, x = exponent_regrision(X_array, Y_array)
	
	for i in range(len(teta)):
		print(f"teta {i}: {teta[i]}", end=", ")
	
	#crate new points to get the regression line
	x_array = np.linspace(0, 10, 100)
	y_array = exp_function(x_array, teta, x)
	
	display(X_array, Y_array, x_array, y_array)
	
	
if __name__ == "__main__":
    main()


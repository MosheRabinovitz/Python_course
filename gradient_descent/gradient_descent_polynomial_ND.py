import numpy as np
import matplotlib.pyplot as plt

ORDER = int(input("Enter number for ORDER of the function: "))


#Calculating the vector of the gradients
def gradient_descent(X_array, Y_array, y_predicted, ORDER):
	partial_derivative = np.zeros(ORDER)
	for i in range(ORDER):
		partial_derivative[i] = sum((X_array **i) * (y_predicted - Y_array))
	return partial_derivative


#Algorithm for Gradient Descent
def polynomisl_regression(X_array, Y_array, ORDER, iterations=2000, learning_rate=0.0000000001):

	#Initializing teta, learning rate ,epsilon and iterations
	teta = np.array([1] * ORDER)
	learning_rate = learning_rate
	epsilon = 1
	iterations = iterations
	
	i = 0
	while i < iterations and epsilon > learning_rate: 
		y_predicted = np.zeros(len(X_array))
		for j in range(ORDER):
			y_predicted += teta[j] * X_array **j
		partial_derivative = gradient_descent(X_array, Y_array, y_predicted, ORDER)
		teta = teta - learning_rate * partial_derivative * 2/len(X_array)
		
		error_cost = cost(Y_array, y_predicted)
		epsilon = max(abs(partial_derivative))
		
		# Printing the parameters for each iteration
		print(f'Cost {i}: {error_cost}')
		print(f'Epsilon {i}: {epsilon}')
		
		i += 1
		
	return teta


# Calculating the loss or cost
def cost(Y_array, y_predicted):
	cost = sum((y_predicted - Y_array)**2)
	return cost


# Plotting the original points and the regression line
def display(X_array, Y_array, x_array, y_array):
	plt.plot(x_array, y_array, color="black", linewidth=2)
	plt.scatter(X_array, Y_array, color="red")
	plt.xticks(X_array)
	plt.yticks(Y_array)
	plt.show()


# Calculate the values of the y_coordinates according to teta_vactor we received in the polynomisl_regression
def function(array, teta):
	result = np.zeros(len(array))
	for i in range(len(teta)):
		result += teta[i] * array **i
	return result

	
# Get an x and y arrays of the numbers to test 
def points_test():
	NUM_SIZE = 50
	X_array = []
	Y_array = []

	for i in range(int(NUM_SIZE/2)):
		X_array.append(2*i)
		X_array.append(-i*2)
		Y_array.append(function_test(-i*2))
		Y_array.append(function_test(i*2))
	return np.array(X_array), np.array(Y_array)


# Calculate function in power of ORDER to points_test
def function_test(num):
	return num **ORDER
	
	
def main():
	#data = np.load('XYdata.npz')
	#X_array, Y_array = data['array_1'], data['array_2']
	
	X_array, Y_array = points_test()
	

	teta = polynomisl_regression(X_array, Y_array, ORDER+1, 1000)
	for i in range(len(teta)):
		print(f"teta {i}:", teta[i], end=",")
	
	#crate new points to get the regression line
	x_array = np.linspace(-50, 50, 100)
	y_array = function(x_array, teta)
	
	display(X_array, Y_array, x_array, y_array)
	
	
if __name__ == "__main__":
    main()


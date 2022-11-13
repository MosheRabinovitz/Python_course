import numpy as np
import matplotlib.pyplot as plt

ORDER = int(input("Enter number for ORDER of the function: ")) +1


#Calculating the vector of the gradients
def gradient_descent(X_array, Y_array, y_predicted, weights):
	partial_derivative = np.zeros(ORDER)
	for i in range(ORDER):
		partial_derivative[i] = sum(weights * (X_array **i) * (y_predicted - Y_array)) # * 2/len(X_array)
	return partial_derivative


#Algorithm for Gradient Descent
def polynomisl_regression(X_array, Y_array, weights, iterations=2000):

	#Initializing teta, learning rate ,epsilon and iterations
	teta = np.array([1] * ORDER)
	learning_rate = 10**(-2*ORDER)
	epsilon = 1
	iterations = iterations
	
	i = 0
	while i < iterations and epsilon > learning_rate: 
		y_predicted = np.zeros(len(X_array))
		for j in range(ORDER):
			y_predicted += teta[j] * X_array **j
		partial_derivative = gradient_descent(X_array, Y_array, y_predicted, weights)
		teta = teta - learning_rate * partial_derivative
		
		error_cost = cost(Y_array, y_predicted, weights)
		epsilon = max(abs(partial_derivative))
		coefficient = coefficient_of_determination(Y_array, y_predicted)
		# Printing the parameters for each iteration
		print(f'Cost {i}: {error_cost}')
		print(f'Epsilon {i}: {epsilon}')
		print(f'coefficient_of_determination: {coefficient}')
		
		i += 1
	
	return teta


# Weight_function for the center
def weights(X_array):
	median = np.median(X_array)
	max_distance = max(abs(median - max(X_array)), abs(median - min(X_array)))
	weights = -(X_array - median)**2 + max_distance **2 + 0.01
	sum_array = sum(weights)
	weights /= sum_array
	return weights


# Calculating the loss or cost
def cost(Y_array, y_predicted, weights):
	cost = sum(weights * (y_predicted - Y_array)**2)
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
		X_array.append(i*2)
		X_array.append(-i*2)
		Y_array.append(function_test(i*2))
		Y_array.append(function_test(-i*2))
	return np.array(X_array), np.array(Y_array)


# Calculate function in power of ORDER to points_test
def function_test(num):
	return num **(ORDER-1)
	
	
def main():
	data = np.load('XYdata.npz')
	X_array, Y_array = data['array_1'], data['array_2']
	
	#X_array, Y_array = points_test()
	
	weights_coordinates = weights(X_array)
	iterations = int(input("Enter number for iterations: "))
	teta = polynomisl_regression(X_array, Y_array, weights_coordinates, iterations)
	for i in range(len(teta)):
		print(f"teta {i}: {teta[i]}", end=", ")
	
	#crate new points to get the regression line
	x_array = np.linspace(-1, 11, 100)
	y_array = function(x_array, teta)
	
	display(X_array, Y_array, x_array, y_array)
	
	
if __name__ == "__main__":
    main()


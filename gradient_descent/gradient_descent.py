import numpy as np
import matplotlib.pyplot as plt


#Calculating the values of the gradients
def gradient_descent(X_array, Y_array, y_predict,weights):
	partial_derivative_1 = sum(weights * (y_predict - Y_array))
	partial_derivative_2 = sum(weights * X_array * (y_predict - Y_array))
	return partial_derivative_1, partial_derivative_2


#Algorithm for Gradient Descent
def linear_regression(X_array, Y_array, weights, iterations=2000):
	#Initializing teta, learning rate and epsilon
	teta_1 ,teta_2 = 1, 1
	learning_rate = 10**-3
	epsilon = 1
	iterations = iterations
	
	i = 0
	while i < 10000 and epsilon > learning_rate: 
		y_predict = (teta_2 * X_array) + teta_1
		partial_derivative_1, partial_derivative_2 = gradient_descent(X_array, Y_array, y_predict, weights)
		
		teta_1 = teta_1 - learning_rate * partial_derivative_1
		teta_2 = teta_2 - learning_rate * partial_derivative_2 
		
		cost_error = cost(Y_array, y_predict, weights)
		epsilon = max(abs(partial_derivative_1), abs(partial_derivative_2))
		print(f'Cost function {i}: {cost_error}')
		print(f'Epsilon {i}: {epsilon}')
		i += 1
	print('coefficient_of_determination: ', coefficient_of_determination(Y_array, y_predict))
	return teta_1, teta_2


# Calculating the loss or cost
def cost(Y_array, y_predict, weights):
	cost = np.sum(weights *(y_predict - Y_array)**2)
	return cost


# Plotting the original points and the regression line
def display(X_array,Y_array, x_points, y_points):
	plt.plot(x_points ,y_points)
	plt.scatter(X_array, Y_array, color="red")
	plt.show()


# Calculate the values of the y_coordinates according to teta we received in the linear_regression
def function(x_points, teta_1, teta_2):
	result = teta_1 + teta_2 * x_points
	return result
	

# Weight_function for the center
def weights(X_array):
	median = np.median(X_array)
	max_distance = max(abs(median - max(X_array)), abs(median - min(X_array)))
	weights = -(X_array - median)**2 + max_distance **2 + 0.01
	sum_array = sum(weights)
	weights /= sum_array
	return weights
	

#Calculate the Coefficient of Determination
def coefficient_of_determination(Y_array, y_predict):
	mean = np.mean(Y_array)
	ss_res = sum((Y_array - y_predict)**2)
	ss__tot = sum((Y_array - mean)**2)
	coefficient_of_determination = 1 - ss_res/ss__tot
	return coefficient_of_determination
	
	
	
def main():
	data = np.load('XYdata.npz')
	X_array, Y_array = data['array_1'], data['array_2']
	
	weight = weights(X_array)
	teta_1, teta_2 = linear_regression(X_array, Y_array, weight)
	print("teta 1:", teta_1, "teta 2:", teta_2)
	
	#crate new points to get the regression line
	x_points = np.linspace(-1, 11, 50)
	y_points = function(x_points, teta_1, teta_2)
	
	display(X_array, Y_array, x_points ,y_points)
	
	
if __name__ == "__main__":
    main()


import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():

	NUM_SIZE = 1000
	arr_1 = np.array(np.arange(NUM_SIZE)).reshape((-1, 1))
	arr = []

	for i in range(len(arr_1)):
		arr.append(function(i))
	arr = np.array(arr)

	#arr_train, arr_1_train = np.delete(arr, np.arange(len(arr), 3)), np.delete(arr_1, np.arange(len(arr_1), 3)).reshape((-1, 1))
	#arr_test, arr_1_test = arr[::3], arr_1[::3].reshape((-1, 1))
	
	#arr_1_train = np.delete(arr_1, rand_index).reshape((-1, 1))
	#arr_train = np.delete(arr, rand_index)
	
	
	rand_indexes = random.sample(range(len(arr)), int(len(arr)/3))

	arr_1_train = np.array([arr_1[index] for index in range(len(arr_1)) if index not in rand_indexes]).reshape((-1, 1))
	arr_train = np.array([arr[index] for index in range(len(arr)) if index not in rand_indexes])
	arr_1_test = np.array([arr_1[rand_index] for rand_index in rand_indexes]).reshape((-1, 1))
	arr_test = np.array([arr[rand_index] for rand_index in rand_indexes])
	
	
	model = LinearRegression().fit(arr_1_train, arr_train)
	forks_predict = model.predict(arr_1_test)
	stars_predict = model.predict(arr_1_train)
	#forks_pred = model.intercept_ + model.coef_ * stars_train

	regression_error = model.score(arr_1_test, arr_test)
	print(f"coefficient of determination: {regression_error}")
	
	
	plt.scatter(arr_1_train, arr_train, color="red")
	plt.scatter(arr_1_test, arr_test, color="blue")
	plt.plot(arr_1_test, forks_predict, color="black", linewidth=2)
	plt.plot(arr_1_train, stars_predict, color="green", linewidth=2)
	plt.xticks()
	plt.yticks()
	plt.show()


def function(num):
	return num * num

if __name__ == "__main__":
    main()

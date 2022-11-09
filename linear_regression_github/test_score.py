import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def main():

	arr_1 = np.array(np.arange(1000)).reshape((-1, 1))
	arr = []

	for i in range(1000):
		arr.append(function(i))
	arr = np.array(arr)
	#print(arr_1)
	#print(arr)

	arr_train, arr_1_train = np.delete(arr, np.arange(len(arr), 3)), np.delete(arr_1, np.arange(len(arr_1), 3)).reshape((-1, 1))
	arr_test, arr_1_test = arr[::3], arr_1[::3].reshape((-1, 1))
	
		
	model = LinearRegression().fit(arr_1_train, arr_train)
	forks_predict = model.predict(arr_1_test)
	#forks_pred = model.intercept_ + model.coef_ * stars_train

	regression_error = model.score(arr_1_test, arr_test)
	print(f"coefficient of determination: {regression_error}")
	
	
	plt.scatter(arr_1_train, arr_train, color="red")
	plt.scatter(arr_1_test, arr_test, color="blue")
	plt.plot(arr_1_test, forks_predict, color="black", linewidth=3)
	plt.xticks()
	plt.yticks()
	plt.show()


def function(num):
	return num * num

if __name__ == "__main__":
    main()

import random
import numpy as np

def point_distance(correct_point, check_point):
	distance = sum((correct_point-check_point)**2)**0.5
	return distance


def array_distance(correct_flower, flowers_data, index):
	array_distance = np.zeros(len(flowers_data))
	i = 0
	for flower in flowers_data:
		if not i == index: #np.array_equal(flower, correct_flower):
			array_distance[i] = (point_distance(correct_flower, flower))
		else:
			array_distance[i] = 1.7976931348623157e+308			
		i+=1
		
	return array_distance


def k_nearest_neighbors(correct_flower, flowers_data, k, i):
	distance = array_distance(correct_flower, flowers_data, i)
	min_k_distance = np.argpartition(distance, k)
	min_k = min_k_distance[:k]
	return min_k
	
	
def vote(flowers_type, min_k):
	names = flowers_type[min_k]
	most_frequent = np.bincount(names)#.argmax()
	maximum = max(most_frequent)
	most_frequent =[i for i in range(len(most_frequent)) if most_frequent[i] == maximum]
	if len(most_frequent) == 1:
		return most_frequent[0]
	else:
		return most_frequent[0]
	

def change_to_name(most_frequent):
	if most_frequent == 1:
		return 'Iris-setosa'
	elif most_frequent == 2:
		return 'Iris-versicolor'
	else:
		return 'Iris-virginica'
	
	
def training(flowers_data, flowers_type):
	best_k = 0
	best_cuont = 0
	best = []
	for k in range(1, 20):
		count = 0
		i = 0
		for flower in flowers_data:
			neighbors = k_nearest_neighbors(flower, flowers_data, k, i)
			predict_flower = vote(flowers_type, neighbors)
			if predict_flower == flowers_type[i]:
				count +=1
			i += 1
		best.append(count)
		if best_cuont < count:
			best_cuont = count
			best_k = k
	print(best)
	print(f'Accuracy of {best_cuont} out of {len(flowers_data)}')
	precision = 100 * best_cuont / len(flowers_data)
	print(f'precision: {precision} %')
	return best_k


def predict(flowers_data_test, flowers_type_test, flowers_data, flowers_type, num_k_neighbors):
	count = 0
	i = 0
	for flower in flowers_data_test:
		neighbors = k_nearest_neighbors(flower, flowers_data, num_k_neighbors, i)
		predict_flower = vote(flowers_type, neighbors)
		if predict_flower == flowers_type_test[i]:
			count +=1
		i+=1
	print(f'Accuracy of {count} out of {len(flowers_data_test)}')
	error = 100 * count / len(flowers_data_test)
	return error


def main():
#	flowers_type = np.loadtxt("iris.data",usecols=4, skiprows=1, dtype='str', delimiter=",")
#	flowers_data = np.loadtxt("iris.data",usecols=[0,1,2,3], skiprows=1, dtype='float', delimiter=",")
	flowers_type = np.loadtxt("aaa.data",usecols=2, skiprows=1, dtype='str', delimiter=",")
	flowers_data = np.loadtxt("aaa.data",usecols=[0,1,], skiprows=1, dtype='float', delimiter=",")

#	for i in range(15):
#	print('itarition: ', i)

	shuffler = np.random.permutation(len(flowers_type))
	flowers_type_shuffled = flowers_type[shuffler]
	flowers_data_shuffled = flowers_data[shuffler]
	
	flowers_type_shuffled[flowers_type_shuffled=='Iris-setosa'] = 1
	flowers_type_shuffled[flowers_type_shuffled=='Iris-versicolor'] = 2
	flowers_type_shuffled[flowers_type_shuffled=='Iris-virginica'] = 3
	flowers_type_shuffled = flowers_type_shuffled.astype(int)
	
	middle = int(len(flowers_type_shuffled)*4/5)
	flowers_data_train = flowers_data_shuffled[:middle]
	flowers_type_train = flowers_type_shuffled[:middle]
	flowers_data_test = flowers_data_shuffled[middle:]
	flowers_type_test = flowers_type_shuffled[middle:]
	
	best_k = training(flowers_data_train, flowers_type_train)
	print("best_k: ", best_k)
	print()
	print('predict of flowers_data_test:')
	precision = predict(flowers_data_test, flowers_type_test, flowers_data_train, flowers_type_train, best_k)
	print(f'precision: {precision} %')


if __name__ == "__main__":
    main()

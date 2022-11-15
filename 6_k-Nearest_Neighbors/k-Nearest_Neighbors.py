import random
import numpy as np


#Finds k neighbors from a specific point
def find_k_nearest_neighbors(correct_flower, flowers_data, k, i):
	distance = array_distance_from_point(correct_flower, flowers_data, i)
	min_k_distance = np.argpartition(distance, k)
	min_k = min_k_distance[:k]
	return min_k


#Calculate the distances of other points from a specific point
def array_distance_from_point(correct_flower, flowers_data, index):
	array_distance = np.zeros(len(flowers_data))
	i = 0
	for flower in flowers_data:
		array_distance[i] = point_distance(correct_flower, flower) if not i == index else 1.7976931348623157e+308			
		i+=1		
	return array_distance


#Calculate the distance between two points according to the Pythagorea theorem
def point_distance(correct_point, check_point):
	distance = sum((correct_point-check_point)**2)**0.5
	return distance
	

#Choose the most frequent type from k neighbors
def vote(flowers_type, min_k):
	names = flowers_type[min_k]
	flower_predict = most_frequent(names)
	return flower_predict[0] if len(flower_predict) == 1 else flower_predict[0]
	

#Find the best k neighbors for predicting the flower type
def training(flowers_data, flowers_type, range_k):
	best_k = 0
	best_cuont = 0

	for k in range(1, range_k):
		count = count_precision(flowers_data, flowers_type, k, flowers_data, flowers_type)
		if best_cuont < count:
			best_cuont = count
			best_k = k

	precision = round(100 * best_cuont / len(flowers_data))
	return best_k, precision, best_cuont


#Predicting the flower type of data test according to flowers data
def predict(flowers_data_test, flowers_type_test, flowers_data, flowers_type, num_k_neighbors):
	count = count_precision(flowers_data, flowers_type, num_k_neighbors, flowers_data_test, flowers_type_test)
	error = round(100 * count / len(flowers_data_test))
	return count, error


#Calculate the number of the successful predictions
def count_precision(flowers_data, flowers_type, num_k_neighbors ,pretict_flowers_data, test_type_flowers):
	count = 0
	i = 0
	for flower in pretict_flowers_data:
		neighbors = find_k_nearest_neighbors(flower, flowers_data, num_k_neighbors, i)
		predict_flower = vote(flowers_type, neighbors)
		if predict_flower == test_type_flowers[i]:
			count +=1
		i += 1
	return count
	

#Find the most frequent value in an array
def most_frequent(array):
	most_frequent = np.bincount(array)
	maximum = max(most_frequent)
	most_frequent =[i for i in range(len(most_frequent)) if most_frequent[i] == maximum]
	return most_frequent


#Extract data from the file into two numpy arrays
def extract_file(dats_file):
	flowers_data = np.loadtxt(dats_file,usecols=[0,1,2,3], skiprows=1, dtype='float', delimiter=",")
	flowers_type = np.loadtxt(dats_file,usecols=4, skiprows=1, dtype='str', delimiter=",")
#	flowers_data = np.loadtxt(dats_file,usecols=[0,1], skiprows=1, dtype='float', delimiter=",")
#	flowers_type = np.loadtxt(dats_file,usecols=2, skiprows=1, dtype='str', delimiter=",")

	flowers_type[flowers_type=='Iris-setosa'] = 1
	flowers_type[flowers_type=='Iris-versicolor'] = 2
	flowers_type[flowers_type=='Iris-virginica'] = 3
	flowers_type = flowers_type.astype(int)
	
	return flowers_data, flowers_type


#Return the flower type according to the number
def change_to_name(most_frequent):
	if most_frequent == 1:
		return 'Iris-setosa'
	elif most_frequent == 2:
		return 'Iris-versicolor'
	else:
		return 'Iris-virginica'


def main():
	flowers_data, flowers_type = extract_file("iris.data")
	#flowers_data, flowers_type = extract_file("test.data")
	range_k = int(input('Enter number for range k: '))
	best = []
	
	#Run 100 times to find the best k of any shuffle
	for i in range(100):
		print('\nThe itarition now is:', i+1)

		shuffler = np.random.permutation(len(flowers_type))
		flowers_type_shuffled = flowers_type[shuffler]
		flowers_data_shuffled = flowers_data[shuffler]
		
		middle = int(len(flowers_type_shuffled)*4/5)
		flowers_data_train, flowers_type_train = flowers_data_shuffled[:middle], flowers_type_shuffled[:middle]
		flowers_data_test, flowers_type_test = flowers_data_shuffled[middle:], flowers_type_shuffled[middle:]
		
		best_k, precision, best_cuont = training(flowers_data_train, flowers_type_train, range_k)
		best.append(best_k)
		print('The best k is:', best_k)
		print(f'Accuracy of this itarations is: {best_cuont} out of {len(flowers_data)}')
		print(f'precision: {precision} %')
		
	best_k_itarations = most_frequent(best)
	count, precision = predict(flowers_data_test, flowers_type_test, flowers_data_train, flowers_type_train, best_k_itarations[0])
	
	print('\nFinal result:')
	print("\nThe best k itarations is:", best_k_itarations)
	print(f'\nAccuracy of {count} out of {len(flowers_data_test)}')
	print(f'precision: {precision} %')


if __name__ == "__main__":
    main()

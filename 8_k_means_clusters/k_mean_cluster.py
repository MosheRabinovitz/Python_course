import csv, random
import matplotlib.pyplot as plt


DIMENSIONS = 4
NUM_ITARETIONS = 10
K = int(input('Enter a number for the k mean: '))


# Extracts attributes of the irises from the file and return an array of them
# in addition to checking the results, returns an array of pairs [attributes, iris species]
def extract_file_and_order_data(file_name):
	# Extract data
	with open(file_name) as f:
		csvreader = csv.reader(f)
		data = list(csvreader)
	
	# Gets an array containing the attributes
	attributes = [[float(iris[j]) for j in range(4)] for iris in data]
	
	#Organizes into an array of pairs
	data_pairs = [[attribute, iris[-1]] for attribute, iris in zip(attributes,data)]
	return attributes, data_pairs


# Random selection of K central points for the first iteration
def start_random(data, k):
	random_irises = random.sample(data, k)
	return random_irises


# Association of each iris to the cluster closet to it
def association(k_clusters, data):
	clusters = [[]for i in range(len(k_clusters))]
	
	for point in data:
		index, min_distance = index_of_min_distance(point, k_clusters)
		clusters[index].append([point, min_distance])

	return clusters


# Calculate the minimum distance between a point and k central clusters
def index_of_min_distance(correct_point, k_clusters):
	min_distance = 2**63-1
	short_distance_index = -1
	
	for k_point in k_clusters:
		distance = points_distance(correct_point, k_point)
		if distance < min_distance:
			short_distance_index = k_clusters.index(k_point)
			min_distance = distance
			
	return short_distance_index, min_distance


# Calculate the distance between two points according to the Pythagorea theorem
def points_distance(correct_point, k_point):
	distance = sum([(i-j)**2 for i,j in zip(correct_point, k_point)])
	return distance


# Find the central mass of each cluster 
def find_central_mass(clusters):
	k_clusters = [[] for i in clusters]
	
	for k in range(len(clusters)):
		for i in range(DIMENSIONS):
			central_mass  = 0
			for iris in clusters[k]:
				central_mass += iris[0][i]/len(clusters[k])
			k_clusters[k].append(central_mass)
	return k_clusters


# Calculation of the squared distance of the data (from index 1 in each iris) according to the association with the clusters 
def squared_distance(clusters):
	squared_distance = 0
	for k_mean in clusters:
		for iris in k_mean:
			squared_distance += iris[1]
	return squared_distance
	

# Improving the clusters untill the convergence 
def clustering(random_irises, data):
	previos_k_clusters = random_irises
	
	clusters = association(random_irises, data)
	error = squared_distance(clusters)
	current_k_clusters = find_central_mass(clusters)
	
	while not(current_k_clusters == previos_k_clusters):
		previos_k_clusters = current_k_clusters
		clusters = association(current_k_clusters, data)
		current_k_clusters = find_central_mass(clusters)
		error = squared_distance(clusters)

	return clusters, error


# Finds the k best clusters per one k (given a number for k) 
def itaretions_per_k(data, k):

	squared_distances = []
	clusters_itarations = []
	
	for i in range(NUM_ITARETIONS):
		random_irises = start_random(data, k)
		clusters, current_squared_distance = clustering(random_irises, data)
		squared_distances.append(current_squared_distance)
		clusters_itarations.append(clusters)
	
	index_of_best_cluster = squared_distances.index(min(squared_distances))
	return squared_distances[index_of_best_cluster], clusters_itarations[index_of_best_cluster]


# Calculate all the best clusters for range 1 to K
def find_the_best_k(data, k_meam):

	squared_distances = []
	clusters_of_k_means = []
	
	for k in range(1, k_meam):
		squared_distances_of_size_k, clusters_of_size_k = itaretions_per_k(data, k)
		squared_distances.append(squared_distances_of_size_k)
		clusters_of_k_means.append(clusters_of_size_k)

	return squared_distances, clusters_of_k_means


# Show the errors of the squared distances for each k between 1 to K
def display(squared_distances):
	
	x_axis = [i for i in range(1, K)]
	plt.style.use('seaborn')
	plt.plot(x_axis, squared_distances)
	plt.xticks(x_axis)
	#plt.yscale('log')
	plt.xlabel("k")
	plt.ylabel("total squared error")
	plt.title("Total Error vs. # of Clusters")
	plt.show()
	

# Create a matrix of K * iris_type and count the appearance of each iris type in a clusters 
def confusion_matrix(clusters, data_pairs, choose_k):
	confusion_mat = [[0]*3 for i in clusters]
	
	for i in range(len(clusters)):
		for iris in clusters[i]:
			index = search(iris[0], data_pairs)
			confusion_mat[i][index] +=1

	return confusion_mat
				

# Search in the data the iris type
def search(iris_coordinate, data_pairs):
	iris_type = 7
	for iris in data_pairs:
		if iris_coordinate == iris[0]:
			iris_type = iris[-1]
			return 0 if iris_type == 'Iris-setosa' else 1 if iris_type == 'Iris-versicolor' else 2


# Printing the appearance of each iris in clusters
def to_display(confusion_mat):
	for value in range(3):
		print(f'\nIris {value+1}: ', end='  ')
		for row in confusion_mat:	
			print(row[value], end='	')
	print()


def main():

	# Extract the data
	data, data_pairs = extract_file_and_order_data('iris.data')
#	data, data_pairs = extract_file_and_order_data('test.data')
	
	# Calculate and show all the best clusters for range 1 to K
	squared_distances, clusters_of_k_means = find_the_best_k(data, K)
	display(squared_distances)
	
	# Asking to choose k and printing the appearance of each iris in clusters 
	choose_k = int(input('Choose k: ')) -1
	confusion_mat = confusion_matrix(clusters_of_k_means[choose_k], data_pairs, choose_k)
	to_display(confusion_mat)
	

if __name__ == "__main__":
    main()

import csv, math, random

# The number of the attribute columns
DIMENTION = 4

# Extract data from the file and organizes them to an array of pairs  = [attribute, iris species]
def extract_file_and_order_data(file_name):
	# Extract data
	with open(file_name) as f:
		csvreader = csv.reader(f)
		data = list(csvreader)
	
	#Organizes to an array of pairs
	coordinates = [[float(data[i][j]) for j in range(4)] for i in range(len(data))]
	data_pairs = [[coordinates[i], data[i][-1]] for i in range(len(data))]
	return data_pairs


# Shuffle and split the Data to two arrays train_data and test_data
def split_dataset(data_pairs):
	random.shuffle(data_pairs)
	train_data, test_data = data_pairs[:int(len(data_pairs)*0.8)], data_pairs[int(len(data_pairs)*0.8):]
	return train_data, test_data


# Return an array of arrays of the unique attributes for each column(index) 
def get_labels(data_pairs):
	temp = [[int(data_pairs[j][0][i]) for j in range(len(data_pairs))] for i in range(DIMENTION)]
	unique_attributes = [set(temp[i]) for i in range(len(temp))]
	return unique_attributes


# Create a dictionary in order to count appearances of each attribute in iris varieties
def crate_dictionary(unique_attributes):
	dictionary = {}
	for i in range(len(unique_attributes)):
		dictionary[i] = {}
		for item in unique_attributes[i]:
			dictionary[i][item] = [0,0,0]
	return dictionary


# Count from the data train the appearances of each attribute in iris varieties
def count_attribute(dictionary, train_data):
	for i in range(len(train_data)):
		for j in range(DIMENTION):
			attribute = int(train_data[i][0][j])
			dictionary[j][attribute][0 if train_data[i][1] == 'Iris-setosa' else 1 if train_data[i][1] == 'Iris-versicolor' else 2] +=1


# Count the total sum of the each iris variety
def count_sum_irises(train_data):
	sum_setosa = sum_versicolor = sum_virginica = 0
	for i in range(len(train_data)):
		if train_data[i][1] == 'Iris-setosa':
			sum_setosa +=1
		elif train_data[i][1] == 'Iris-versicolor':
			sum_versicolor +=1
		else:
			sum_virginica +=1
	return sum_setosa, sum_versicolor, sum_virginica


# Calculate the probability of each attribute belonging to one of the irises
def attributes_probabilities(dictionary, sum_setosa, sum_versicolor, sum_virginica, k=0.5):
	probabilities = [0] * (DIMENTION)
	for i in range(DIMENTION):
		probabilities[i] = []
		for j, (setosa, versicolor, virginica) in dictionary[i].items():
			probabilities[i].append((j, (setosa + k) / (sum_setosa + 2 * k), (versicolor + k) / (sum_versicolor + 2 * k), (virginica + k) / (sum_virginica + 2 * k)))

	return probabilities
	

# Calculate the probabilities of each attribute which variety it belong
def irises_probabilities(atribite_probabilities ,iris):
	log_prob_if_setosa = log_prob_if_versicolor = log_prob_if_virginica = 0.0
	for i in range(DIMENTION):
		for atribite, prob_if_setosa, prob_if_versicolor, prob_if_virginica in atribite_probabilities[i]:
			if atribite == int(iris[i]):
				log_prob_if_setosa += math.log(prob_if_setosa)
				log_prob_if_versicolor += math.log(prob_if_versicolor)
				log_prob_if_virginica += math.log(prob_if_virginica)
				
			else:
				log_prob_if_setosa += math.log(1.0 - prob_if_setosa)
				log_prob_if_versicolor += math.log(1.0 - prob_if_versicolor)
				log_prob_if_virginica += math.log(1.0 - prob_if_virginica)
	
	prob_if_setosa = math.exp(log_prob_if_setosa)
	prob_if_versicolor = math.exp(log_prob_if_versicolor)
	prob_if_virginica = math.exp(log_prob_if_virginica)
	
	setosa_probabilities = prob_if_setosa / (prob_if_setosa + prob_if_versicolor + prob_if_virginica)
	versicolor_probabilities = prob_if_versicolor / (prob_if_setosa + prob_if_versicolor + prob_if_virginica)
	virginica_probabilities = prob_if_virginica / (prob_if_setosa + prob_if_versicolor + prob_if_virginica)
	
	return setosa_probabilities, versicolor_probabilities, virginica_probabilities


# Calculate and test the accuracy of the probability model on the testing data
def testing_model(test_data, probabilities, sum_setosa, sum_versicolor, sum_virginica):
	count_setosa = count_versicolor = count_virginica = 0
	for i in range(len(test_data)):
		setosa_probabilities, versicolor_probabilities, virginica_probabilities = irises_probabilities(probabilities ,test_data[i][0])
		iris_prob = 'Iris-setosa' if setosa_probabilities > versicolor_probabilities and setosa_probabilities > virginica_probabilities else 'Iris-versicolor' if versicolor_probabilities > setosa_probabilities and versicolor_probabilities > virginica_probabilities else 'Iris-virginica'
		
		count_setosa += 1 if test_data[i][1] == 'Iris-setosa' and iris_prob == test_data[i][1] else 0
		count_versicolor += 1 if test_data[i][1] == 'Iris-versicolor' and iris_prob == test_data[i][1] else 0
		count_virginica += 1 if test_data[i][1] == 'Iris-virginica' and iris_prob == test_data[i][1] else 0
	
	setosa_success = round(100 * count_setosa / sum_setosa)
	versicolor_success = round(100 * count_versicolor / sum_versicolor)
	virginica_success = round(100 * count_virginica / sum_virginica)
	
	return count_setosa,count_versicolor, count_virginica, setosa_success, versicolor_success, virginica_success


def main():
	# Extract and order the data into an array of pairs
	data_pairs = extract_file_and_order_data('iris.data')
	
	# Get a dictionary of the unique attributes of each column to count the appearances
	unique_attributes = get_labels(data_pairs)
	dictionary = crate_dictionary(unique_attributes)
	
	# Split the data and calculate the probabilities of each attribute which variety it belong
	train_data, test_data = split_dataset(data_pairs)
	sum_setosa, sum_versicolor, sum_virginica = count_sum_irises(train_data)
	count_attribute(dictionary, train_data)
	probabilities = attributes_probabilities(dictionary, sum_setosa, sum_versicolor, sum_virginica, 0.5)
	
	# Calculate and test the accuracy of the probability model on the testing data
	sum_setosa, sum_versicolor, sum_virginica = count_sum_irises(test_data)
	count_setosa,count_versicolor, count_virginica, setosa_success, versicolor_success, virginica_success = testing_model(test_data, probabilities, sum_setosa, sum_versicolor, sum_virginica)
	
	# Printing the results
	print(f'{count_setosa = } out of {sum_setosa}')
	print(f'{count_versicolor = } out of {sum_versicolor}')
	print(f'{count_virginica = } out of {sum_virginica}')
	
	print(f'{setosa_success = } %')
	print(f'{versicolor_success = } %')
	print(f'{virginica_success = } %')
	print(f'final accuracy is: {count_setosa + count_versicolor + count_virginica} out of {sum_setosa + sum_versicolor + sum_virginica}')
	print(f'final grade is: {round(100 * (count_setosa + count_versicolor + count_virginica)/(sum_setosa + sum_versicolor + sum_virginica))} %')

if __name__ == "__main__":
    main()

import csv, math, random

# The number of the attribute columns
DIMENTION = 22

# Extract data from the file and organizes them to an array of pairs  = [is_poisonous, attribute]
def extract_file_and_order_data(file_name):
	# Extract data
	with open(file_name) as f:
		csvreader = csv.reader(f)
		data = list(csvreader)
	
	#Organizes to an array of pairs
	data_pairs = [[data[i][1:], data[i][0]] for i in range(len(data))]
	return data_pairs


# Shuffle and split the Data to two arrays train_data and test_data
def split_dataset(data_pairs):
	random.shuffle(data_pairs)
	train_data, test_data = data_pairs[:int(len(data_pairs)*0.8)], data_pairs[int(len(data_pairs)*0.8):]
	return train_data, test_data


# Return an array of arrays of the unique attributes for each column(index) 
def get_labels(data_pairs):
	temp = [[data_pairs[j][0][i] for j in range(len(data_pairs))] for i in range(DIMENTION)]
	unique_attributes = [set(temp[i]) for i in range(len(temp))]	
	return unique_attributes


# Create a dictionary in order to count the poisonous/not poisonous for each attribute
def crate_dictionary(unique_attributes):
	dictionary = {}
	for i in range(len(unique_attributes)):
		dictionary[i] = {}
		for item in unique_attributes[i]:
			dictionary[i][item] = [0,0]
	return dictionary


# Count from the data train the appearances of each attribute in poisonous/not poisonous mushrooms 
def count_attribute(dictionary, train_data):
	for i in range(len(train_data)):
		for j in range(DIMENTION):
			attribute = train_data[i][0][j]
			dictionary[j][attribute][0 if train_data[i][1] == 'p' else 1] +=1


# Count the total sum of the poisonous/not poisonous mushrooms
def count_sum_poisonous(train_data):
	sum_poisonous = sum_non_poisonous = 0
	for i in range(len(train_data)):
		if train_data[i][1] == 'p':
			sum_poisonous +=1
		else:
			sum_non_poisonous +=1
	return sum_poisonous, sum_non_poisonous


# Calculate the probability for each attribute to be poisonous/not poisonous
def attributes_probabilities(dictionary, sum_poisonous, sum_non_poisonous, k=0.5):
	x = 0
	probabilities = [0] * (DIMENTION)
	for i in range(DIMENTION):
		probabilities[i] = []
		for j, (poisonous, non_poisonous) in dictionary[i].items():
			probabilities[i].append((j, (poisonous + k) / (sum_poisonous + 2 * k), (non_poisonous + k) / (sum_non_poisonous + 2 * k)))
			x+= (poisonous + k) / (sum_poisonous + 2 * k)
	print(x)
	
	return probabilities
	

# Calculate the poisonous probability for each mashroom 
def poisonous_probabilities(atribite_probabilities ,mushroom):
	log_prob_if_poisonous = log_prob_if_not_poisonous = 0.0
	for i in range(DIMENTION):
		for atribite, prob_if_poisonous, prob_if_not_poisonous in atribite_probabilities[i]:
			if atribite in mushroom[i]:
				log_prob_if_poisonous += math.log(prob_if_poisonous)
				log_prob_if_not_poisonous += math.log(prob_if_not_poisonous)
			else:
				log_prob_if_poisonous += math.log(1.0 - prob_if_poisonous)
				log_prob_if_not_poisonous += math.log(1.0 - prob_if_not_poisonous)
	
	prob_if_poisonous = math.exp(log_prob_if_poisonous)
	prob_if_not_poisonous = math.exp(log_prob_if_not_poisonous)
	
	poisonous_probabilities = prob_if_poisonous / (prob_if_poisonous + prob_if_not_poisonous)
	
	return poisonous_probabilities


# Calculate and test the accuracy of the probability model on the testing data
def testing_model(test_data, probabilities, sum_poisonous, sum_non_poisonous):
	count_poisonous = count_non_poisonous = 0
	for i in range(len(test_data)):
		poisonous_prob = poisonous_probabilities(probabilities ,test_data[i][0])
		mushroom_prob = 'p' if poisonous_prob > 0.5 else 'e'
		count_poisonous += 1 if test_data[i][1] == 'p' and mushroom_prob == test_data[i][1] else 0
		count_non_poisonous += 1 if test_data[i][1] == 'e' and mushroom_prob == test_data[i][1] else 0
	
	poisonous_success = round(100 * count_poisonous / sum_poisonous)
	non_poisonous_success = round(100 * count_non_poisonous / sum_non_poisonous)
	
	return count_poisonous,count_non_poisonous, poisonous_success, non_poisonous_success


def main():
	# Extract and order the data into an array of pairs
	data_pairs = extract_file_and_order_data('agaricus-lepiota.data')
	
	# Get a dictionary of the unique attributes of each column to count the appearances
	unique_attributes = get_labels(data_pairs)
	dictionary = crate_dictionary(unique_attributes)
	
	# Split the data and calculate the probabilities of each attribute to be poisonous/not poisonous
	train_data, test_data = split_dataset(data_pairs)
	sum_poisonous, sum_non_poisonous = count_sum_poisonous(train_data)
	count_attribute(dictionary, train_data)
	probabilities = attributes_probabilities(dictionary, sum_poisonous, sum_non_poisonous, 10**-5)
	
	# Calculate and test the accuracy of the probability model on the testing data
	sum_poisonous, sum_non_poisonous = count_sum_poisonous(test_data)
	count_poisonous,count_non_poisonous, poisonous_success, non_poisonous_success = testing_model(test_data, probabilities, sum_poisonous, sum_non_poisonous)
	
	# Printing the results
	print(f'{count_poisonous = } out of {sum_poisonous}')
	print(f'{count_non_poisonous = } out of {sum_non_poisonous}')
	print(f'{poisonous_success = } %')
	print(f'{non_poisonous_success = } %')
	print(f'final accuracy is: {count_poisonous + count_non_poisonous} out of {sum_poisonous + sum_non_poisonous}')
	print(f'final grade is: {round(100 * (count_poisonous + count_non_poisonous)/(sum_poisonous + sum_non_poisonous))} %')

if __name__ == "__main__":
    main()

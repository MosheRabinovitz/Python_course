import requests, json, sys, os.path

BASE_URL = "https://swapi.dev/api/"

# Return names/titles of resources that contain the term
def search(resource, term):
	# Get the data 
	data = reduce_api(resource)
	
	# Add to results the resources if containing the term
	results = {}
	for resource in data:
		if any(term in item for item in resource):
			results[resource['name' if 'name' in resource else 'title']] = resource[term] 
	return results
		

# Return the sorted order_field in 'planets'
def get_planets_sorted(order_field, reverse = False):
	# Get the data 
	data = reduce_api('planets')
	# Sort the data
	results = sorted(data, key = lambda resource: resource[order_field], reverse = reverse)
	return results


# Return the repositories from the file if the API alredy downloaded. else request it from BASE_URL
def reduce_api(resource):
	# Check if folder exists
	if not os.path.isdir('swapi'):
		os.mkdir('swapi')
	os.chdir('swapi')
	# Check if file exists
	if os.path.exists(resource + '.json'):
		with open(resource + '.json', 'r') as open_file:
			data = json.load(open_file)
		return data
	
	# Request the API from BASE_URL
	with requests.get(BASE_URL + resource) as data:
		result = json.loads(data.text)
	data = result['results']
	# Save the data
	with open(resource + '.json', 'w') as open_file:
		json.dump(data, open_file)
	os.chdir('..')
	return data
	
	
def main():
	if sys.argv[1] == 'search':
		resource = sys.argv[2]
		term = sys.argv[3]
		print(search(resource, term))
	elif sys.argv[1] == 'sorted':
		order_field = sys.argv[2]
		reverse = sys.argv[3]
		a = (get_planets_sorted(order_field, reverse == 'True'))
		for i in a:
			print(i[order_field])
	else:
		print(3)

if __name__ == "__main__":
    main()

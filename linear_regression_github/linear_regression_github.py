import json
import random
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from urllib.request import urlopen
from sklearn.linear_model import LinearRegression


#Get the repositories from the API page
def get_repositories(page_number):
	with urlopen(f'https://api.github.com/search/repositories?q=language:python&per_page=100&page={page_number}') as repo:
		data_repo = json.load(repo)
	return data_repo['items']


#Collect the repositories from the chosen number of pages to an array of repositories
def collect_repositories_pages(num_pages):
	repositories_list = []
	for i in tqdm(range(num_pages)):
		num_page = i + 1
		page = get_repositories(num_page)
		for repo in page:
			repositories_list.append(repo)	
	return repositories_list


#get the spesific wanted data from an array of repositories
def split_repositories(repositories_list):
	stars = []
	forks = []
	for repositorie in repositories_list:
		stars.append(repositorie.pop('stargazers_count'))
		forks.append(repositorie.pop('forks_count'))
	return np.array(stars), np.array(forks)


#The model of Linear Regression _ fit the model with 2/3 of the array and then predict the result for the rest of it
def linear_regression(stars, forks):

	rand_indexes = random.sample(range(len(stars)), int(len(stars)/3))
	
	stars_train = np.array([stars[index] for index in range(len(stars)) if index not in rand_indexes]).reshape((-1, 1))
	forks_train = np.array([forks[index] for index in range(len(forks)) if index not in rand_indexes])
	stars_test = np.array([stars[rand_index] for rand_index in rand_indexes]).reshape((-1, 1))
	forks_test = np.array([forks[rand_index] for rand_index in rand_indexes])
	
	model = LinearRegression().fit(stars_train, forks_train)
	forks_predict = model.predict(stars_train)
	
	regression_error = model.score(stars_test, forks_test)
	print(f"Score error: {regression_error}")

	return stars_train, forks_train, stars_test, forks_test, forks_predict
	

#Displaing the result on coordinate system
def display(stars_train, forks_train, stars_test, forks_test, forks_predict):
	plt.scatter(stars_train, forks_train, color="blue")
	plt.scatter(stars_test, forks_test, color="red")
	plt.plot(stars_train, forks_predict, color="black", linewidth=2)
	plt.xticks()
	plt.yticks()
	plt.show()


def main():
	num_of_pages = int(input("Enter number for repositories pages: "))
	list_of_repositories_pages = collect_repositories_pages(num_of_pages)
	stars_list, forks_list = split_repositories(list_of_repositories_pages)
	stars_train, forks_train, stars_test, forks_test, forks_predict = linear_regression(stars_list, forks_list)
	display(stars_train, forks_train, stars_test, forks_test, forks_predict)
	
if __name__ == "__main__":
    main()

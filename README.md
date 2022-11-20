# python_course

# 1. Random_walk_with_N_dimensions
This program shows a progression of a random walk in any chosen dimension - for any number of steps we request.

Input: The program asks for the requested number of dimensions and steps that the program will be asked to perform and display.
Output: The output of the program depends on the number of dimensions selected; If one dimension is selected, the walk will be displayed as a graph relative to the number of steps axis:

If two dimensions are selected, the progress will be shown in the graph in relation to the two dimensions of progress.
If three dimensions are selected, the walk will be displayed in a three-dimensional cube.
If a higher number of dimensions is selected, the steps will be displayed in coordinates.

# 2. CVS_file_of_best_Hacker_News_jobs
This program extracts the 60 best works on 'thehackernews.com' website, and creates a csv file that contains the details: "ID", "title", "URL", "text" for these works.

Input: the name of the file (the name of the file must end in .csv)
Output: The program finds (via API) the 60 best jobs on 'thehackernews.com' website and extracts the requested details for them, then creates a csv file and writes the requested details into it.
 
# 3. Download_wikipedia_images_by_crawler
This program downloads all images from multiple Wikipedia pages (starting from a specific page) recursively and randomly.

Input: The program asks the user for a specific link to the Wikipedia website, as well as a depth and a width argument.
Output: The program does the following:

1. Downloads all the images from the selected Wikipedia page to its folder.
2. Then it randomly selects a number of links - according to the number of the width argument - and recursively executes them.
3. The process repeats itself a number of times - according to the number of the depth argument.

# 4. Analysis_stars_and_forks_Github_projects
This program performs a mathematical analysis to check the relation between the number of 'downloads' (forks) and 'stars' for  projects in github ,with the result shown in a graph via a straight line that reflects the coefficient of determination for the number of downloads and the given number of stars, as well as representing the downloads via points for both the training set (which contains part of the data) and in the prediction set (which contains the rest).

Input: the program requests as input the number of project pages on which it will run the model (each such page will have 100 projects).

Output:
1. The program will extract the requested number of jobs from the API into an array.
2. The program will initiate an array of pairs for the stars and downloads  data.
3. The program will then run a 'linear regression' model on these values to check the error of the straight line that provides the coefficient of determination in relation to these points, then display it on a graph.

# 5 Gradient descent
This program finds and displays the equation of the line closest to all points in a given dataset.

Extensions:
a. Another program finds the polynomial equation (of  second degree) closest to the points.
b. Another program finds the polynomial equation (of  N degree) closest to the points.
c. Another program finds the exponent equation closest to the points.

Input:
The program uses the data-set from the file 'XYdata.npz' (You can use the point_test function instead)
In addition, it requests as input from the user: the requested degree and the number of iterations he wishes to run (in extensions).

Output:
The program starts the calculation from an arbitrary point, and for each point performs the calculation of the gradient (the vector of the partial derivatives) in order to learn in which direction to 'lower' the values of the equation of the line (when, of course, the result of the gradient is multiplied by the learning rate to minimize possible errors).
This process is repeated by the program as long as the progress continues, up to the limit of iterations defined by the user.

At the end of the run, the program returns the equation of the line (or the polynomial) obtained, indicates the degree of accuracy of the line in relation to the points (coefficient of determination) and displays in a graph the equation of the straight line and the true position of the points (in the training and prediction model, the points of the test array will be displayed in different colors).

In order to increase the accuracy of the model, we defined a 'weight' for each point, so that the points close to the center (on the x-axis) receive a higher score than the points that are far from it, and when calculating the gradient we multiplied the calculation of the partial derivative for each x value by the 'weight' ' corresponding to the same value, and thus we reduced the influence of the points far from the center on the resulting straight line equation.

# 6 k-nearest neighbors algorithm
This program uses the k-NN algorithm to find the number k that will provide the group of neighbors that will allow to predict with the highest degree of accuracy according to the characteristics of each flower (from the given data-set) the species to which it belongs.

Input:
The program uses a dataset from the file 'iris.data' (you can practice on the simpler data-set from the test.data file), and receives as input the highest k number that will serve as the limit of the range up to which it will check the k values.

Output:
The program performs 100 iterations so that in each iteration the program randomly selects 80% of the data, and performs k tests on it to find the best k-value in the range between 1 and the k-value chosen for the data.
Finally, the program selects the k-value that provided the highest accuracy out of the 100 iterations. And checks the result of another test with the k-value returned on an array that contains 20% of the data.

# 7 Naive Bayes classification
This program implements the Naive Bayes probabilistic model, the purpose of which is to characterize data according to their properties. In this program, we will first classify the data on a training set that will be randomly selected from the given data-set, and then we will choose the accuracy of the model in characterizing the data on the test set.

input:
The program uses a dataset from the file 'agaricus-lepiota.data', which holds data about different features of mushrooms (where for each feature there are several different options), as well as their  classification as 'poisonous' and 'non-poisonous'.

output:
a. The program splits the data into pairs of data - features alongside classification as poison/not poisonous 

b. Splits the data randomly: 80% into an array to train the model, and 20% for testing the model.

c. Training: the program extracts from the training set all the unique options that exist for each of the twenty-two attributes of the mushrooms, and initializes a nested dictionary for each attribute, within which is a nested dictionary for each option.
In the next step, the program summarizes for each option the number of times it appeared for a poisonous and non-poisonous mushroom, and with this data performs the probability calculation according to Bayes' law for each and every possibility.

Examination : After the model is trained, the program sends the test array for testing, performs a classification for each element in it, and counts and displays how many times the model gave a higher than fifty percent chance that the mushroom is indeed poisonous or less and the mushroom not poisonous as well as the percentage of success

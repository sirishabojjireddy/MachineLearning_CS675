# MachineLearning_CS675
Machine Learning codes in python during CS675 course period
https://web.njit.edu/~usman/courses/cs675_fall19/index.html

Assignment1:
Python program that implements the Naive Bayes classifier, take as input a dataset file and a set of training labels and produce predicted labels for the test
dataset which are feature vectors whose labels are not given for training, initializing the mean to zero to 0.1.

Assignment2:
Python program that implements gradient descent for minimizing the least squares loss, with stopping condition check for the objective between the current and previous iteration, with same input and output as nearest means and Naive-Bayes.

Assignment3:
Python program for optimizing the SVM hinge loss, same input and output as Assignment2.

Assignment4:
Python program for the logistic discrimination gradient descent algorithm, same input and output as nearest means and Naive-Bayes, without convert 0 to -1 in the labels

Assignment5:
Modify assignments 2 and 3 to do an adaptive eta setting. Between the compute dellf and updatew code portions.

Assignment6:
Python program that determines the column with the best split for the CART decision tree algorithm. Write a program that will traverse all columns in the data and output the column and the threshold that gives the lowest gini index. The input should be the data file and labels as in previous assignments. The output is the column number k and the split value s. Test with XOR example.

Assignment7:
Python program to perform bagging on the decision stump from assignment 6. The input should be the data file and labels as in previous assignments. The output is the prediction of test datapoints. Create a bootstrapped dataset and then run your decision stump on it and obtain predictions labels, repeat this a 100 times and output the majority vote of the predictions. 

Assignment8:
Write a Python program to output a k-means clustering, similar structure to the nearest means program. The input to your program is a dataset and number of cluster k. The output is in the same format of label files.

Assignment9:
Experiment with random hyperplanes for classification. Take a dataset as input and produce new features. The input is in the same format as for previous assignments. Predict using linear SVM and k values of 10, 100, 1000 and 10000, compare error liblinear on original data for each k. Crossvalidate on the first split of each of six datasets, on both original and new data represenation for all values of k. Create features and run linearSVC using scikit learn on new training data and predict on new test data, set max_iter parameter to 10000 for deep search.

Extracredit:
Predict the  final week's sales from the previous values for each item in the weekly sales transaction dataset.

Course Project:
Predicted the labels of 2000 test data whose true labels are unknown.

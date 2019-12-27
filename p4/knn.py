
# Make Predictions with k-nearest neighbors on the Iris Flowers Dataset
from csv import reader
from math import sqrt
import matplotlib.pyplot as plt


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
        del dataset[0]
    return dataset

ranges=list()
def load_train_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
        del dataset[0]
        for i in dataset:
            ranges.append(int(i[-1]))
            del i[-1]
    return dataset
 
# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Convert string column to integer

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax
 
# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])
 
# Calculate the Euclidean distance between two vectors
def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(len(row1)-1):
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)
 
# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors
 
# Make a prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	output_values = [row[-1] for row in neighbors]
	prediction = max(set(output_values), key=output_values.count)
	return prediction
 
# Make a prediction with KNN on Iris Dataset
filename = 'test.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])-1):
	str_column_to_float(dataset, i)
# define model parameter
num_neighbors = 10
# define a new record
row = [1726,0,2.1,0,2,1,63,0.6,85,7,8,1463,1992,2457,19,13,7,1,0,1]
# predict the label
label = predict_classification(dataset, row, num_neighbors)
print('Data=%s, Predicted: %s' % (row, label))

traintable=load_train_csv("train.csv")

for i in range(len(traintable[0])-1):
    str_column_to_float(traintable,i)

accuracies=list()
accuracies.append(0)
for i in range(1,num_neighbors+1):
    predict_array=list()
    correct_predict=0
    for row in traintable:
        label2=predict_classification(dataset,row,i)
        predict_array.append(label2)
        print('For k=%s, Data=%s, Predicted: %s, Actual: %s' % (i,row,label2,ranges[traintable.index(row)]))
    for k in range(len(ranges)):
        if int(predict_array[k])==ranges[k]:
            correct_predict+=1
    a = (correct_predict/len(ranges)*100)
    accuracies.append(round(a,3))

ks=[1,2,3,4,5,6,7,8,9,10]
accuracies.remove(accuracies[0])
pdf = plt.figure()
plt.scatter(accuracies,ks)
plt.grid()
plt.suptitle("Accuracies-K value Plot")
plt.show()
pdf.savefig("plot.pdf", bbox_inches='tight')

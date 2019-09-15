from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np

## Read in data from csv
data = pd.read_csv('kc_house_data.csv')
data = pd.DataFrame(data)

## Removes the unnecessary or not allowed columns
x_train_data = data.drop(['id', 'price', 'lat', 'long','sqft_living15','sqft_lot15'], axis=1)
y_train_data = data['price']
x_test_data = data.drop(['id', 'price', 'lat', 'long','sqft_living15','sqft_lot15'], axis=1)
y_results = data['price']

## Removes the month and day from date
x_train_data['date'] = x_train_data['date'].apply(lambda x : x[-4:])
x_test_data['date'] = x_test_data['date'].apply(lambda x : x[-4:])

## Set up the training and testing sets
x_train = x_train_data[0:21526]
y_train = y_train_data[0:21526]

x_test = x_test_data[-1:]
y_test = y_results[-1::]

custom_question = pd.DataFrame({'date':[2016],'bedrooms':[3], 'bathrooms':[1.5], 'sqft_living':[1500], 'sqft_lot':[1575], 'floors':[2.0], 'waterfront':[0], 
            'view':[0], 'condition':[4], 'grade':[8], 'sqft_above':[1100], 'sqft_basement':[400], 'yr_built':[2008], 'yr_renovated':[0], 'zipcode':[98038]})

# custom_question['date'] = 2016
# custom_question['bedrooms'] = 3
# custom_question['bathrooms'] = 1.5
# custom_question['sqft_living'] = 1500
# custom_question['sqft_lot'] = 1575
# custom_question['floors'] = 2.0
# custom_question['waterfront'] = 0
# custom_question['view'] = 0
# custom_question['condition'] = 4
# custom_question['grade'] = 8
# custom_question['sqft_above'] = 1100
# custom_question['sqft_basement'] = 400
# custom_question['yr_built'] = 2008
# custom_question['yr_rennovated'] = 0
# custom_question['zipcode'] = 98038

# Create and train neural networks
clf = MLPClassifier(solver='adam', alpha=1e-5,
                    hidden_layer_sizes=(5,2), random_state=1)
clf.fit(x_train, y_train)

print(clf.predict(x_test))
print(y_test)

# print(clf.predict(custom_question))
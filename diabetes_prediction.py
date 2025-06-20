import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import warnings
warnings.simplefilter('ignore', UserWarning)

diabetes_dataset=pd.read_csv('/content/diabetes.csv')

diabetes_dataset['Outcome'].value_counts()

diabetes_dataset.groupby('Outcome').mean()

"""Separating Data and Labels"""

A = diabetes_dataset.drop(columns='Outcome',axis=1)
B = diabetes_dataset['Outcome']

"""Data"""

print(A)

"""Labels"""

print(B)

"""Data Standardization"""

scaler=StandardScaler()

standardized_data=scaler.fit_transform(A)

print(standardized_data)

"""Loading the standardized data into A which currently contains the raw data except the column using which we evaluate if a person is diabetic, which is held in B (used to evaluate if a person is diabetic)."""

A=standardized_data

print(A)
print(B)

"""A contains the standardized data, B contains the labels, hence we can proceed

Splitting the standardized data into Training and Test Data
"""

A_train, A_test, B_train, B_test=train_test_split(A, B, test_size=0.1, stratify=B, random_state=1)

"""90% of the data is used to train the model and 10% for testing, stratify is used to make sure that the splitting is done proportionally and not in a manner in which data of the same outcome is contained in either testing or training data.

A_train and A_test contain the standardized data split into training and testing data, whereas B_train and B_test contain the outcomes, using which we evaluate if a person is diabetic, split for training and testing.
"""

print(A.shape, A_train.shape, A_test.shape)

"""Training the model"""

classifier=svm.SVC(kernel='linear')
classifier.fit(A_train, B_train)

"""Model Evaluation

Accuracy Score when tested against training data
"""

A_train_prediction=classifier.predict(A_train)
training_data_accuracy=accuracy_score(A_train_prediction, B_train)
print('Accuracy score of the training data: ', training_data_accuracy)

"""Accuracy Score when tested against testing data"""

A_test_prediction=classifier.predict(A_test)
testing_data_accuracy=accuracy_score(A_test_prediction, B_test)
print('Accuracy score of the testing data: ', testing_data_accuracy)

"""The training data accuracy is about 79% while that of the testing data is only 68%. This may be a sign of overfitting. Only 10% of the data being used for testing and the random_state is 1. We may now edit these values to try and reduce the gap between the accuracy scores of testing and training data."""

A_train, A_test, B_train, B_test=train_test_split(A, B, test_size=0.3, stratify=B, random_state=2)
print(A.shape, A_train.shape, A_test.shape)

A_train_prediction=classifier.predict(A_train)
training_data_accuracy=accuracy_score(A_train_prediction, B_train)
print('Accuracy score of the training data: ', training_data_accuracy)
A_test_prediction=classifier.predict(A_test)
testing_data_accuracy=accuracy_score(A_test_prediction, B_test)
print('Accuracy score of the testing data: ', testing_data_accuracy)

"""We now have a training data accuracy of 78% and testing data accuracy of 79%. We now perform this one more time with a different percentage of training data.

This result is acceptable, but if it occurs many times (accuracy[test]>accuracy[test]) then it might be a sign of data leakage.
"""

A_train, A_test, B_train, B_test=train_test_split(A, B, test_size=0.2, stratify=B, random_state=2)
print(A.shape, A_train.shape, A_test.shape)

A_train_prediction=classifier.predict(A_train)
training_data_accuracy=accuracy_score(A_train_prediction, B_train)
print('Accuracy score of the training data: ', training_data_accuracy)
A_test_prediction=classifier.predict(A_test)
testing_data_accuracy=accuracy_score(A_test_prediction, B_test)
print('Accuracy score of the testing data: ', testing_data_accuracy)

"""We achieve an accuracy score of 78.9% with training data and about 77% with testing data.

Now we provide specific atomic input to the model to check if can predict if the person is diabetic.
"""

input_data=(7,196,90,0,0,39.8,0.451,41)

#fitting the input data into a numpy array
input_data_as_nparray=np.asarray(input_data)


#reshaping as we are predicting for a singular input
input_data_reshaped=input_data_as_nparray.reshape(1,-1)


#standardize the input data
std_data=scaler.transform(input_data_reshaped)
print(std_data)


prediction=classifier.predict(std_data)
print(prediction)

if(prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')

"""The model correctly predicts that the person is diabetic."""

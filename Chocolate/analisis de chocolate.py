import numpy as np
import pandas as pd

datos = pd.read_csv("cocoa final.csv", header=0)
Y = datos.ix[0:]['Rating']
X = (datos.iloc[:,0:2])

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = .5)

from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train,Y_train)

#predictions = my_classifier.predict(X_test)


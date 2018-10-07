import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

#iris.feature son las medidas de las hojas
#iris.target son los tipos de iris (planta)
#iris.data [index que quieras] son las medidas de la planta en especifico de ese index
#iris.target [index que quieras] es el tipo de iris (planta) del index que seleccionaste

# 0 = setosa 1 = versicolor 2 = virginica

test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx) #Esto lo que hace es que guarda en la variable "train_target" TODOS los tipos de plantas, MENOS los que estan en el array "test_idx"
train_data = np.delete(iris.data, test_idx, axis=0)#Hace lo mismo que el de arriba solo que con las medidas de TODAS las plantas

#testing data
test_target = iris.target[test_idx] #Esto guarda en la variable "test_target" las 3 plantas que utilizaremos como prueba
test_data = iris.data[test_idx] #Esto guarda en la variable "test_data" las medidas de las 3 plantas que utlizaremos de prueba

clf = tree.DecisionTreeClassifier() #Esto crea un clasificador de tipo tree en "clf"
clf.fit(train_data,train_target) #Esto dice que buscara patrones con la funcion "fit" en las variables "train_data" y "train_target"

print test_target
print clf.predict(test_data) 
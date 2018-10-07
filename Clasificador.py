from scipy.spatial import distance

def euc(a, b): # A es un punto de la training data y B es un punto de testing data
    return distance.euclidean(a,b) #mide la distancia entre esos dos puntos

class ScrappyKNN(): #crea la nueva clase de clasificador de tipo KNN
    def fit(self, X_train,y_train): #creamos la funcion fit que tiene comp atributos nuestra lista de trainers 
        self.X_train = X_train #"memoriza" la informacion
        self.y_train = y_train #"memoriza" la informacion

    def closest(self,row): #crea la funcion closest que busca el punto mas cercano al 
        
        #Que son Rows?
        #[[1,2],[2,3],[3,4]]
        #[1,2] es la primer row, [2,3] la segunda y [3,4] la tercera y asi sucesivamente 

        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1,len(self.X_train)):
            dist = euc(row,self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

    def predict(self, X_test): #crea la funcion predict que tiene como atributo la informacion que testearemos
        predictions = [] #crea un array vacio para las predicciones
        for row in X_test: 
            label = self.closest(row)
            predictions.append(label) #append sirve para agregar elementos al final de una lista (los elementos son arrays, quieres que solo se agregue elemento por elemento usa extend)

        return predictions
        


from sklearn import datasets#importa la base de datos de iris
iris = datasets.load_iris() #carga la base de datos de iris

X = iris.data #guarda los 150 valores de las flores en X (las cuales tienen 4 medidas) es decir que es un array de 150 arrays con 4 medidas dentro de ellos Ej= [23,40,50,12],[32,43,21,23]... y asi hasta 150
y = iris.target#guarda las 150 flores en Y (las cuales pueden tener 3 tipos)


from sklearn.model_selection import train_test_split #importa la funcion para dividir toda la informacion
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = .5) #divide las 2 variables (X,y) a la mitad, es decir en X_train, X_test, y_train, y_test

#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN() #dice que clasificador vamos a usar

my_classifier.fit(X_train, y_train) #utiliza el clasificador para buscar patrones (en este caso calcula la distancia)

predictions = my_classifier.predict(X_test) #predice la respuesta a la lista de X_test utilizando nuestro clasificador

from sklearn.metrics import accuracy_score #importa la funcion para calcular la precicion
print accuracy_score(predictions, y_test) #imprime la precicion de las respuestas y la predicccion
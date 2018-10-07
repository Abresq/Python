#Autor: DieEsq05

from sklearn import tree

features = [[140,1],[130,1],[150,0],[170,0]] # 1 = Suave  0 = Rugoso
labels = [0,0,1,1] # 0 = Manzana 1 = Naranja

clf = tree.DecisionTreeClassifier()
cld = clf.fit(features,labels)

peso = raw_input("Cual es el peso de tu fruta?\n")
superficie_input = raw_input("cual es la superficie de tu fruta\n")

if superficie_input == "suave" or "Suave":
    superficie = 1

elif superficie_input == "rugosa" or "Rugosa":
    superficie = 0

else:
    print "Esa no es una superficie valida, habran errores."

prediccion = cld.predict([[peso,superficie]])

if prediccion == 0:
    print "Tu fruta es una Manzana"
else :
    print "Tu fruta es una Naranja"

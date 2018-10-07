from sklearn import tree


features = [[1,3],[1,4],[0,1],[0,1]] 
labels = [3000,3500,200,300]

clf = tree.DecisionTreeClassifier()
cld = clf.fit(features,labels)

print cld.predict([[1,1]])
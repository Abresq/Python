# encoding: utf-8

import pandas as pd
datos = pd.read_csv("cocoa.csv", header=0)

#print (datos)
x = datos.ix[0:]['Rating']
#print (datos.sort_values(by='Rating',ascending = False))
y = (datos.iloc[:,1])

print x
print y
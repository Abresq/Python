#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#Script para sustituir palabras y carácteres de un archivo de texto plano

original = open('cocoa.csv', 'r')
final = open('final.csv',"w")

diccionario = [
("A. Morin", "0"), 
("Acalli", "1"), 
("Adi", "2"),
("Aequare (Gianduja)","3"),
("Ah Cacao","4"),
("Akesson's (Pralus)","5"),
("Alain Ducasse","6"),
("Alexandre","7"),
("Altus aka Cao Artisan","8"),
("Amano","9"),
("Amatller (Simon Coll)","10"),
("Ambrosia","11"),
("Amedei","12"),
("AMMA","13"),
("Animas","14"),
("Ara","15")

]

data = original.read()
original.close()
salida = reduce(lambda a, kv: a.replace(*kv), diccionario, data)
final.write(salida)
final.close()  
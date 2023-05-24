import shapefile
sf = shapefile.Reader("poly.shp")
print(sf.fields)
enregistrements = sf.shapeRecords()
#Affichage des points
print(enregistrements[0].shape.points)
#[(-71.20156440919199, 46.81686875991673), (-71.2027021978781, 46.80690142700209), ...
#Affichage des données tabulaires
print(enregistrements[0].record)
#Record #0: [None, 'Vieux Qc']

#Écriture
w = shapefile.Writer("creation.shp",shapeType=1)
w.autoBalance = 1 #Pour balancer le nombre d'entité et d'enregistrement
w.field('Nom', 'C')#Création du champ
w.field('Pop', 'N')#Création du champ
w.record("Québec", 600000)#Ajout de la valeur
w.point(-71, 46)#Ajout de la géométrie
#Pour un polygone
#w.poly(shapeType=3, parts=[[[122,37,4,9], [117,36,3,4]], [[115,32,8,8],
#... [118,20,6,4], [113,24]]])
w.close()


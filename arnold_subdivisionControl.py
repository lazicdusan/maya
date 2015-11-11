import pymel.core as pm
#select the top geo_C_001_GRUP and run this python to get all the subobjects to catclark 1:
for mesh in pm.listRelatives(pm.selected(),c=1,ad=1,typ='shape'):
	mesh.aiSubdivType.set(1)
	mesh.aiSubdivIterations.set(1)

#select the top geo_C_001_GRUP and run this python to get all the subobjects to catclark 2:
for mesh in pm.listRelatives(pm.selected(),c=1,ad=1,typ='shape'):
	mesh.aiSubdivType.set(1)
	mesh.aiSubdivIterations.set(2)
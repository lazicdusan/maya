import maya.cmds as cmds
import pymel.core as pm

#search for the name through all the files
def searchReplace(searchVar,newVar):
	#search for searchVar and add * to both ends
	allObjects = cmds.ls('*' + searchVar + '*')
	for a in allObjects:
		try:
			#rename a >> a replaced with the newVar
		    cmds.rename(a,a.replace(searchVar, newVar))
		except RuntimeError:
		    pass

#searchReplace('pSphere','_senfara_')
#mayapy D:\\Dusan\\Stvaralastvo\\Skripte\\mayapySetup.py
import sys
sys.path.append('C:\\solidangle\\mtoadeploy\\2016\\scripts')
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds
import pymel.core as pm
cmds.loadPlugin('mtoa')
import maya.cmds as cmds
import pymel.core as pm
import random

def makeSelSets():
    #make selection sets and break the current groups
    if len(cmds.ls(sl=1)) ==0:
        cmds.warning ('FECK! nothing is selected')
    else:
        def groupsToSets(groupName, setName):
            cmds.sets(cmds.listRelatives(groupName,c=1),n=setName)
        
        groupsToSets('krov','krovSet')
        groupsToSets('metal','metalSet')
        groupsToSets('zid','zidSet')
        groupsToSets('okviri','okviriSet')
        groupsToSets('okviriSvetla','okviriSvetlaSet')
        
        #unparent everything - select all transforms and parent -w;
        allT=cmds.ls(sl=1)
        cmds.parent (allT, w=1)
        
        #delete all groups in the scene
        transforms =  cmds.ls(type='transform')
        deleteList = []
        for tran in transforms:
            if cmds.nodeType(tran) == 'transform':
                children = cmds.listRelatives(tran, c=True) 
                if children == None:
                    print '%s, has no childred' %(tran)
                    deleteList.append(tran)
                    
        cmds.delete(deleteList)
        
        #make new groups
        cmds.group(empty=True, name = "prvaStrana")
        cmds.group(empty=True, name = "drugaStrana")
        cmds.group(empty=True, name = "sredina")
        cmds.group(empty=True, name = "dimnjak")
        cmds.group(empty=True, name = "nadKrov")

def fixShaders():
    #fix diffuse
    cmds.setAttr('diffuseWeightSetRange' + '.minX',0.85)
    cmds.setAttr('diffuseWeightSetRange' + '.maxX',1)
    #fix metals
    allMetals = cmds.ls('metalShader*')
    for m in allMetals:
        cmds.setAttr(m+'.Ksn', 0.02)

def makeMeshLights():
    #make mesh lights attributes in selected meshes
    for meshLight in cmds.ls(sl=1):
        cmds.setAttr(meshLight + '.aiExposure',17)
        cmds.setAttr(meshLight + '.lightVisible',1)
        cmds.setAttr(meshLight + '.color',1, 0.931079, 0.776)

def exportHouse():
    #select group and okviriSvetlaSet
    cmds.select('kuca*')
    cmds.select('okviriSvetlaSet',add=1,ne=1)
    #if there's any cameras delete them
    cams = cmds.listRelatives(cmds.ls(sl=1),type='camera',c=1,ad=1)
    if cams:
        for cam in cams:
            #get the transform of the camera
            trns = cmds.listRelatives(cam,type='transform',p=1)
            cmds.delete(trns)
        else:
            pass
    #save the file
    cmds.file(s=1)
    #get the name of the scene
    sceneName = cmds.file(q=1,sn=1,shn=1)
    #make the new path into the exported directory
    filePath = 'D:\\Dusan\\Stvaralastvo\\Grad\\mod\\houses\\exported\\'
    #export the scene
    cmds.file(filePath + 'rand_4'+ sceneName,es=1,f=1,type='mayaAscii')

#randomize color for all three textures
def randomizeColor():
    cmds.setAttr('diffuseTintBrighter.colorEntryList[1].color', random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0))
    cmds.setAttr('diffuseTintBrightestAndWhite.colorEntryList[1].color', random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0))
    cmds.setAttr('diffuseTint.colorEntryList[1].color', random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0))

#new prop routine
def importProps():
    newProp = pm.selected()[0]
    newProp.centerPivots()
    newProp.scaleX.set(137)
    newProp.scaleY.set(137)
    newProp.scaleZ.set(137)

#the scene is created with one argument: naming of the asset
def exportProps(naming):
    #save the file
    cmds.file(s=1)
    #make the new path into the exported directory
    filePath = 'D:\\Dusan\\Stvaralastvo\\Grad\\mod\\props\\exported\\'
    #export the scene with naming as the argument
    cmds.file(filePath + naming,es=1,f=1,type='mayaAscii')
def checkSelectionProps():
    #check if nothing is selected, then export all props
    if len(cmds.ls(sl=1))==0:
        #select the group
        cmds.select('props')
        #get the list of the bottom groups
        allProps = cmds.listRelatives('props',c=1)
        #export them
        for prop in allProps:
            cmds.select(prop,r=1)
            exportProps(prop)
    #else export just the selected one
    else:
        #get the name of the selected asset
        selectedProp = pm.selected()[0]
        #export it
        exportProps(selectedProp)


#make mesh lights and animate attributes for windows
def animateWindowLights():
    winLights = cmds.listRelatives('okviriSvetlaSet', c=1)
    #iterate through all the mesh lights
    for winLight in winLights:
        y_random = random.randint(0,1)
        if y_random == 1:
            try:
                #make them a mesh light
                cmds.setAttr(winLight + '.aiTranslator','mesh_light',type='string')
            except RuntimeError:
                print "not given..."
            try:
                #get the random frame range where lights should animate
                #lights turn off at this time
                randomFrameOff = random.randrange(530,620)
                step = 1
                randomFrameOn = randomFrameOff + step
                #lights turn on at this time
                randomFrameOn2 = random.randrange(700,800)
                randomFrameOff2 = randomFrameOn2 + step
                #set attributes for light turned off
                pm.setAttr(winLight + '.intensity',0)
                pm.setAttr(winLight + '.aiExposure',0)
                pm.setAttr(winLight + '.lightVisible',1)
                pm.setAttr(winLight + '.color',1, 0.897, 0.667)
                keyableAttributes = ['aiExposure','intensity']
                #keyframe it
                pm.setKeyframe(winLight,at=keyableAttributes,t=randomFrameOff)
                #set attributes for light turned on
                pm.setAttr(winLight + '.intensity',1)
                pm.setAttr(winLight + '.aiExposure',15)
                #keyframe it
                pm.setKeyframe(winLight,at=keyableAttributes,t=randomFrameOn)
                #keyframe the other time when it's time to turn off
                pm.setKeyframe(winLight,at=keyableAttributes, t=randomFrameOn2)
                #turn the lights off
                pm.setAttr(winLight + '.intensity',0)
                pm.setAttr(winLight + '.aiExposure',0)
                #keyframe it
                pm.setKeyframe(winLight,at=keyableAttributes, t=randomFrameOff2)
                print 'made a mesh light out of this light!!!'
            except RuntimeError:
                pass
        else:
            pass

def duplicateNames():    
    #kill duplicate names
    objs = [x for x in cmds.ls(shortNames=True) if '|' in x]
    objs.sort(key=lambda x : x.count('|'))
    objs.reverse()
    for i in range(len(objs)):
        cmds.rename(objs[i], objs[i].replace('|', ''))

    # proof
    if not len([x for x in cmds.ls(shortNames=True) if '|' in x]):
        print 'no non-unique names'

def renameMeshes():
    kuca=cmds.listRelatives('kuca*',c=1)
    for k in kuca:
        children=cmds.listRelatives(k,c=1,ad=1)
        for child in children:
            cmds.rename(child, k)

def shaderSwitch(oldShader,newShader):
    shadingGroup = cmds.listConnections(oldShader,type='shadingEngine')
    shadingGroupConn = cmds.listConnections(shadingGroup,type='shape')
    mySG = cmds.sets(renderable=1, noSurfaceShader=1, empty=1, name=newShader + '_SG')
    cmds.connectAttr((newShader+'.outColor'),(mySG + '.surfaceShader'),f=1)
    try:
        for con in shadingGroupConn:
            cmds.sets(con, e=1, forceElement = mySG)
    except TypeError:
        pass

def newShadersImport():
    cmds.file("D:\Dusan\Stvaralastvo\Grad\scenes\shd2.ma", i=True, f=True)

def animatePropLights():
    allPropLights=cmds.ls('propLight*')
    for propLight in allPropLights:
        try:
            #make them a mesh light
            cmds.setAttr(propLight + '.aiTranslator','mesh_light',type='string')
        except RuntimeError:
            print "not given..."
        try:
            #get the random frame range where lights should animate
            #lights turn off at this time
            randomFrameOff = random.randrange(530,535)
            step = 20
            randomFrameOn = randomFrameOff + step
            #lights turn on at this time
            randomFrameOn2 = random.randrange(900,905)
            randomFrameOff2 = randomFrameOn2 + step
            #set attributes for light turned off
            pm.setAttr(propLight + '.intensity',0)
            pm.setAttr(propLight + '.aiExposure',0)
            pm.setAttr(propLight + '.lightVisible',1)
            #pm.setAttr(propLight + '.color',1, 0.897, 0.667)
            keyableAttributes = ['aiExposure','intensity']
            #keyframe it
            pm.setKeyframe(propLight,at=keyableAttributes,t=randomFrameOff)
            #set attributes for light turned on
            pm.setAttr(propLight + '.intensity',1)
            pm.setAttr(propLight + '.aiExposure',10)
            #keyframe it
            pm.setKeyframe(propLight,at=keyableAttributes,t=randomFrameOn)
            #keyframe the other time when it's time to turn off
            pm.setKeyframe(propLight,at=keyableAttributes, t=randomFrameOn2)
            #turn the lights off
            pm.setAttr(propLight + '.intensity',0)
            pm.setAttr(propLight + '.aiExposure',0)
            #keyframe it
            pm.setKeyframe(propLight,at=keyableAttributes, t=randomFrameOff2)
            print 'made a mesh light out of this light!!!'
        except RuntimeError:
            pass

def animateSpotLights():
    spotLights=cmds.ls(type='spotLight')
    for spotL in spotLights:
        #lights turn off at this time
        randomFrameOff = random.randrange(530,535)
        step = 20
        randomFrameOn = randomFrameOff + step
        #lights turn on at this time
        randomFrameOn2 = random.randrange(900,905)
        randomFrameOff2 = randomFrameOn2 + step
        #set attributes for light turned off
        pm.setAttr(spotL + '.intensity',0)
        pm.setAttr(spotL + '.aiExposure',0)
        pm.setAttr(propLight + '.color',1, 0.897, 0.667)
        keyableAttributes = ['aiExposure','intensity']
        #keyframe it
        pm.setKeyframe(spotL,at=keyableAttributes,t=randomFrameOff)
        #set attributes for light turned on
        pm.setAttr(spotL + '.intensity',1)
        pm.setAttr(spotL + '.aiExposure',10)
        #keyframe it
        pm.setKeyframe(spotL,at=keyableAttributes,t=randomFrameOn)
        #keyframe the other time when it's time to turn off
        pm.setKeyframe(spotL,at=keyableAttributes, t=randomFrameOn2)
        #turn the lights off
        pm.setAttr(spotL + '.intensity',0)
        pm.setAttr(spotL + '.aiExposure',0)
        #keyframe it
        pm.setKeyframe(spotL,at=keyableAttributes, t=randomFrameOff2)
        print 'spot is animated out of this light!!!'
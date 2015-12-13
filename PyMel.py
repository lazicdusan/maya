#make a variable for PyNode
ASSET='*_C_*_*_*'
#pm PyNode 01
CUSTOMPYNODE = pm.PyNode(ASSET)

#make the empty group with the cameras
cameraGroup = pm.group(n="custom_group", em=True)
# create a camera and set the focal length
renderCam = pm.createNode("camera")
renderCam.getParent().rename("turntable_camera")
renderCam.focalLength.set(50)
renderCam.getParent().setParent(cameraGroup)
renderCam.displayResolution.set(True)
renderCam.getParent().tz.set(camDistance) #camDistance is calculated elsewhere

# make a sphere and set its attributes
matteSphGeo = pm.polySphere(n='sphere_matte',r=0.015,ch=0,cuv=1)
pm.setAttr('sphere_matte.t',(0.162,-0.121,-0.729))
#this resets transformations
pm.makeIdentity(matteSphGeo,t=1,r=1,s=1,a=1)
#makes the sphere a child of a group previously made
pm.parent(matteSphGeo,'turntable_camera')

#get the bounding box of the asset
allGrpBoundingBox = CUSTOMPYNODE.boundingBox()
#get cented, depth and width of the bounding box
allGrpBoundingBox.center()
allGrpBoundingBox.depth()
allGrpBoundingBox.width()
#move the asset to the center of the bounding box
CUSTOMPYNODE.setTranslation(allGrpBoundingBox.center())

# create the Light Setup
#custom arnold directional light
lightsGroup = pm.group(n="light_group", em=True)
keyLight = pm.shadingNode('directionalLight',al=True,name='key_light')
keyLight.translate.set(-5.002,4.155,0.002)
keyLight.rotate.set(-76.186,-43.135,25.961) 
keyLight.color.set((1,0.99,0.95))
keyLight.aiExposure.set(2.5)
keyLight.aiAngle.set(10.000)
keyLight.aiShadowDensity.set(1)
keyLight.aiVolumeSamples.set(2)
keyLight.setParent(lightsGroup)

#custom arnold skydome light
domeLight = pm.shadingNode('aiSkyDomeLight',al=True,name='dome_light')  
domeLight.intensity.set(1)
domeLight.aiSamples.set(4)
domeLight.setParent(lightsGroup)

#animate the asset rotating it for 360 degrees
CUSTOMPYNODE.setParent(animateGroup)
animateGroup.ry.setKey(t=1001, outTangentType="linear", inTangentType="linear") 
animateGroup.ry.setKey(t=1059 + 1, v=360, outTangentType="linear", inTangentType="linear")

# create the ground plane
ground = pm.polyPlane(w=60,h=60,name='ground_plane',ch=0)
pm.setAttr('ground_plane.primaryVisibility',0)

# look through the render cam
try :
    pm.mel.lookThroughModelPanel("turntable_camera", "modelPanel4")
except : pass

# lock and Hide multiple attrs
objects=['sphereMatte','sphereShiny','sphereChrome','groundPlane','turntableCam','key_light']
attrToHide = ['.translateX','.translateY','.translateZ','.rotateX',
'.rotateY','.rotateZ','.scaleX','.scaleY','.scaleZ']

for obj in objects :
    for attrs in (attrToHide):     
        cmds.setAttr(trans+attrs,keyable=0,cb=0,lock=1)

# global render settings
renderGlobals = pm.PyNode("defaultRenderGlobals")
renderGlobals.animation.set(True)
renderGlobals.extensionPadding.set(4)
renderGlobals.animationRange.set(0)
renderGlobals.startFrame.set(1)
renderGlobals.endFrame.set(60)
renderGlobals.putFrameBeforeExt.set(1)

# set the ouput resolution
defaultResolution = pm.PyNode("defaultResolution")
defaultResolution.width.set(1920)
defaultResolution.height.set(1080)
defaultResolution.deviceAspectRatio.set(1.777777)

#change render to arnold
pm.mel.eval("setCurrentRenderer arnold")

# create the default arnold node.
mtoa.core.createOptions()
  
# arnold render settings
#PyNode 02
arnoldRenderGlobal = pm.PyNode("defaultArnoldRenderOptions")
arnoldRenderGlobal.AASamples.set(5)
arnoldRenderGlobal.GIDiffuseSamples.set(1)
arnoldRenderGlobal.GIGlossySamples.set(1)
arnoldRenderGlobal.GIRefractionSamples.set(1)
arnoldRenderGlobal.display_gamma.set(1.0)
arnoldRenderGlobal.light_gamma.set(2.2)
arnoldRenderGlobal.shader_gamma.set(2.2)
arnoldRenderGlobal.texture_gamma.set(2.2)
      
# set output format to exr
defaultArnoldDriver = pm.PyNode("defaultArnoldDriver")
defaultArnoldDriver.aiTranslator.set("exr")
  
# set colorSpace to Linear
pm.setAttr('defaultViewColorManager.imageColorProfile',2)
pm.setAttr('defaultViewColorManager.displayColorProfile',3)

# assign Shaders
# Matte Sph Shader
matteSphSG = pm.sets(renderable=True,noSurfaceShader=True,empty=True,name='sphere_matte_sg')
matteSph = pm.shadingNode('aiStandard',asShader=True,name='sphere_matte_shader')
matteSph.color.set((0.5,0.5,0.5))
matteSph.Kd.set(1)
matteSph.diffuseRoughness.set(0.350)
matteSph.Ks.set(0)
matteSph.specularRoughness.set(0.467)
matteSph.IOR.set(1.0)
matteSph.sssRadius.set(0.1,0.1,0.1)
pm.connectAttr('sphere_matte_shader.outColor','sphere_matte_sg.surfaceShader')          
cmds.sets('sphere_matte',e=True, forceElement= matteSph + 'SG')

#get attributes from cameras one way
camName=pm.ls('CAM:*',type='camera',ap=True)
fl=pm.getAttr(camName[0].fl)
hfa=pm.getAttr(camName[0].hfa)
vfa=pm.getAttr(camName[0].vfa)
ncp=pm.getAttr(camName[0].ncp)
fcp=pm.getAttr(camName[0].fcp)

#get attributes the other way
transform =  mesh.getParent()
tx = transform.translateX.get()
ty = transform.translateY.get()
tz = transform.translateZ.get()

rx = transform.rotateX.get()
ry = transform.rotateY.get()
rz = transform.rotateZ.get()

sx = transform.scaleX.get()
sy = transform.scaleY.get()
sz = transform.scaleZ.get()

#get first and last frame of the shot 
minTime=pm.playbackOptions(q=True,minTime=True)
maxTime=pm.playbackOptions(q=True,maxTime=True)

#try this with camTrans, cam assigning of two variables 
camTrans, cam = pm.camera()  # create a new camera
cam.setFocalLength(100)
fov = cam.getHorizontalFieldOfView()
cam.dolly(-3)
cam.track(left=10)
cam.addBookmark('new')

'''
In PyMEL, all you have to do is type help(nt.Camera) in the python script
editor to find out all the things a camera node can do, or just look up 
the Camera class in the PyMEL docs.
'''

#find out if some of the multiple objects exist
if pm.ls(["foo", "bar", "baz"]):
    print "at least one exists"

#find out if all objects exist
names = ["foo", "bar", "baz"]
found = pm.ls(names)
if len(found) == len(names):
    print "all objects exist"

#deal with the objects which exist
items = ["foo", "biz", "baz"]
for item in items:
    if cmds.objExists(item):
        print item, "exists"
    else:
        print item, "does not exist"
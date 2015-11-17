import maya.cmds as cmds
import pymel.core as pm

#make the shader and all the connections
#make the path to follow for the textures
#make the ui in which you'll have to specify your asset type so it has all the correct ids and which maps you want 
#assign the shader to the existing meshes, check if there's already something assigned and break it if it is

#get all the selected objects and their relatives
selected = pm.selected()[0]
children = selected.listRelatives(c=1,ad=1,typ='transform')
shapes = selected.listRelatives(c=1,ad=1,typ='shape')
#error if nothing is selected or if group/geometry are not selected
if not children:
    pm.warning ('the selection is not the group node')

#get the name of the file and put it in minors and delete the numbers
#/srv/projects/deep/work/assets/prop/HTCH02
sceneName = pm.sceneName()
assetName = sceneName.split('/')[2]
assetNameLow = assetName.lower() #will need 6 for workPath
shaderName = ''.join([i for i in assetNameLow if not i.isdigit()])
#check textures first, what is there and error if nothing is in 
#/mnt/localh/mari/tmp/dusan/deep/work/assets/prop/HTCH02/lookDev/textLod2/dusan/mari/images/base/DIF/latest/exr/
userName = sceneName.split('/')[3] #will need an exact path but 9 should work
texturePath = 'mnt/localh/mari/tmp/' + userName + '/deep/work/assets/prop/' + assetName + '/lookDev/textLod2/' + userName + '/mari/images/base/'
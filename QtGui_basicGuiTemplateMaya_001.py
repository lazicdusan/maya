from PySide import QtGui
import maya.OpenMayaUI as mui
import shiboken

def button01_function():
    cmds.polySphere()

def button02_function():
    print 'Tijana'

def getMayaWindow():
    pointer = mui.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)

def MasterUI():
    objectName = 'pyConstraintMasterWin'
    
    #check to see if the UI already exists and if so, delete
    if cmds.window('pyConstraintMasterWin',exists = 1):
        cmds.deleteUI('pyConstraintMasterWin', wnd = 1)
    
    #create the window
    parent = getMayaWindow()
    window = QtGui.QMainWindow(parent)
    window.setObjectName(objectName)
    window.setWindowTitle('Lighters little helper')
    
    #create the main widget
    mainWidget = QtGui.QWidget()
    window.setCentralWidget(mainWidget)
    
    #create main vertical layour
    verticalLayout = QtGui.QVBoxLayout(mainWidget)
    
    #create a button01
    button01 = QtGui.QPushButton('Create pSphere')
    verticalLayout.addWidget(button01)
    button01.setMinimumSize(200,40)
    button01.setMaximumSize(200,40)
    button01.clicked.connect(button01_function)

    #create a button02
    button02 = QtGui.QPushButton('Tijana')
    verticalLayout.addWidget(button02)
    button02.setMinimumSize(200,40)
    button02.setMaximumSize(200,40)
    button02.clicked.connect(button02_function)
    
    #show the window
    window.show()

MasterUI()
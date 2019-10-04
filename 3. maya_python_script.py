import maya.cmds as maya

int = 4

def createRailing(numOfRails):
    
    # Create slanted top cylinder
    cmds.polyCylinder(r=0.12, h=9, n='topCyl')
    cmds.rotate('64deg',0,0)
    cmds.move(0,2.5,2)

    # Create bottom cylinders
    for i in range(0,3):   
        cmds.polyCylinder(r=0.1, h=3, n='myCyl#')
        cmds.move(0,i,i*2)

    # Combine all polygons created to form a railing and rotate   
    rail = cmds.polyUnite('topCyl','myCyl1','myCyl2','myCyl3', n='railing')
    cmds.move( -28, 2.464, 18.7 )
    cmds.rotate(0, '180deg',0)
    
    for x in range (0,numOfRails):
        cmds.instance()
        
        if x <1:          
            cmds.move( -28, 2.464, 18.7 )
            cmds.rotate(0, '180deg',0)
		
        else:
            cmds.move( 17, 2.873, 4)
            cmds.rotate(0, '-90deg', 0)
  
createRailing(int)
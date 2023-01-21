import bpy   
import numpy as np


# move all objects into layer 10 (should just be lamp, camera and block)
obs = bpy.context.scene.objects
for ob in obs:
    ob.layers[9] = True
    ob.layers[0] = False


natoms = 10
boxl = 10
positions = np.random.random((natoms,3))*boxl - 0.5*boxl

# create atoms
for i in range(natoms):
  bpy.ops.mesh.primitive_uv_sphere_add(segments=32, size=0.3, location=positions[i])
  bpy.ops.object.shade_smooth()
  
print ("Hello world!")
# set key frames
ifrme = 0 
nfrme = 10
dfrme = 5 

for i in range(nfrme):
    ifrme += dfrme
    bpy.context.scene.frame_set(ifrme)
    
    # update positions
    j = 0 
    obs = [ob for ob in bpy.context.scene.objects if ob.layers[0]]
    for ob in obs:    
        #bpy.context.scene.objects.active = ob
        if j < natoms:
            ob.location[0] += np.random.random() - 0.5 
            ob.location[1] += np.random.random() - 0.5 
            ob.location[2] += np.random.random() - 0.5 
            ob.keyframe_insert(data_path="location")
        j += 1




## get all objects on second layer
#objs = [ob for ob in bpy.context.scene.objects if ob.layers[1]]
#
## set active object to myob
#myob = bpy.data.objects['Sphere'] # or objs[0]
#bpy.context.scene.objects.active = myob
#
# I cant figure out how to set the interpolation type from within a script, I suppose I'll just have to set it manually from within the Blender GUI
# bpy.obs.action.interpolation_type(type='CONSTANT')
# bpy.obs.action.interpolation_type(type='LINEAR')
# bpy.obs.action.interpolation_type(type='BEZIER')

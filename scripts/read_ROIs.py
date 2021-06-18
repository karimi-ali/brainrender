import os
from pathlib import Path

from brainrender import Scene, actor, Animation

from rich import color, print
from myterial import orange
from vedo import Volume, io, load, show
import numpy as np

import util
# path names and roi names
paths = util.get_paths()
roi_names = util.roi_names()
print(f"[{orange}]Running example: {Path(__file__).name}")

# Create a brainrender scene
scene = Scene(title="Injection ROIs", atlas_name='allen_mouse_10um')

mesh_names = [os.path.join(paths['data'], 'meshes', f'{roi}.obj') for roi in roi_names]
meshes = [load(cur_name) for cur_name in mesh_names]
colors = ['#6DB546', '#C30017', '#9D9D9C']
for cur_idx, cur_mesh in enumerate(meshes):
    cur_actor = actor.Actor(cur_mesh, 
                            name=roi_names[cur_idx],
                            color=colors[cur_idx],
                            alpha=0.8)
    scene.add(cur_actor)
    scene.add_silhouette(cur_actor)

# You can specify color, transparency...
# scene.add_brain_region("VISp", "MOs", alpha=0.2, color="green")

# Render!
#scene.render(camera='sagittal', zoom=2.0)
scene.screenshot(name=os.path.join(paths['data'], 'saggital_screenshot.png'))
# Animation

anim = Animation(scene, paths['data'], "ROI_inj_animation")
# Specify camera position and zoom at some key frames
# each key frame defines the scene's state after n seconds have passed
anim.add_keyframe(0, camera="top", zoom=0.7)
anim.add_keyframe(1, camera="sagittal", zoom=0.5)
anim.add_keyframe(2, camera="frontal", zoom=0.7)
anim.add_keyframe(
    3,
    camera="frontal",
)
# Make videos
anim.make_video(duration=3, fps=10)
import os
from pathlib import Path
import brainrender
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
alpha_rois = 0.6
for cur_idx, cur_mesh in enumerate(meshes):
    cur_actor = actor.Actor(cur_mesh, 
                            name=roi_names[cur_idx],
                            color=colors[cur_idx],
                            alpha=alpha_rois)
    scene.add(cur_actor)
    scene.add_silhouette(cur_actor)

# You can specify color, transparency...
# scene.add_brain_region("CTX", alpha=0.2, color="green")

# Render and save screen shots
screen_shot_dir = os.path.join(paths['data'], 'screen_shots')
os.makedirs(screen_shot_dir, exist_ok = True) 
camera_names = list(brainrender.camera.cameras.keys())
zoom_vals = [2.0, 0.8, 1.0, 1.0, 1.0, 1.0]
for idx, c in enumerate(camera_names):
    scene.render(camera=c, zoom=zoom_vals[idx], interactive=False)
    scene.screenshot(name=os.path.join(screen_shot_dir, f'{c}_alpha_{alpha_rois}.png'))

# Animation
animate_flag = True
if animate_flag: 
    anim = Animation(scene, screen_shot_dir, "ROI_inj_animation",size="3240x2100")
    # Specify camera position and zoom at some key frames
    # each key frame defines the scene's state after n seconds have passed
    anim.add_keyframe(0, camera="top", zoom=0.3)
    anim.add_keyframe(5, camera="sagittal", zoom=1.0)
    anim.add_keyframe(9, camera="frontal", zoom=1.0)
    anim.add_keyframe(
        10,
        camera="frontal",
    )
    # Make videos
    anim.make_video(duration=10, fps=10)
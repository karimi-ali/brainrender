from pathlib import Path
from brainrender import Scene

from rich import print
from myterial import orange
from vedo import Volume
import numpy as np

print(f"[{orange}]Running example: {Path(__file__).name}")
f_name = '/Users/karimia/code/alik/+corExp/temp/injection_site_annotations/NPY/vol_orig.npy'

# Create a brainrender scene
scene = Scene(title="brain regions", atlas_name='allen_mouse_10um')
data = np.load(f_name)
vol = Volume(data, spacing=[10,10,10])
mesh = vol.isosurface()
scene.add(mesh)

# You can specify color, transparency...
scene.add_brain_region("CA1", alpha=0.2, color="green")

# Render!
scene.render()
import os
from vedo import Volume, io
import numpy as np
import util
# Read the data
paths = util.get_paths()
f_name = os.path.join(paths['NPY'], 'vol_orig.npy')
data = np.load(f_name)
roi_names = util.roi_names()

for i in [1, 2, 3]:
    cur_data = np.copy(data)
    cur_data[cur_data != i] = 0
    # extract isosurface
    vol = Volume(cur_data, spacing=[10, 10, 10], alpha=0.2, shade=True)
    mesh = vol.isosurface()
    # write the mesh (OBJ) file
    out_name = os.path.join(paths['data'], 'meshes', f'{roi_names[i-1]}.obj')
    io.write(mesh, out_name)
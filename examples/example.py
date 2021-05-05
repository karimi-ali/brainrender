from brainrender import Scene

scene = Scene(atlas_name="allen_mouse_10um")
scene.add_brain_region("ZI", "SCm")
scene.render()
from brainrender import Scene

from rich import print
from myterial import orange
from pathlib import Path

print(f"[{orange}]Running example: {Path(__file__).name}")

# Create a brainrender scene
scene = Scene(title="brain regions")

# Add brain regions
scene.add_brain_region("TH")

# You can specify color, transparency...
scene.add_brain_region("SSp-tr", alpha=0.2, color="green")
scene.add_brain_region("PTLp", alpha=0.2, color="red")

# Render!
scene.render()

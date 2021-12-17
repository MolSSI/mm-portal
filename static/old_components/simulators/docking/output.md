# Extract output
scores, poses = dockOutput.scores, dockOutput.poses

# Validate output
from mmelemental.models.sim.docking import DockOutput
DockOutput(**dockOutput.dict())
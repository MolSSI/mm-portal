# Import docking simulation component for autodock vina
from mmic_autodock.components.autodock_component import AutoDockComponent

# Run autodock vina
dockOutput = AutoDockComponent.compute(dockInput)

# Extract scores + ligand poses
scores, ligands = dockOutput.scores, dockOutput.ligands
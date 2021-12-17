# Import MM molecule data model
from mmelemental.models.molecule import Molecule

# Construct MMSchema molecules
receptor_data   = Molecule.from_file(pdb_file)
ligand_data     = Molecule.from_data(smiles_code)

# Import docking data input model
from mmelemental.models.sim.docking import DockInput

# Construct docking input data from MMSchema molecules
dockInput = DockInput(ligand=ligand_data, receptor=receptor_data)
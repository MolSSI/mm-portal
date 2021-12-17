# Import the param input and molecule models that comply with MMSchema
from mmic_ffpa.models.input import ParamInput
from mmelemental.models.molecule import Molecule

# Create MMSchema molecule
mol = Molecule.from_file(path_to_file)

# Create input for Amber99 FF (optionally) using the GMX engine
paramInput = ParamInput(mol=mol, forcefield='amber99', engine='gmx')
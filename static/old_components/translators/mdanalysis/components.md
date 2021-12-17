# Import translation input model
from mmic_translator.models import TransInput

# Create input for converting Mda to MMSchema molecule
from_mda = TransInput(
        tk_object = MDAnalysis.Universe,
        tk_units = mmic_mda.units
)

# Run conversion
mm_mol = MdaToMolComponent.compute(from_mda)

# Create input for converting MMSchema to Mda molecule
from_mm = TransInput(
        schema_object = MDAnalysis.Universe,
        tk_version = '>=1.0.0'
)

# Run conversion
mm_mol = MdaToMolComponent.compute(from_mda)
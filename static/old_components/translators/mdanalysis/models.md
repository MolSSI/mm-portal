# Import models for MDAnalysis
from mmic_mda.models import MdaMol, MdaFF, MdaTraj

# Create mda objects from MMSchema models
mda_mol = MdaMol.from_schema(mm_mol)
mda_ff = MdaFF.from_schema(mm_ff)
mda_traj = MdaTraj.from_schema(mm_traj)

# Convert mda objects to MMSchema models
mm_mol = mda_mol.to_schema()
mm_ff = mda_ff.to_schema()
mm_traj = mda_traj.to_schema()
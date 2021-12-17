# Import main component for running the computation
from mmic_ffpa.components import FFPAComponent

# Run the FF param assignment component
paramOutput = FFPAComponent.compute(paramInput)

# Extract MMSchema mol and and its associated ff object
mol, ff = paramOutput.mol, paramOutput.ff
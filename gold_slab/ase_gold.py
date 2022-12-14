from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import fcc111, add_adsorbate
from ase.io import write
from ase.visualize import view


h = 3.5
d = 5.0

slab = fcc111('Au', size=(3, 3, 3), vacuum=20.0)
add_adsorbate(slab, 'He', h, position=(5.5,3.5))
write('slab1.xyz', slab)
#view(slab)

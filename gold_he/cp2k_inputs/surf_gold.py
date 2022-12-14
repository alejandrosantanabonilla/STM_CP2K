from ase.build import fcc111, add_adsorbate, surface
from ase.io import write

#slab= surface('Au', (1, 1, 1), 3)
slab = fcc111('Au', size=(2,2,3))
add_adsorbate(slab, 'H', 6.5, 'ontop')
slab.center(vacuum=10.0, axis=2)
write('slab.cif', slab)

from ase import io
from ase.io import write
from ase.visualize import view
from ase.build import add_adsorbate
import numpy as np


def slab_creation(h):
    h = 4.25

    slab = io.read('last.cif')
    old_pos = np.asarray(slab.get_positions())

    new_pos=old_pos-np.asarray([0,0,8.5])

    slab.set_positions(new_pos)
    he_com=slab.get_center_of_mass()

    add_adsorbate(slab, 'He', h, position=(he_com[0],he_com[1]))
    view(slab)
    write("final.xyz", slab)

if __name__ == '__main__':

    slab = io.read('last.xyz')
    grid = io.read('grid_he.xyz')
    old_pos = np.asarray(grid.get_positions())

    slab_ele=slab.get_chemical_symbols()
    stm_atom = ["He1"]
    all_atoms=slab_ele+stm_atom

    
    all_list=[]
    for idx, values in enumerate(old_pos):
        old_pos = slab.get_positions()
        all_list.append(np.append(old_pos, [values], axis=0))

   
    for i in range(len(all_list)):
        with open("He"+str(i)+".xyz", "w") as myfile:
          myfile.write('{}'.format(len(all_list[0])))
          myfile.write('\n')
          myfile.write('\n')
          for j in range (len(all_list[0])):
              myfile.write('{} {} {} {} \n'.format(all_atoms[j],all_list[i][j][0],all_list[i][j][1], all_list[i][j][2]))

        


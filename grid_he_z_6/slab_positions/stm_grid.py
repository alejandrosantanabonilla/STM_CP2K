import numpy as np

from ase import Atoms
from ase.io import read, write
from ase.visualize import view

import argparse


def create_grid(size, space, vac):
   """
   Function to create a grid of H atoms for 
   NEGF STM images.
   """
   grid_size=size
   spacing=space
   n_copies=grid_size**2

   elements=['He']*n_copies

   tip = np.array([[ 0,        0,       0      ]]) 

   # translating coordinates around a grid
   coordinates = []

   for i in range(n_copies):
      x = spacing * (i % grid_size)
      y = spacing * ((i // grid_size) % grid_size)
      xyz = np.array([x, y, 0])
      coordinates.extend(tip + xyz.T)

   chem_symb=''.join(elements)

   grid = Atoms(str(chem_symb),coordinates)
   grid.center(vacuum=float(vac))
   
   return grid
   

def com(atoms):
    """ Function to compute the center of mass (com)
        of an ASE object.
    """
    return atoms.get_center_of_mass()


def read_coord(mol, vac): #, heigth):
   """
   Function to read the system to be imaged using XYZ  

   """
   mol = read(str(mol))
   #values, direc = rot

   #mol.rotate(int(values),str(direc))
   mol.center(vacuum=vac)

   return mol
   
def tip_grid_sys(mol, grid, height, out_name="stm_total.xyz"):
    """ 
    Function
    """
    
    com_mol=mol.get_center_of_mass()
    com_grid=grid.get_center_of_mass()

    mol.translate(com_grid-com_mol)
    new_pos=mol.get_positions()+[0,0,-1.0*float(height)]
    mol.set_positions(new_pos)
    mol.extend(grid)

    return write(str(out_name), mol, format="xyz")
    
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("grid_size",
                        help="Define the size of a square grid of He atoms",
                        type=int)

    parser.add_argument("grid_space",
                         help="Define the spacing of the He atoms in the grid",
                        type=float)


    parser.add_argument("vacuum",
                        help="Define the vacuum for the create He grid.",
                        type=float)

    parser.add_argument("heigth",
                        help="Distance between the grid and the system.",
                        type=float)


    parser.add_argument("--output",
                        help="Output xyz file name.",
                        type=str)
    
    args = parser.parse_args()
    
    grid=create_grid(args.grid_size, args.grid_space, args.vacuum)
    mol=read_coord("mol.xyz",args.vacuum)
    tip_grid_sys(mol, grid, 3.0, args.output)
    


STM_CP2K
============

Repository for developing a NEGF-STM image code.

Content:
==========

In the folder **old_example_benzene** the following files can be found:

1. **BENZENE-UNPERTURBED-KS_MAT-1_0_28.Log** : Contains the informtion from a CP2K calculation to obtain a Kohn-Sham Hamiltonian.

2. **BENZENE-UNPERTURBED-RESTART.wfn** : Binary file printed by CP2K that contains information from the calculation like eigenvectors, eigenvalues, spin channels, number of molecular orbitals, among others.

3. **EIGEN.dat-1_0.MOLog** : Eigenvalues and Eigenvectors printed by CP2K. 

4. **eigen_vals_vecs.dat** : Refactored file which contains the eigenvalues and eignevectors in a new formated way, to be post-processed by a Fortran code.

5. **tot_ks.dat**: Refactored KS-Hamiltonian file, which prints the full KS-Hamiltonian in 4 column format.



In the folder **grid_z_height**, the results of "real" systems can be found. They are divided into He*index* where the *He_*index*_eigenval.dat* 
and *He_*index*_ks_tot.dat* store the eigenvalues, eigenvectors and KS-Hamiltoanian.



To do:
=========

The following are the tasks to be done to complete the tests:

1. Pack all the 3 codes in source to make them a python package that can be pip installable. 

2. **Test the code with a "real" system, namely, Gold surface plus a Helium atom. (DONE)**

3. Create an automatic CP2k template generator for performing calculations.

4. Generate test codes for this package.
                                         

STM_CP2K
============

Repository for developing a NEGF-STM image code.

Content:
==========

In this repository, we can find the following files:

1. **BENZENE-UNPERTURBED-KS_MAT-1_0_28.Log** : Contains the Informtion from a CP2K calculation to obtain a Kohn-Sham Hamiltonian.

2. **BENZENE-UNPERTURBED-RESTART.wfn** : Binary file printed by CP2K that contains information from the calculation like eigenvectors, eigenvalues, spin channels, number of molecular orbitals, among others.

3. **eigen_vals_vecs.dat ** : Refactored file which contains the eigenvalues and eignevectors in a new formated way, to be post-processed by a Fortran code.

4. **tot_ks.dat**: Refactored KS-Hamiltonian file, which prints the full KS-Hamiltonian in 4 column format.


All these results have been obtained using the **python** codes displayed in **source**.

To do:
=========

The following are the tasks to be done to complete the tests:

1. Pack all the 3 codes in source to make them a python package that can be pip installable. 

2. Test the code with a "real" system, namely, Gold surface plus a Helium atom.

3. Create an automatic CP2k template generator for performing calculations

4. Generate test codes for this package.
                                         

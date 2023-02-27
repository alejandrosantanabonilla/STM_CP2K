STM_CP2K
============

Repository for developing a NEGF-STM image code.

Content:
==========

In the folder **example** the following files can be found:

1. **wfn_gs.py, ks_ham_cp2k.py, *.wfn and .Log**: These files are needed to perform the analysis of the Hamiltonian, Eigenvalues and Eigenvectors.

2. **eigen_vals_vecs.dat** : Refactored file which contains the eigenvalues and eignevectors in a new formated way, to be post-processed by a Fortran 
code.

3. **tot_ks.dat**: Refactored KS-Hamiltonian file, which prints the full KS-Hamiltonian in 4 column format.

in the folder **scripts_young** is stored a workflow to be used when grid calculations are automated employing **array** jobs. Also, **scripts_python** 
stores a copy of the python files used for obtaining the eginevalues, eigenvectors and organised KS Hamiltonian.



To do:
=========

The following are the tasks to be done to complete the tests:

1. Pack all the 3 codes in source to make them a python package that can be pip installable. 

2. Create an automatic CP2k template generator for performing calculations.

3. Generate test codes for this package.
                                         

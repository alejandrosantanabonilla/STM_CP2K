Example
============

This repository contains an example of how to use the scripts:

1. **wfn_gs.py**: This progam process the file with extension *.wfn.
   It needs to be in the same folder as the script **wf_coeff_cp2k.py**

This script works in this way. Inside the file **wfn_gs.py** and after the
command **if __name__ == "__main__":**, one can use these 3 functions:

.. code-block:: python
   :caption: Usage of wfn_gs.py

   # Uploading the *.wfn result for analysis.
   total=read_wfn_gs_file("Gold-RESTART.wfn")

   # Printing both eigenvalues and eigenvectors into a .dat file
   # called eigen.
   gs_wfn().wfs_print(total, "eigenvalues_eignevectors")


   
.. code-block:: python
   :caption: This line provides the input for using **ks_ham_cp2k.py**.


    chunk_orbs=[len(values) for idx, values in enumerate(total.coeff)]
    print (chunk_orbs[0])


2. The next script is **ks_ham_cp2k.py**. This script requires a valid
   **.Log** file produced by **CP2K**.

   
.. code-block:: python
   :caption: Functions for using the script **ks_ham_cp2k.py**

    # SPINLESS Hamitonian
    c=ks_ham().ns_ks_ham("Gold-KS_MAT_last.Log")

    #WORKING HAMILTONIAN CHUNKING IN TERMS OF the number of maximum
    #shells +1 due to a blank space in the KS file

    ks_ham().block_ham(c, 452, "tot_ks.dat")

The number 452 is obtained from the number printed in **wfn_gs.py**
plus 1 (451+1).

If you type:

.. code-block:: python
   :caption: How to use **wfn_gs.py**
	     
   python wfn_gs.py

will produce **eigenvalues_eignevectors.dat**.

Typping:

.. code-block:: python
   :caption: How to use **ks_ham_cp2k.py**

   python ks_ham_cp2k.py

will produce the file tot_ks.dat.

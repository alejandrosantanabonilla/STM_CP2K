import itertools
import numpy as np
from wf_coeff_cp2k import *


class ks_ham(object):
    """
    A class for formating a KS Hamiltonian file
    obtained from a CP2K calculation. 

    Attributes:
    -----------
    ks_file     File printed by CP2K as part of 
                &PRINT &AO_MATRICES options.

    Note:
    -----
    This class relies on wfn_gs class for obtaining
    parameters of the wavefunction such as number of
    molecular orbitals, number of electrons, extension
    of basis set among others.    

    """    

    def chunks(self, lst, n, init_pos=0):
       """
       Function yielding successive 
       n-sized chunks from lst.

       Parameters:
       -----------
       lst :: list
            List to be split into n-chunks

       n :: int
            Size of the selected chunks

       init_pos :: int
            Index from which the chunking process
            starts.

       Return:
       --------

       None

       """
       for i in range(int(init_pos), len(lst), n):
           yield lst[i:i + n]

           
    def check_spin(self, ks_file):
       """ 
       Function to check the number of 
       spin channels for the calculation.

       ks_file :: str
             Name of the KS_HAM obtained 
             from a CP2K calculation.

       Return:
       ---------

       return :: list
           List with one string signalling spin-polarized or 
           not calculation.

       """
       n=0

       result=[]
      
       if 'KOHN-SHAM MATRIX FOR ALPHA SPIN' in open(ks_file).read():
          n=n+1

       if 'KOHN-SHAM MATRIX FOR BETA SPIN' in open(ks_file).read():
          n=n+1

       if n==2:
          result.append("spin_pol")

       elif n!=0:
          result.append('no_spin_pol')
       
       return result

    def ns_ks_ham(self, ks_file):
        """
        """
        with open(ks_file, "r") as fp: 
           result=list(itertools.dropwhile(lambda x:
                                        'KOHN-SHAM MATRIX'
                                        not in x, fp))

        ks=list(filter(str.strip,[element.strip('\n')
                                  for element in result]))[1:]

        return ks
       
    def spin_ks_ham(self, ks_file):
       """
       Function to separate the Hamiltonian based on 
       spin channels alpha and beta.
    
       Parameter:
       -----------
       ks_file :: str
            Name of the KS_HAM obtained from a 
            CP2K calculation.

       Returns:
       ---------
       result:: tuple
            tuple of lists with the Hamiltonians 
            split up in alpha and beta components.
    
       """
       with open(ks_file) as fp, open(ks_file) as fp_1:
           result_alpha=list(itertools.takewhile(lambda x:
                                                 'KOHN-SHAM MATRIX FOR BETA SPIN' not in x, 
             itertools.dropwhile(lambda x:
                                 'KOHN-SHAM MATRIX FOR ALPHA SPIN'
                                 not in x, fp)))

           result_beta=list(itertools.dropwhile(lambda x:
                                                'KOHN-SHAM MATRIX FOR BETA SPIN'
                                                not in x, fp_1))
        

       ks_spin_alpha=list(filter(str.strip,[element.strip('\n')
                                            for element in result_alpha]))[1:]

       ks_spin_beta=list(filter(str.strip,[element.strip('\n')
                                           for element in result_beta]))[1:]

       
       return ks_spin_alpha, ks_spin_beta

    def block_ham(self, spin_channel, num_orb, output_file):
        """ 
        Function for printing a CP2K Hamilatonin in a format based 
        on user-defined block size.
       
        Parameters:
        -----------

        spin_chanel :: list
              List containing raw values from a CP2K printed
              Hamiltonian. 
                     
        num_orb :: int 
               Number of orbitals used in the CP2K calculation. 
               This depends on the basis-set used in the calculation
               and automatically detected in class wfn_gs.

        output_file :: str
               Name of the output file where the block-printed 
               Hamiltonian is stored.

        block_size :: int
               Size of the block (number of columns) in which 
               the Hamiltonian can be printed.

        Return:
        --------
       
        None

        """
       
        ham=self.chunks(spin_channel,num_orb+1)

        # 4 slices from numerical values in the .log CP2K file.
        with open(str(output_file), "w") as out:
            for item in itertools.chain.from_iterable(list(ham)):
                print('  '.join(map(str,item.strip().split()[4:])),
                      file=out, flush=True)

                
    def print_ham(self, ks_file):
       """ no spin polarized calculation """
       ks_ham().check_spin("KS.dat-1_0_78.Log")
    
if __name__ == "__main__":
    # SPIN-POLARIZED Hamiltonian
    # spliting Hamiltonian into alpha and beta
    #a,b=ks_ham().spin_ks_ham("KS.dat-1_0_78.Log")
    
    # SPINLESS Hamitonian
    c=ks_ham().ns_ks_ham("Gold-KS_MAT_last.Log")

    #WORKING HAMILTONIAN CHUNKING IN TERMS OF the number of maximum
    #shells +1 due to a blank space in the KS file

    ks_ham().block_ham(c, 452, "tot_ks.dat")



    

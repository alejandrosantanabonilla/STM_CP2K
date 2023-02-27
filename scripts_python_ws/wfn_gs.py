from wf_coeff_cp2k import *

class gs_wfn(object):
    """
    Attributes:
    ------------

    """

    def print_wfs(self, wf_gs, output_name, counter):
       """ 
       Function to print the relevant information from 
       a wfs_gs object. It determines if non_spin, spin_up
       and spin_down are required.

       Parameters:
       -----------

       wf_gs :: wfs_gs object
          Object with the .wfn information

       output_name :: str
           Name provided to the output_file.
    
       counter :: int
           Number signalling the used channel 
           spin_alpha (up) and spin_beta (down). 

       Return
       -------
       None

       """
       with open(str(output_name), "w") as ofile:
          for i in range(counter):
             ofile.write(str(wf_gs.eigen[0][i])+"\n")
             ofile.write("\n")
             for idx, values in enumerate(wf_gs.coeff[0][i]):
                 ofile.write(str(values)+"\n")
             ofile.write("\n")
            
    def print_wfs_spin(self, wf_gs, output_name, counter, channel):
        """ Function to print the relevant information from 
            a wfs_gs object. It determines if non_spin, spin_up
            and spin_down are required.

        Parameters:
        -----------

        wf_gs :: wfs_gs object
             Object with the .wfn information

        output_name :: str
             Name provided to the output_file.
    
        counter :: int
             Number signalling the used channel 
             spin_alpha (up) and spin_beta (down). 

        channel :: int
             Number signalling the printed channel
             spin_alpha (0) and spin_beta (1).
  
        Return
        -------
        None
    
        """
        with open(str(output_name), "w") as ofile:
             for i in range(counter):
                 ofile.write(str(wf_gs.eigen[channel][i])+"\n")
                 ofile.write("\n")
                 for idx, values in enumerate(wf_gs.coeff[channel][i]):
                      ofile.write(str(values)+"\n")
                 ofile.write("\n")

    def wfs_print(self, wfn_gs, output_name):
        """ Function to print eigenvectors and eigenvalues 
            from a CP2K file with extension .wfn. This contains
            all the needed information for this aim.

            Parameters:
            ------------

            wf_gs: wfs_gs object
               Object with the .wfn information

            output_name :: str
               Name provided to the output_file.

            Return:
            --------
            None
        """
    
        if wfn_gs.nspin == 2:

           up, down=wfn_gs.nmo

           name_1 = str(output_name) + str("_up") + str(".dat")
           name_2 = str(output_name) + str("_down") + str(".dat")
       
           self.print_wfs_spin(wfn_gs, name_1, int(up), 0)   
           self.print_wfs_spin(wfn_gs, name_2, int(down), 1)

        else:

          mo_num, _= wfn_gs.nmo
          name_3 = str(output_name) + str(".dat")
          self.print_wfs(wfn_gs, name_3,mo_num)


if __name__ == "__main__":
    
    # Uploading the *.wfn result for analysis.
    total=read_wfn_gs_file("BENZENE-UNPERTURBED-RESTART.wfn")

    # Printing both eigenvalues and eigenvectors into a .dat file
    # called eigen.
    gs_wfn().wfs_print(total, "eigen")

    #Printing coefficients
    #print (len(total.coeff))

    #print (sum(total.coeff[0],[]))
    #for idx, values in enumerate(total.coeff):
    #    print (len(values))
    
    # Printing occupations
    #print (total.occup)

    # Number of eigenvalues
    #neigup=len(total.eigen[0])

    # Getting number of number of eigenvalues and eigenvectors solved
    #up, down=total.nmo

    #Printing the number fo eigenvalues and eigenvectors
    #print (up, down)
   
    #PRINTING MO coefficients for spin_up len = number_max_orb
    #for i in range(neigup):
    #    print(total.coeff[0][i])

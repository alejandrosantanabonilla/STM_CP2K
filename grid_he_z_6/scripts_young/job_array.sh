#!/bin/bash -l
# Batch script to run a serial array job under SGE.
#$ -l h_rt=6:00:00
#$ -l mem=4.5G
#$ -pe mpi 40
# Set up the job array. In this instance we have requested 10 tasks
#$ -t 1-25
# Set the name of the job.
#$ -N MyArrayJob
#$ -A KCL_Admin_rse
#$ -P Gold
#$ -cwd 

# Run the application.
module purge
module load gerun
module load gcc-libs
module load compilers/gnu/4.9.2
module load mpi/openmpi/3.1.4/gnu-4.9.2
module load openblas/0.3.7-openmp/gnu-4.9.2
module load cp2k/7.1/ompi/gnu-4.9.2

export OMP_NUM_THREADS=1

# Creating the list. Directories to be looped must be present in the same
# folders as this script is launched.
find . -type d | sort -V | tail -n +2 > list_folders.dat


# Proceeding with the calculations
INFILE=`sed -n "${SGE_TASK_ID}p" list_folders.dat`
cd $INFILE
gerun cp2k.popt -inp input.inp > output.out


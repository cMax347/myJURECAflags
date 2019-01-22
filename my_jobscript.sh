#!/bin/bash


#
#
##### JOB SETUP #################################
#SBATCH -J MEPinterp
#SBATCH -N 2
#SBATCH --ntasks=1368
#SBATCH --time=30
#SBATCH -o MEPinterp-%j.out
#SBATCH -e MEPinterp-%j.err
#SBATCH -p booster
#SBATCH --mail-user=m.merte@fz-juelich.de
#SBATCH --mail-type=ALL 
##################################################


#
#
# 
##### ENV SETUP #################################
source ~/mep_ld_lib_path.sh
#################################################



#
#
#
##### JOB EXECUTION ############################
srun -N1 --ntasks=68 mepInterp

# feel free to add additional jobs here
# 	eg:	srun -N2 --ntasks=136 -t 10 -p booster mepInterp

################################################





#
#
##### FORCE EXIT ################################
wait 
exit 0
################################################

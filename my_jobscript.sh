#!/bin/bash


#
#
##### JOB SETUP #################################
#SBATCH -J MEPinterp
#SBATCH -A jiff40
#SBATCH -N 1
#SBATCH --ntasks=68
#SBATCH --time=02:00:00
#SBATCH -o log/MEPinterp-%j.out
#SBATCH -e log/MEPinterp-%j.err
#SBATCH -p booster
#SBATCH --mail-user=m.merte@fz-juelich.de
#SBATCH --mail-type=ALL 
##################################################


#
#
##### make sure log dir exists ##################
$log=./log
if[ ! -d $log ]; then
	mkdir $log
fi
################################################ 



#
#
# 
##### ENV SETUP #################################
module load Architecture/KNL
module load Intel IntelMPI imkl 
################################################


#
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

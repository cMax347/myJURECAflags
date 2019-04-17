#!/bin/bash
#
#
#******** JOB ALLOCATION ************************
#SBATCH -J MEPinterp
#SBATCH -A jiff40
#SBATCH -N 1
#SBATCH --ntasks=272
#SBATCH --time=02:00:00
#SBATCH -o log/MEPinterp-%j.out
#SBATCH -e log/MEPinterp-%j.err
#SBATCH -p booster
#SBATCH --mail-user=m.merte@fz-juelich.de
#SBATCH --mail-type=END 
################################################## 
#
#
# 
#******** ENV SETUP *****************************8
#module use /usr/local/software/jurecabooster/OtherStages/
#module load Stages/2017a 
module load Architecture/KNL
module load Intel IntelMPI imkl 
################################################
#
#
#
#
#**** JOB EXECUTION ****************************
#
# MPI job
srun -N1 --ntasks=272 mepInterp
#
# HYBRID job
#export OMP_NUM_THREADS=4
#srun -N1 --ntaks=68 --cpus-per-task=4mepInterp

# feel free to add additional jobs here
# 	eg:	srun -N2 --ntasks=136 -t 10 -p booster mepInterp

################################################





#
#
##### FORCE EXIT ################################
wait 
exit 0
################################################

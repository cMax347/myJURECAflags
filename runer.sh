#!/bin/bash


source ~/mep_ld_lib_path.sh
#~
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#	run exe
#  ---------	
srun -N1 --ntasks-per-node=68 ./mepInterp
#-----------------------------------------------



#~
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#	kill env when finished
#  --------
wait 
exit 0  
#----------------------------------------------

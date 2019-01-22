#!/bin/sh

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
#	by Max Merte									|
#	load a suitable enviroment and builds cmake project in current directory	|
#											|
#	to compile:									|
#		->typ 									|
#			srun -N1 -A jiff40 -p booster -t 5 ./compile_MEP.sh		|
#		  		- from within build_dir to compile			|
#											|
#		-> use the script:							|
#			spawn_compile_mep.sh 						|
#											|
#~~~~~~~~~~~~~~~~~~~~~~~								|
#---------------------------------------------------------------------------------------|					



#
#
#
###### setup Arch & comp version ########
module purge 
wait
module load Architecture/KNL
wait

module use /usr/local/software/jurecabooster/OtherStages/
wait
module load Stages/2018a
#module load git (git seems to be available in Stages/2018a without further loading)
########################################


#
#
#
######## setup INTEL compiler env #####
module load Intel IntelMPI imkl
module load CMake
export FC=mpif90
export CC=mpicc
export CXX=mpicxx
#######################################





#
#
#
####### print ENV summary ###########
wait
echo "enviroment loaded, active modules:"
module list
####################################




#
#
#
####### PIT PULL   ####################
wait
echo ""
echo "try to run update git, current status:"
git status
echo ""
echo ""
echo "now stash any possible local changes and pull from upstream.."
git stash
wait
git pull
wait
echo ""
echo ".. finished git pull, now try to clean the build dir .."
echo ""
sh cleanUp.sh
#########################################



#
#
###### run CMake & make ############ 
echo ""
echo "cleaned the build dir, now start cmake.."
cmake ..
wait 
echo ""
echo "... finished cmake"
if [ -f ./Makefile ]; then
	echo "now try make ..."
	make -j 16
	echo ""
	wait
	echo "...make done!"
	#
	exe="bin/mepInterp"
	if [ -f $exe ]; then
		echo "SUCCESS wrote compiled exe to $exe"
	else
		echo "ERROR $exe was not found after make!"
		exit 1
	fi
else
	echo 'ERROR cmake failed. no Makefile was found'
	exit 1
fi
echo ""
########################################





#
#
##### SET  LD_LIBRARY_PATH  #####################
#
#  -> the file is then sourced by jobsripts ###
# ----------------
ld_file=~/mep_ld_lib_path.sh
rm -f $ld_file
#
header1="#wrote on "
DATE=`date "+%c"`
header="$header1 $DATE"
echo "$header"  >>      $ld_file
#
echo "wrote LD_LIBRARY_PATH to $ld_file"
echo ""
##################################################






#
#
##### FINALIZE ##################################
wait
if [ -f $ld_file ]; then
	echo "SUCCESS compile script finished without any issues"
	exit 0
else
	echo "WARNING an exe was compiled but the ld_library file $ld_file was not found"
	exit 1
fi
echo "ERROR - unknown error"
exit 1
#################################################

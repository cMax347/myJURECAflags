#!/bin/sh

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|
# by Max Merte													|
#~~~~~~														|
#	run from Jureca login node to spawn an interactive env that compiles the MEPinterp program for booster	|
#														|
#---------------------------------------------------------------------------------------------------------------|







#
#
###### prepare env ######################
source ~/.bashrc
wait
#
#
target=$myBIN/MEPinterp/build
compilerSH="compile_MEP.sh"
#
#
slurm_part="develbooster"
max_wall=3
########################################








#
#
#
#
##### update compile script #############
newF=$mySCRIPTS/$compilerSH	
oldF=$target/$compilerSH
#
if [ -f $newF ]; then
	rm $oldF  &> /dev/null
	cp $newF  $target
else
	echo "ERROR $newF does not exist! This is highly unexpected and should be fixed"
	exit 1
fi
#########################################










#
#
#
##### spawn interactive compilation ####
if [ -f $oldF ]; then
	cd $target
	echo "preperations successfull try to spawn a compilation now..."
	srun -N1 --ntasks-per-node=1 -A jiff40 -p $slurm_part -t $max_wall ./$compilerSH
	echo "... compilation done"
else
	echo "ERROR could not find $oldF - COMPILATION ABORTED !!!"
	exit 1
fi
#########################################









#
#
####### cleanUP #######################
wait
cd $HOME
exit 0
echo "all done by!"
#####################################

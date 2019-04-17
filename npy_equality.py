#!/usr/bin/env python3
import sys
import numpy as np


#	allclose evalautes
#	(1)		abs(a - b) <= (atol + rtol * abs(b))
#	elementwise for arrays a,b 
#	returns true if true for all elements
rtol	=	1e-05
atol	=	1e-08

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#		BODY
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def npy_compare(f1,f2):
	if(		f1.endswith('.npy')	
		and	f2.endswith('.npy')	
	):
		tens1	=	np.load(f1)
		tens2	=	np.load(f2)
		#
		print('[npy_compare]:	loaded data from file ',f1)
		print('[npy_compare]:	loaded data from file ',f2)		
		#
		are_same		=	np.allclose(	tens1,tens2,	rtol=rtol, atol=atol,		equal_nan=False)
		if not are_same:
			print('[npy_compare]: FAIL' )
			are_same	=	np.allclose(	tens1,tens2,	rtol=rtol, atol=atol,		equal_nan=True)
			if are_same:
				print('[npy_compare]: SUCCESS (rtol=',rtol,'; atol=',atol,')')
				print('[npy_compare]: WARNING found elements equal to NaN !')
			else:
				print('[npy_compare]: FAIL')
				print('[npy_compare]: WARNING at least one array contains NaN')
		else:
			print('[npy_compare]:	SUCCESS 	(rtol=',rtol,'; atol=',atol,')')


	else:
		print('[npy_compare]: provided files have to be .npy!')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def main():
	if len(sys.argv)<3:
		print('[npy_equality]:	please provide two .npy-files to compare')
		return 1
	else:
		compare(sys.argv[1],sys.argv[2])
	return 0
main()	





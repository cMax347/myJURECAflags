#!/usr/bin/env python3
import sys
import os
import time
import numpy as np

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#	numpy.allclose										|
#---------												| 
#	evalautes											|
#		(1)		abs(a - b) <= (atol + rtol * abs(b))	|
#	elementwise for arrays a,b 							|
#	returns true if true for all elements				|
#----													|
#	defaults											|	
#				rtol	=	1e-05						|
#				atol	=	1e-08						|
#-------------------------------------------------------|
rtol	=	0
atol	=	1e-08

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#		BODY
#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
def sys_input_valid():
	if len(sys.argv)<3:
		print('...\n[npy_equality]:	please provide two files')
	else:
		f1			=	sys.argv[1]
		f2			=	sys.argv[2]
		exist_f1	=	os.path.isfile(f1)
		exist_f2	=	os.path.isfile(f2)
		if exist_f1 and exist_f2:
			if f1==f2:
				print('...\n[npy_equality]: WARNING ',f1,' & ',f2,' are the same file...')
			else:
				return True
		else:
			if not exist_f1:
				print('...\n[npy_equality]: ERROR ',f1,' file does not exist')
			if not exist_f2:
				print('...\n[npy_equality]: ERROR ',f2,' file does not exist')
	return False


def npy_analyze(tens1,tens2):
	print('[npy_analyze]: ...') 
	if tens1.shape == tens2.shape:
		diff_tens	=	np.abs(		np.ndarray.flatten(tens1)	-	np.ndarray.flatten(tens2)		)
		#
		avg 	=	np.average(diff_tens)
		amax	=	np.amax(diff_tens)
		print('[npy_analyze]: AVG DIFF=' + ' {:e}'.format(	np.average(	diff_tens))	)
		print('[npy_analyze]: MAX DIFF=' + ' {:e}'.format(	np.amax(	diff_tens))	)
		#
	else:
		print('[npy_analyze]: WARNING detected different shapes	...')
		print('[npy_analyze]: #1: ',	tens1.shape)		
		print('[npy_analyze]: #2: ',	tens2.shape)
	print('[npy_analyze]: ...') 
#~~~~~




def npy_compare(f1,f2):
	if(		f1.endswith('.npy')	
		and	f2.endswith('.npy')	
	):
		tens1	=	np.load(f1)
		tens2	=	np.load(f2)
		#
		print('...\n[npy_compare]:	loaded data from file ',	f1		, ' ', 	tens1.shape	, '[absmin=	',np.amin(np.abs(tens1)),'; absmax=',np.amax(np.abs(tens1)),']'	)
		print('[npy_compare]:	loaded data from file ',	f2		, ' ', 	tens2.shape		, '[absmin=	',np.amin(np.abs(tens2)),'; absmax=',np.amax(np.abs(tens2)),']'		)		
		
		#
		passed	=	False
		atol	=	1e-10
		marker	=	'X'
		print('\n[npy_compare]: now compare tensors at different tolerances\n...')	
		while( 	not passed):
			start = time.time()
			atol = atol * 10
			if np.allclose(	tens1,tens2,	rtol=0, atol=atol,	equal_nan=False):
				passed=True
			elif np.allclose(tens1,tens2,		rtol=0, atol=atol,	equal_nan=True):
				print("[npy_compare]:	WARNING  tensors contain NaN element(s) ")
				passed=True
			if passed:
				marker	=	'✔'

			end = time.time()
			print('{:4.2e} '.format(atol)+marker+' (time spent: ','{:4e}'.format(end-start),'s)')

	
		print('...\n[npy_compare]: SUCCESS accepted tolerance=',atol)
		npy_analyze(tens1,tens2)
		#are_same		=	np.allclose(	tens1,tens2,	rtol=rtol, atol=atol,		equal_nan=False)
		#if not are_same:
		#	are_same	=	np.allclose(	tens1,tens2,	rtol=rtol, atol=atol,		equal_nan=True)
		#	if are_same:
		#		print('[npy_compare]: WARNING found elements equal to NaN !')
		#		print('[npy_compare]: SUCCESS (rtol=',rtol,'; atol=',atol,')')
		#	else:
		#		print('[npy_compare]: arrays appear to be not equal, start detailed analysis...')
		#		npy_analyze(tens1,tens2)
		#		print('[npy_compare]: FAIL - NOT EQUAL')		
		#else:
		#	print('[npy_compare]:	SUCCESS 	(rtol=',rtol,'; atol=',atol,')')
	else:
		print('[npy_compare]: ERROR provided files have to be .npy!')



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def main():
	print('^^^^^^^^^^^^^^^^^^^^ NPY EQUALITY ANALYZER ^^^^^^^^^^^^^^^')
	if sys_input_valid():
		npy_compare(sys.argv[1],sys.argv[2])
	return 0

main()	





#!/usr/bin/env python3
import sys
import os
import numpy as np
#
if len(sys.argv)>1:
    if sys.argv[1].endswith('.npy'):
        tens=None
        try:
            tens=np.load(sys.argv[1])
            print('SUCCESS read  ',os.path.abspath(sys.argv[1]))
        except FileNotFoundError:
            print('ERROR ',sys.argv[-1],' does not exist')
            sys.exit(1)
        #
        print("")
        print('detected  size:',    tens.size, ' (',tens.dtype,')')
        print('detected shape:',    tens.shape)
        print("")
        #
        flat_arr    =   np.ndarray.flatten(tens)
        abs_flat_arr=   np.abs(flat_arr)
        is_nan      =   np.isnan(flat_arr)
        #
        if True in is_nan:
            print('WARNING detected Nan elements')
            flat_arr_float = []
            for elem in abs_flat_arr:
                if not np.isnan(elem):
                    flat_arr_float.append(elem)
            print(">>>stripped NaN values from array<<<")
            print("")
        else:
            flat_arr_float = abs_flat_arr
        #
        print('*min* abs value (excluding nan): {:+12.6e}'.format(min(flat_arr_float)))
        print('*max* abs value (excluding nan): {:+12.6e}'.format(max(flat_arr_float)))
        sys.exit(0)
    else:
        print('pls provide a .npy file')
        sys.exit(1)
else:
    print('no input file given')
    sys.exit(1)

#!/usr/bin/env python3
import sys
import numpy as np
#
if len(sys.argv)>1:
    if sys.argv[1].endswith('.npy'):
        tens=np.load(sys.argv[1])
        print('found tens in ',sys.argv[1])
        print('raw tens:')
        print(tens)
        print('detected  size:',    tens.size)
        print('detected shape:',    tens.shape)
        #
        flat_arr    =   np.ndarray.flatten(tens)
        abs_flat_arr=   np.abs(flat_arr)
        is_nan      =   np.isnan(flat_arr)
        #
        if True in is_nan:
            print('WARNING detected Nan elements')
        #
        print('max abs value:', max(abs_flat_arr))
        print('min abs value:', min(abs_flat_arr))
        sys.exit(0)
    else:
        print('pls provide a .npy file')
        sys.exit(1)
else:
    print('no input file given')
    sys.exit(1)

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
        except FileNotFoundError:
            print('ERROR ',sys.argv[-1],' does not exist')
            sys.exit(1)
        #
        print("raw:",tens)
        print("~")
        print("sorted:",np.sort(tens))
        sys.exit(0)
    else:
        print('pls provide a .npy file')
        sys.exit(1)
else:
    print('no input file given')
    sys.exit(1)

# pool_ops.py
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#  Converts input shape and operation count of average pooling layer into output.
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  h_pool: average pooling kernel height count
#  w_pool: average pooling kernel width count
#  s: stride of average pooling kernel
#  p: amount of padding on each of the four input map sides
# Output:
#  Output shape and operation count of average pooling layer.
#
# Written by Matthew Moore
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
c_out = float('nan')
h_out = float('nan')
w_out = float('nan')
adds = 0.0
muls = 0.0
divs = 0.0

# parse script arguments
if len(sys.argv)==8:
    c_in = float(sys.argv[1])
    h_in = float(sys.argv[2])
    w_in = float(sys.argv[3])
    h_pool = float(sys.argv[4])
    w_pool = float(sys.argv[5])
    s = float(sys.argv[6])
    p = float(sys.argv[7])
else:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    exit()

# write script below this line
c_out = c_in
h_out = (h_in + 2 * p - h_pool) / s + 1
w_out = (w_in + 2 * p - w_pool) / s + 1
adds = c_in * h_out * w_out * (h_pool * w_pool - 1)
divs = c_in * h_out * w_out


# script output
print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))

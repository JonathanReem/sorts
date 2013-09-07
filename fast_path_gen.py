from __future__ import division
import numpy.random as nprnd
import time

def r_step_generator(lo, hi):
    num = lo
    while True:
        num += nprnd.randint(0, 10000)
        if num < hi:
            yield num
        else:
            raise StopIteration
        
N = 10 ** 7
t1 = time.clock()
 
u = range(0, (N // 10000) * 9999)
x = nprnd.randint(0, N, N // 1000).tolist()
 
for i_x, i_u in enumerate(r_step_generator(0, N)):
# Useful for timing, shows percent complete, time, and percent complete per second.
#    if i_x % 1000 == 0:
#    	print i_u / N * 100, time.clock() - t1, (i_u / N * 100) / (time.clock() - t1)
    u.insert(i_u, x[i_x - 1])
    
t2 = time.clock()
print t2 - t1
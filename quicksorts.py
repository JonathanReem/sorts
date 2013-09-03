import random
from itertools import chain
from compSortTest import compSortTest
import numpy as np

def triQuicksort(unsorted):
	unsorted_list = unsorted[:] #Make a copy so we leave the original list alone.
	if len(unsorted_list) < 6:
		return sorted(unsorted_list)
	
	pivot_indexes = np.random.choice(range(len(unsorted_list)), size=3)

	(unsorted_list[pivot_indexes[0]], unsorted_list[pivot_indexes[1]], unsorted_list[pivot_indexes[2]], 
	   unsorted_list[0], unsorted_list[1], unsorted_list[2]) = (unsorted_list[0], unsorted_list[1], unsorted_list[2],
	   unsorted_list[pivot_indexes[0]], unsorted_list[pivot_indexes[1]], unsorted_list[pivot_indexes[2]])
	
	pivots = triQuicksort(unsorted_list[:3])
	unsorted_list = unsorted_list[3:]
	
	lesser1  = triQuicksort(filter(lambda num: num > pivots[0], unsorted_list))
	lesser2  = triQuicksort(filter(lambda num: pivots[1] > num >= pivots[0], unsorted_list))
	greater1 = triQuicksort(filter(lambda num: pivots[2] > num >= pivots[1], unsorted_list))
	greater2 = triQuicksort(filter(lambda num: num >= pivots[2], unsorted_list))

	return list(chain(lesser1, [pivots[0]], lesser2, [pivots[1]], greater1, [pivots[2]], greater2))


def dualQuicksort(unsorted_list):
	u = unsorted_list[:]
	if len(u) < 6:
		return sorted(u)

def singleQuicksort(unsorted_list):
	u = unsorted_list[:]
	if len(u) < 6:
		return sorted(u)
	p_ind = np.random.choice(np.arange(len(unsorted_list)))
	u[0], u[p_ind] = u[p_ind], u[0]

	lesser = singleQuicksort(filter(lambda num: num <= u[0], u[1:]))
	greater = singleQuicksort(filter(lambda num: num > u[0], u[1:]))

	return list(chain(lesser, [u[0]], greater))

def main():
	compSortTest([singleQuicksort, triQuicksort])

if __name__ == '__main__':
	main()
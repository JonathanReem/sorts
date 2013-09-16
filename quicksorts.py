import random
from itertools import chain
from compSortTest import compSortTest
import numpy as np

def singleQuicksort(unsorted_list):
	def prepPivot(u):
		p_ind = np.random.choice(np.arange(len(unsorted_list)))
		u[0], u[p_ind] = u[p_ind], u[0]
		return u
	def partition(u):
		lesser = singleQuicksort(filter(lambda num: num <= u[0], u[1:]))
		greater = singleQuicksort(filter(lambda num: num > u[0], u[1:]))
		return lesser, greater

	u = unsorted_list[:]

	if len(u) < 6:
		return sorted(u)	

	u = prepPivot(u)
	lesser, greater = partition(u)
	
	return list(chain(lesser, [u[0]], greater))

def singlePureQuicksort(unsorted_list):
	def prepPivot(u):
		p_ind = random.randint(0, len(u) - 1)
		u[0], u[p_ind] = u[p_ind], u[0]
		return u

	def partition(u):
		lesser = []
		greater = []
		for num in u[1:]:
			if num < u[0]:
				lesser.append(num)
			else:
				greater.append(num)
		return lesser, greater

	u = unsorted_list[:]
	
	if len(u) < 2:
		return u

	u = prepPivot(u)
	lesser, greater = partition(u)
	
	return singlePureQuicksort(lesser) + [u[0]] + singlePureQuicksort(greater)

def main():
	compSortTest([singleQuicksort, singlePureQuicksort], max_size_order=5) # Sorts are too slow for higher orders with profiling.

if __name__ == '__main__':
	main()

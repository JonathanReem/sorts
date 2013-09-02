import time
import random
from collections import defaultdict
import numpy as np
from numpySorts import np_sort, simple_np_sort

from itertools import chain, repeat

def pure_countsort(unsorted_list):
    counts = defaultdict(int)
    for num in unsorted_list:
        counts[num] += 1

    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(min(counts), max(counts) + 1)))
    return sorted_list


def timed_countsort(unsorted_list):
	start_time = time.clock()
	counts = (np.bincount(np.array(unsorted_list))).tolist()

	end_time = time.clock()
	print "Making the count took:"
	print end_time - start_time
	
	start_time = time.clock()
	sorted_list = []
	for num in xrange(min(unsorted_list), max(unsorted_list) + 1):
		sorted_list += [num]*counts[num]	
	end_time = time.clock()
	print "Constructing the sorted list took:"
	print end_time - start_time
	
	print "Total time:"
	return sorted_list

def countsort(unsorted_list):
	"Sort a list of integers (ONLY INTEGERS) in linear time. 2-3x faster than sorted() for certain lists."
	counts = (np.bincount(np.array(unsorted_list))).tolist()
	sorted_list = []
	for num in xrange(min(unsorted_list), max(unsorted_list) + 1):
		sorted_list += [num]*counts[num]
	return sorted_list

from compSortTest import compSortTest

def main():
	compSortTest([countsort, timed_countsort, pure_countsort, sorted])

if __name__ == '__main__':
	main()

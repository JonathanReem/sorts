import time
import numpy as np

from collections import defaultdict
from itertools import chain, repeat

def pure_countsort(unsorted_list):
    """Pure-stdlib countsort, slower than numpy version."""
    counts = defaultdict(int)
    for num in unsorted_list:
        counts[num] += 1

    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(min(counts), max(counts) + 1)))
    return sorted_list


def timed_countsort(unsorted_list):
    """Countsort that prints useful benchmarking information."""
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

def test_countsort(unsorted_list):
    """Bleeding edge, not necessarily functional version."""
    start_time = time.clock()
    counts = (np.bincount(np.array(unsorted_list))).tolist()

    end_time = time.clock()
    print "Making the count took:"
    print end_time - start_time

    start_time = time.clock()
    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(len(counts))))
    end_time = time.clock()
    print "Constructing the sorted list took:"
    print end_time - start_time

    print "Total time:"
    return sorted_list

def countsort(unsorted_list):
    """Sort a list of integers (ONLY INTEGERS) in linear time.
    3-4x faster than sorted() for certain lists."""
    counts = (np.bincount(np.array(unsorted_list))).tolist()

    sorted_list = list(
        chain.from_iterable(
            repeat(num, counts[num])
            for num in xrange(len(counts))))

    return sorted_list

from compSortTest import compSortTest
import sys

def main():
    """Runs compSortTest on the sorts in this module."""
    try:
        size = int(sys.argv[1])
    except IndexError:
        size = 6
    compSortTest([countsort, pure_countsort, sorted], max_size_order=size)

if __name__ == '__main__':
    main()

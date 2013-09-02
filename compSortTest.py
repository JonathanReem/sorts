 #!/usr/bin/env python
"""
Author: Jonathan Reem
Author email: jonathan.reem@gmail.com
Date: September 2013
Implementation of a comprehensive speed test for sorting algorithms.
 Version 1.0
Current Features:
  Speed Testing with leaderboard generation over variable size lists
  Options for changing list sizes, number of lists, and others. See docstring of compSortTest for more info.
  Automatic error detection, and notification along with automatic debug list (10 item list) testing for easy debugging.
Future Features:
  Options for pathological data (sorted lists, almost sorted lists, lists with high repetition, near reversed lists, etc.)
  Better automatic debugging with pathological data options and more helpful errors.
    Where was the problem in the large list? Where they the same length? etc.
Current bugs:
  Bad sorts break the leaderboard by making consequent sorts not test for the list that the broken sort failed on.
    Branch: Issue-1
"""

import numpy.random as nprnd
import time
from random import randint

def compSortTest(sortList, max_size_order = 7, mult_list_size = True, 
				 check_sort = True, try_debug_list = True, verbose_timing = True):
	"""
	Takes as input a list of sorts and runs tests on them.
	Set max_size_order to the largest list size you want where the size is 10 ** max_size_order.
	Set mult_list_size to False to check on only one size of list. (10 million integers under 100 thousand)
	Set check_sort to False to not do assertions on the sorted lists.
	Set try_debug_list to False to not try the sort on a small list if it fails the assertion test.
	Set verbose_timing to False to only show leaderboards and assertion errors.
	"""

	unsorted_lists = []
	if mult_list_size:
		for i in range(2, max_size_order):
			size_random_sample = 10 ** i
			range_upper_limit = 10 ** randint(i-1, i)
			print "Generating %i random ints with max size %i..." % (size_random_sample, range_upper_limit)
			a = nprnd.randint(range_upper_limit, size=size_random_sample).tolist()
			unsorted_lists.append(a)
	else:
		size_random_sample = 10 ** max_size_order
		range_upper_limit = 10 ** (max_size_order - 2)
		print "Generating %i random ints with max size %i..." % (size_random_sample, range_upper_limit)
		a = nprnd.randint(range_upper_limit, size=size_random_sample).tolist()
		unsorted_lists.append(a)

	print ''

	if not verbose_timing:
		print "Timing sorts... \n"

	times = {}
	sorted_lists = {}
	sorts_to_test = sortList
	for index, unsorted in enumerate(unsorted_lists):
		sorted_list = sorted(unsorted)
		
		if not verbose_timing:
			print "Testing list %i..." % (index + 1)

		for sort in sorts_to_test:
			sort_name = sort.__name__
			if verbose_timing:
				print "For %i items, trying %s..." % (len(unsorted), sort.__name__)
			start_time, end_time = 0, 0
			try:
				start_time = time.clock()
				sorted_lists[sort_name].append(sort(unsorted))
				end_time = time.clock()
			except KeyError:
				start_time = time.clock()
				sorted_lists[sort_name] = list([sort(unsorted)])
				end_time = time.clock()
			
			try: 
				times[sort_name].append(end_time - start_time)
			except KeyError:
				times[sort_name] = list([end_time - start_time])
			if verbose_timing:
				print times[sort_name][-1]

			if check_sort:
				try:
					assert sorted_lists[sort_name][-1] == sorted_list
				except AssertionError:
					print ''
					print "%s did NOT work for the random list with %i integers." % (sort_name, len(unsorted))
					if try_debug_list:
						print "Generating and testing debug list:"
						debug_list = nprnd.randint(10, size = 10).tolist()
						print "Initial debug list: ", debug_list
						print "Sorted debug list: ", sorted(debug_list)
						print "Broken sort debug list: ", sort(debug_list)
					print sort, sort.__name__
					sorts_to_test.remove(sort)
					print "%s will not be tried again.\n" % (sort_name)

	working_sorts = sorts_to_test

	for index, unsorted in enumerate(unsorted_lists):
		leaderboard = [(times[sort.__name__][index], sort.__name__) for sort in working_sorts]
		leaderboard = sorted(leaderboard)
		
		print "For list %i, with length %i and range %i: " % (index + 1, len(unsorted), max(unsorted) - min(unsorted) + 1)
		for sort_time, sort_name in leaderboard:
			print sort_time, sort_name
		print ''

def main():
	def bad_sort(unsorted_list):
		return unsorted_list

	def good_sort(unsorted_list):
		return sorted(unsorted_list)

	def slow_sort(unsorted_list):
		# Slow operation:
		string_version = ''
		for num in range(1000):
			string_version += str(num)
		return sorted(unsorted_list)

	compSortTest([bad_sort, good_sort, slow_sort])

if __name__ == '__main__':
	main()

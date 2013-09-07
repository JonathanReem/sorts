 #!/usr/bin/env python
"""
Author: Jonathan Reem
Author email: jonathan.reem@gmail.com
Date: September 2013
Implementation of a comprehensive speed test for sorting algorithms.
 Version 1.0
Prerequisites:
  numpy 1.7.0 or later
    Replace lines 53 and 57 with random.randint calls instead of numpy.random.randint calls if you don't have it, know this is >FAR< slower.
Current Features:
  Speed Testing with leaderboard generation over variable size lists
  Options for changing list sizes, number of lists, and others. See docstring of compSortTest for more info.
  Automatic error detection, and notification along with automatic debug list (10 item list) testing for easy debugging.
Future Features:
  Options for pathological data (sorted lists, almost sorted lists, lists with high repetition, near reversed lists, etc.)
  Better automatic debugging with pathological data options and more helpful errors.
    Where was the problem in the large list? Where they the same length? etc.
"""

import numpy.random as nprnd
import time
import numpy as np
from itertools import chain

def compSortTest(sortList, max_size_order = 7, mult_list_size = True, 
				 check_sort = True, try_debug_list = True, verbose_timing = False,
				 pathological = False):
	"""
	Takes as input a list of sorts and runs tests on them.
	Set max_size_order to the largest list size you want where the size is 10 ** max_size_order. Lengths start at 10 ** 2,
	   so the default 7 generates 5 test lists.
	Set mult_list_size to False to check on only one size of list. (10 million integers under 100 thousand)
	Set check_sort to False to not do assertions on the sorted lists.
	Set try_debug_list to False to not try the sort on a small list if it fails the assertion test.
	Set verbose_timing to True to show timing data in real-time.
	Set pathological to True to do testing on pathological data sets.
	"""
	unsorted_lists = []
	if mult_list_size:
		for i in range(2, max_size_order):
			size_random_sample = 10 ** i
			range_upper_limit = 10 ** nprnd.randint(i-1, i)
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

	# Gives a notification of progress if verbose timing is turned off.
	if not verbose_timing:
		print "Timing sorts... \n"

	times = {} # Will eventually contain sort_name:list_of_times_in_order for lookup and use on the leaderboard.
	sorted_lists = {} # Will eventually contain sort_name:sorted_lists_in_order for lookup during sort checking.
	sorts_to_test = sortList # We want to keep the initial list but want to be able to remove bad sorts from the loop.
	for list_index, unsorted in enumerate(unsorted_lists):
		sorted_list = sorted(unsorted)
		
		# Again, progress indicator.
		if not verbose_timing:
			print "Testing list %i of random data..." % (list_index + 1)

		for sort_index, sort in enumerate(sorts_to_test[:]): # Copy made here to avoid a nasty bug where the for loop will 
															 # skip the sort immediately after a broken sort.
			sort_name = sort.__name__
			
			if verbose_timing:
				print "For %i items, trying %s..." % (len(unsorted), sort.__name__)
			
			start_time, end_time = 0, 0 #Timing is done inside the try/except blocks to avoid extra time from KeyErrors.
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
						print "Initial debug list:     ", debug_list
						print "Sorted debug list:      ", sorted(debug_list)
						print "Broken sort debug list: ", sort(debug_list)
					sorts_to_test.remove(sort)
					print "%s will not be tried again.\n" % (sort_name)

	working_sorts = sorts_to_test       # Bad sorts have been removed. Name change is for readability.
	print ''

	if pathological:
		print "Generating pathological lists..."
		print "WARNING: Pathological lists will only be generated and tested at the maximum size."
		pathological_lists = genPathologicalLists(max_size_order)



	for index, unsorted in enumerate(unsorted_lists):
		leaderboard = [(times[sort.__name__][index], sort.__name__) for sort in working_sorts]
		leaderboard = sorted(leaderboard)
		
		print "For list %i, with length %i and range %i: " % (index + 1, len(unsorted), max(unsorted) - min(unsorted) + 1)
		for sort_time, sort_name in leaderboard:
			print sort_time, sort_name
		print ''

def genPathologicalLists(max_size_order):
	#Only used here because this method is ugly if done inline.
	def genNearSorted(size_random_sample, range_upper_limit):
		u = np.arange(size_random_sample - (size_random_sample // 100)).tolist()
		for i in range(size_random_sample // 100):
			u.insert(np.random.randint(0, len(u)), np.random.randint(0, range_upper_limit))
		return u

	size_random_sample = 10 ** max_size_order
	range_upper_limit = 10 ** (max_size_order - 2)

	pathological_types = ["reversed", "sorted", "sorted_except_last"] #, "near_sorted", "near_reversed"] # Currently unimplemented.
	pathological_lists = []

	# Using a list of lists here instead of a keyed dictionary because the modularized timing mechanism will use a list of lists as an input.
	pathological_lists[0] = np.arange(size_random_sample).tolist()[::-1] #reversed
	pathological_lists[1] = np.arange(size_random_sample).tolist() #sorted
	pathological_lists[2] = chain(np.arange(size_random_sample - (size_random_sample // 100)).tolist(), 
													 np.random.randint(range_upper_limit, size=size_random_sample // 100).tolist()) #sorted_except_last
	pathological_lists["near_sorted"] = genNearSorted(size_random_sample, range_upper_limit)
	pathological_lists["near_reversed"] = genNearSorted(size_random_sample, range_upper_limit)[::-1]


def main():
	def bad_sort(unsorted_list):
		"Example of a broken sort"
		return unsorted_list

	def good_sort(unsorted_list):
		"Example of a good sort."
		return sorted(unsorted_list)

	def slow_sort(unsorted_list):
		"Example of a slow sort."
		string_version = ''
		for num in range(len(unsorted_list) // 10):
			string_version += str(num)    # Slow operation
		return sorted(unsorted_list)

	compSortTest([bad_sort, good_sort, slow_sort])

if __name__ == '__main__':
	main()
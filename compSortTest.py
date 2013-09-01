import numpy.random as nprnd
import time
from random import randint

def compSortTest(sortList, max_size_order = 7, mult_list_size = True, check_sort = True, try_debug_list = True):
	"""
	Takes as input a list of sorts and runs tests on them.
	Set max_size_order to the largest list size you want where the size is 10 ** max_size_order.
	Set mult_list_size to False to check on only one size of list. (10 million integers under 100 thousand)
	Set check_sort to False to not do assertions on the sorted lists.
	Set try_debug_list to False to not try the sort on a small list if it fails the assertion test.
	"""

	unsorted_lists = []
	if mult_list_size:
		for i in range(1, max_size_order):
			size_random_sample = 10 ** i
			range_upper_limit = 10 ** randint(i-1, i)
			print "Generating %i random ints with max size %i..." % (size_random_sample, range_upper_limit)
			a = nprnd.randint(range_upper_limit, size=size_random_sample).tolist()
			unsorted_lists.append(a)
	else:
		size_random_sample = 10 ** 7
		range_upper_limit = 10 ** 5
		print "Generating %i random ints with max size %i..." % (size_random_sample, range_upper_limit)
		a = nprnd.randint(range_upper_limit, size=size_random_sample).tolist()
		unsorted_lists.append(a)

	print ''

	times = {}
	sorted_lists = {}
	sorts_to_test = sortList
	for unsorted in unsorted_lists:
		sorted_list = sorted(unsorted)
		for sort in sorts_to_test:
			sort_name = sort.__name__
			print "For %i items, trying %s..." % (len(unsorted), sort.__name__)
			start_time = time.clock()
			try:
				sorted_lists[sort_name].append(sort(unsorted))
			except KeyError:
				sorted_lists[sort_name] = list([sort(unsorted)])
			end_time = time.clock()
			try: 
				times[sort_name].append(end_time - start_time)
			except KeyError:
				times[sort_name] = list([end_time - start_time])
			print times[sort_name][-1]

			if check_sort:
				try:
					assert sorted_lists[sort_name][-1] == sorted_list
				except AssertionError:
					print "%s did NOT work for the random list with %i integers." % (sort_name, len(unsorted))
					if try_debug_list:
						print "Generating and testing debug list:"
						debug_list = nprnd.randint(10, size = 10).tolist()
						print "Initial debug list: ", debug_list
						print "Sorted debug list: ", sorted(debug_list)
						print "Broken sort debug list: ", sort(debug_list)
					sorts_to_test.remove(sort)
					print "%s will not be tried again." % (sort_name)

	working_sorts = sorts_to_test

	for index, unsorted in enumerate(unsorted_lists):
		leaderboard = []
		for sort in working_sorts:
			sort_name = sort.__name__
			leaderboard.append((times[sort_name].pop(0), sort_name))
			print len(times[sort_name])
		leaderboard = sorted(leaderboard)
		
		print "For list number %i: " % (index)
		for sort_time, sort_name in leaderboard:
			print sort_time, sort_name
		print ''

def main():
	def bad_sort(unsorted_list):
		return unsorted_list

	def good_sort(unsorted_list):
		return sorted(unsorted_list)

	compSortTest([sorted, bad_sort, good_sort])

if __name__ == '__main__':
	main()

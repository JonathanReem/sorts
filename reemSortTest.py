from countsort import pure_countsort, timed_countsort, countsort
from smedSort import smedSort
from numpySorts import np_sort, simple_np_sort

from compSortTest import compSortTest

def main():
	compSortTest([pure_countsort, countsort, np_sort, sorted], verbose_timing = False)

if __name__ == '__main__':
	main()
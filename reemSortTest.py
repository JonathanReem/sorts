from countsort import pure_countsort, timed_countsort, countsort
from smedSort import smedSort
from numpySorts import np_sort, simple_np_sort
from quicksorts import singleQuicksort

from compSortTest import compSortTest

def main():
	compSortTest([countsort, np_sort, sorted, singleQuicksort])

if __name__ == '__main__':
	main()
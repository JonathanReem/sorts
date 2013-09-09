from countsort import pure_countsort, timed_countsort, countsort
from smedSort import smedSort
from numpySorts import np_sort, simple_np_sort
from triPivotQuicksort import triQuicksort

from compSortTest import compSortTest

def main():
	compSortTest([countsort, np_sort, sorted, triQuicksort], pathological=True)

if __name__ == '__main__':
	main()

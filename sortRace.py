import sys
import time
from countsort import countsort
from numpySorts import np_sort
import numpy.random as nprnd


def inf_generator(iteration=1):
    num = 0
    while True:
        num += iteration
        yield num

def race(sort):
    race_generator = inf_generator()
    for num in race_generator:
        u = []
        if num > 100:
            u = nprnd.randint(num, size=num / 100)
        else:
            u = nprnd.randint(num, size=num)
        start_time = time.clock()
        s = sort(u)
        end_time = time.clock()
        print num, end_time - start_time, sort.__name__

def main():
    sorts = [countsort, np_sort, sorted]
    sort = sorts[int(sys.argv[1].strip())]
    race(sort)

if __name__ == '__main__':
    main()

import numpy.random as nprnd
import heapq
import sys
import itertools

def rlist(size, limit_low, limit_high):
    return (nprnd.randint(limit_low, limit_high) for _ in xrange(size))
    
def iterator_mergesort(iterator, size):
    return heapq.merge(
             iterator_mergesort(
               (iterator.next() for _ in xrange(size/2)), size/2),
             iterator_mergesort(
                iterator, size - (size/2))
           ) if size >= 2 else iterator

def test():
    size = 10
    randomiterator, backup = itertools.tee(rlist(size, 0, size))
    sortediterator = iterator_mergesort(randomiterator, size)
    try:
        assert list(sortediterator) == sorted(backup)
    except AssertionError as e:
        print "Test failed."
        randomlist, randomlist1 = itertools.tee(rlist(10,0,10))
        print list(iterator_mergesort(randomlist, 10))
        print sorted(randomlist1)
        sys.exit(0)
    print "All tests pass."

def main():
    N = int(sys.argv[1])
    print "Generating generator..."
    testiterators = itertools.tee(rlist(N,0,N))
    print "Sorting..."
    sortediterators = iterator_mergesort(testiterators[0], N)

if __name__ == '__main__':
    #test()
    main()
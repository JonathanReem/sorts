Sorting Work
=====

This is a repository for my own work with sorting algorithms. I have written a very useful sort tester, please feel free to clone/fork your own version and use it in your projects and work.

countsort.py 
======

Contains a few fast implementations of countsort, countsort is the fastest and pure_countsort uses only stdlib functions. (countsort uses numpy for the bincount operation.)


numpySorts.py
======

Contains the default numpy sort as simple_np_sort and a blazingly quick numpy bucket sort as np_sort.

compSortTest.py
=====

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

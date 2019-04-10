                               __________

                                A2 TESTS
                               __________


Automated Testing Instructions
==============================

  Unzip `a2-tests.zip' to create the directory `a2-tests/'.  Copy all
  files in the `a2-tests' directory to the project directory
  `a2-code'. The following unix command should do this if `a2-tests' and
  a2-code are in the same directory.

  ,----
  | cp -r a2-tests/* a2-code/
  `----

  The Makefile provided is a copy of Makefile.withtests. The original
  version is called Makefile.notests.

  The new Makefile introduces the targets
  - `make test-p1' : test problem 1
  - `make test-p2' : test problem 2
  - `make test-p3' : test problem 3
  - `make test-p4' : test problem 4
  - `make test' : test all problems

  Test programs `test_sortedlist1', `test_sortedlist2', and
  `test_undolist' associated with problems 1-3 can run individual tests
  by passing a test number as a command line argument as in

  ,----
  | ./test_sortedlist2 3    # run the 3rd tests only
  `----

  Test program test_listmanager.sh associated with problem 4 also has
  this feature

  ,----
  | ./test_listmanager.sh 10  # run only the 10th test
  `----

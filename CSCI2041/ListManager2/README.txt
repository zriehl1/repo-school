                               __________

                                A3 TESTS
                               __________


Automated Testing Instructions
==============================

  Unzip `a3-tests.zip' to create the directory `a3-tests/'.  Copy all
  files in the `a3-tests' directory to the project directory
  `a3-code'. The following unix command should do this if `a3-tests' and
  a3-code are in the same directory.

  ,----
  | cp -r a3-tests/* a3-code/
  `----

  The Makefile provided is a copy of Makefile.withtests. The original
  version is called Makefile.notests.

  The new Makefile introduces the targets
  - `make test-p1' : test problem 1
  - `make test-p2' : test problem 2
  - `make test-p3' : test problem 3
  - `make test-p4' : test problem 4
  - `make test' : test all problems

  Test programs `test_document', `test_doccol', and `test_bulkops'
  associated with problems 1-3 can run individual tests by passing a
  test number as a command line argument as in

  ,----
  | ./test_doccol 3    # run the 3rd test only
  `----

  Test program `test_multimanager.sh' associated with problem 4 also has
  this feature

  ,----
  | ./test_multimanager.sh 10  # run only the 10th test
  `----

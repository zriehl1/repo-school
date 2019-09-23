from search import *

def p1():
    breadth_first_tree_search(EightPuzzle((6,2,3,1,5,4,0,7,8)))
    while True:
        None

def p2():
    depth_limited_search(EightPuzzle((6,2,3,1,5,4,0,7,8)))
    while True:
        None

def p3():
    depth_first_tree_search(EightPuzzle((6,2,3,1,5,4,0,7,8)))

p3()

def p4():
    depth_first_tree_search(NQueensProblem(8))

def p5():
    print("BFS Tree")
    breadth_first_tree_search(NQueensProblem(8))

p5()

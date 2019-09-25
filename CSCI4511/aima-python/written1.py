from search import *
SIZE = 8
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
    
def p4():
    print("DFS Tree " + str(SIZE))
    depth_first_tree_search(NQueensProblem(SIZE))
    while True:
        None

def p5():
    print("BFS Tree " + str(SIZE))
    breadth_first_tree_search(NQueensProblem(SIZE))
    while True:
        None

p4()

import turtle
import random
import time

### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING
### PLEASE FULLSCREEN THE PROGRAM WHILE IT IS DRAWING

'''
I apologise for the sloppy game functions.
In order to get the game rules you have to fullsize the screen,
unfortunately I don't know how to have python maximize the window automatically.
'''
board = turtle.Turtle()
numbers = turtle.Turtle()
t00 = turtle.Turtle()
t01 = turtle.Turtle()
t02 = turtle.Turtle()
t03 = turtle.Turtle()
t10 = turtle.Turtle()
t11 = turtle.Turtle()
t12 = turtle.Turtle()
t13 = turtle.Turtle()
t20 = turtle.Turtle()
t21 = turtle.Turtle()
t22 = turtle.Turtle()
t23 = turtle.Turtle()
t30 = turtle.Turtle()
t31 = turtle.Turtle()
t32 = turtle.Turtle()
t33 = turtle.Turtle()
rules1 = turtle.Turtle()
rules2 = turtle.Turtle()
def Sudoku():
    drawgrid()
    PUZZ_VAR = random.randint(1,5)
    fillknown(PUZZ_VAR)
    RULES()
    WHICHVERSION = turtle.textinput('Sudoku','Auto-check? Y/N')
    if WHICHVERSION == 'Y' or 'y':
        if PUZZ_VAR == 1:
            CHECKER(puzzle1)
        if PUZZ_VAR  == 2:
            CHECKER(puzzle2)
        if PUZZ_VAR == 3:
            CHECKER(puzzle3)
        if PUZZ_VAR == 4:
            CHECKER(puzzle4)
        if PUZZ_VAR == 5:
            CHECKER(puzzle5)

    else:
        if PUZZ_VAR == 1:
            PLAYGAME(puzzle1)
        if PUZZ_VAR  == 2:
            PLAYGAME(puzzle2)
        if PUZZ_VAR == 3:
            PLAYGAME(puzzle3)
        if PUZZ_VAR == 4:
            PLAYGAME(puzzle4)
        if PUZZ_VAR == 5:
            PLAYGAME(puzzle5)
    
class puzzle:
    def __init__(self,row4,row3,row2,row1, PUZZLE_NUMBER):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.pnum = PUZZLE_NUMBER

puzzle1 = puzzle([1,'','',4],['',3,'',1],[2,'',1,3],[3,'',4,2],1)
puzzle2 = puzzle([3,4,1,2],['','','',''],['','','',''],[4,3,2,1],2)
puzzle3 = puzzle([4,'','',1],['',1,3,''],['',4,1,''],[1,'','',3],3)
puzzle4 = puzzle(['','','',''],[2,3,4,1],[3,4,1,2],['','','',''],4)
puzzle5 = puzzle(['',2,4,''],[1,'','',3],[4,'','',2],['',1,3,''],5)

def PUZZLE_SET(PUZ_NUM):
    board.penup()
    board.goto(-250 + 500/8, -250 + 500/12)
    Var = 0
    UPVar = (500/4)
    UPCon =  -250 + 500/12
    SIDCon = -250 + 500/8
    while Var < 4:
        board.write(PUZ_NUM.row1[Var], move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        Var += 1
    board.goto(SIDCon,UPVar + UPCon)
    Var = 0
    while Var < 4:
        board.write(PUZ_NUM.row2[Var], move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        Var += 1
    board.goto(SIDCon, 2*UPVar + UPCon)
    Var = 0
    while Var < 4:
        board.write(PUZ_NUM.row3[Var], move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        Var += 1
    board.goto(SIDCon, 3*UPVar + UPCon)
    Var = 0
    while Var < 4:
        board.write(PUZ_NUM.row4[Var], move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        Var += 1

def fillknown(PUZZ_VAR): #Fills the grid with the starting values
    if PUZZ_VAR == 1:
        PUZZLE_SET(puzzle1)
    if PUZZ_VAR == 2:
        PUZZLE_SET(puzzle2)
    if PUZZ_VAR == 3:
        PUZZLE_SET(puzzle3)
    if PUZZ_VAR == 4:
        PUZZLE_SET(puzzle4)
    if PUZZ_VAR == 5:
        PUZZLE_SET(puzzle5)

def CHECKER(GAME_NUM):
    R1 = [ el for el in GAME_NUM.row1]
    R2 = [ el for el in GAME_NUM.row2]
    R3 = [ el for el in GAME_NUM.row3]
    R4 = [ el for el in GAME_NUM.row4]
    GAME_DONE = False
    while GAME_DONE == False:
        if GAME_NUM.pnum == 1:
            XVAL = int(turtle.numinput('Sudoku','X Value'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 0 or YVAL == 1 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                t20.clear()
                                INCHECK = False
                                R3[0] = None
                            else:
                                R3[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2: 
                                                                                t20.clear()
                                                                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[0] = None
                                                            
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                                R1[1] = None
                            else:
                                R1[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t01.clear()
                                                                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[1] = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                                R2[1] = None
                            else:
                                R2[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t11.clear()
                                                                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                R2[1] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                                R4[1] = None
                            else:
                                R4[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t31.clear()
                                                                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[1] = None
                                    
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 0 or YVAL == 1:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                                R3[2] = None
                            else:
                                R3[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t22.clear()
                                                                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[2] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                                R4[2] = None
                            else:
                                R4[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t32.clear()
                                                                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[2] = None
            if XVAL == 3:
                None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True                                                       
                        

            
                

            
        if GAME_NUM.pnum == 2:
            XVAL = int(turtle.numinput('Sudoku', ' X VALUE'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t10.clear()
                                R2[0] = None
                            else:
                                R2[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t10.clear()
                                                                                t10.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[0] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t20.clear()
                                R3[0] = None
                            else:
                                R3[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t20.clear()
                                                                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[0] = None
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                                R2[1] = None
                            else:
                                R2[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t11.clear()
                                                                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[1] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t21.clear()
                                R3[1] = None
                            else:
                                R3[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t21.clear()
                                                                                t21.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[1] = None
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t12.clear()
                                R2[2] = None
                            else:
                                R2[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t12.clear()
                                                                                t12.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[2] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                                R3[2] = None
                            else:
                                R3[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t22.clear()
                                                                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[2] = None
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t13.clear()
                                R2[3] = None
                            else:
                                R2[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t13.clear()
                                                                                t13.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[3] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECL = False
                                t23.clear()
                                R3[3] = None
                            else:
                                R3[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t23.clear()
                                                                                t23.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[3] = None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
        
                        
                    
                        
            
        if GAME_NUM.pnum == 3:
            XVAL = int(turtle.numinput('Sudoku','X Value'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t10.clear()
                                R2[0] = None
                            else:
                                R2[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t10.clear()
                                                                                t10.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[0] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t20.clear()
                                R3[0] = None
                            else:
                                R3[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t20.clear()
                                                                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[0] = None
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t13.clear()
                                R2[3] = None
                            else:
                                R2[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t13.clear()
                                                                                t13.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[3] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t23.clear()
                                R3[3] = None
                            else:
                                R3[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t23.clear()
                                                                                t23.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[3] = None
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t02.clear()
                                R1[2] = None
                            else:
                                R1[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t02.clear()
                                                                                t02.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[2] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                                R4[2] = None
                            else:
                                R4[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t32.clear()
                                                                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[2] = None

            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                                R1[1] = None
                            else:
                                R1[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t01.clear()
                                                                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[1] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                                R4[1] = None
                            else:
                                R4[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t31.clear()
                                                                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[1] = None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
        if GAME_NUM.pnum == 4:
            XVAL = int(turtle.numinput('Sudoku', 'X Input'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t00.clear()
                                R1[0] = None
                            else:
                                R1[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t00.clear()
                                                                                t00.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[0] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t30.clear()
                                R4[0] = None
                            else:
                                R4[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t30.clear()
                                                                                t30.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[0] = None
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                                R1[1] = None
                            else:
                                R1[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t01.clear()
                                                                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[1] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                                R4[1] = None
                            else:
                                R4[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t31.clear()
                                                                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[1] = None

            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t02.clear()
                                R1[2] = None
                            else:
                                R1[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t02.clear()
                                                                                t02.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[2] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                                R4[2] = None
                            else:
                                R4[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t32.clear()
                                                                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[2] = None

            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t03.clear()
                                R1[3] = None
                            else:
                                R1[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t03.clear()
                                                                                t03.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[3] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t33.clear()
                                R4[3] = None
                            else:
                                R4[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t33.clear()
                                                                                t33.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[3] = None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
                                
        if GAME_NUM.pnum == 5:
            XVAL = int(turtle.numinput('Sudoku','X Input'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t00.clear()
                                R1[0] = None
                            else:
                                R1[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t00.clear()
                                                                                t00.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[0] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t30.clear()
                                R4[0] = None
                            else:
                                R4[0] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t30.clear()
                                                                                t30.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[0] = None
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t03.clear()
                                R1[3] = None
                            else:
                                R1[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t03.clear()
                                                                                t03.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R1[3] = None
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t33.clear()
                                R4[3] = None
                            else:
                                R4[3] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t33.clear()
                                                                                t33.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R4[3] = None
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                                R2[1] = None
                            else:
                                R2[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t11.clear()
                                                                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[1] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t21.clear()
                                R3[1] = None
                            else:
                                R3[1] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t21.clear()
                                                                                t21.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[1] = None
                                
                        

            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t12.clear()
                                R2[2] = None
                            else:
                                R2[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t12.clear()
                                                                                t12.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R2[2] = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                                R3[2] = None
                            else:
                                R3[2] = INVAL
                                TL = [R4[0],R4[1],R3[0],R3[1]] 
                                TR = [R4[2],R4[3],R3[2],R3[3]]
                                BL = [R2[0],R2[1],R1[0],R1[1]]
                                BR = [R2[2],R2[3],R1[2],R1[3]]
                                C1 = [R4[0],R3[0],R2[0],R1[0]]
                                C2 = [R4[1],R3[1],R2[1],R1[1]]
                                C3 = [R4[2],R3[2],R2[2],R1[2]]
                                C4 = [R4[3],R3[3],R2[3],R1[3]]
                                if R1.count(1) < 2 and R1.count(2) < 2 and R1.count(3) < 2 and R1.count(4) < 2:
                                    if R2.count(1) < 2 and R2.count(2) < 2 and R2.count(3) < 2 and R2.count(4) < 2:
                                        if R3.count(1) < 2 and R3.count(2) < 2 and R3.count(3) < 2 and R3.count(4) < 2:
                                            if R4.count(1) < 2 and R4.count(2) < 2 and R4.count(3) < 2 and R4.count(4) < 2:
                                                if C1.count(1) < 2 and C1.count(2) < 2 and C1.count(3) < 2 and C1.count(4) < 2:
                                                    if C2.count(1) < 2 and C2.count(2) < 2 and C2.count(3) < 2 and C2.count(4) < 2:
                                                        if C3.count(1) < 2 and C3.count(2) < 2 and C3.count(3) < 2 and C3.count(4) < 2:
                                                            if C4.count(1) < 2 and C4.count(2) < 2 and C4.count(3) < 2 and C4.count(4) < 2:
                                                                if TL.count(1) < 2 and TL.count(2) < 2 and TL.count(3) < 2 and TL.count(4) < 2:
                                                                    if TR.count(1) < 2 and TR.count(2) < 2 and TR.count(3) < 2 and TR.count(4) < 2:
                                                                        if BL.count(1) < 2 and BL.count(2) < 2 and BL.count(3) < 2 and BL.count(4) < 2:
                                                                            if BR.count(1) < 2 and BR.count(2) < 2 and BR.count(3) < 2 and BR.count(4) < 2:
                                                                                t22.clear()
                                                                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                                                                INCHECK = False
                                else:
                                    R3[2] = None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':            
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
                
                        




def PLAYGAME(GAME_NUM): #Doesn't autocheck
    R1 = [ el for el in GAME_NUM.row1]
    R2 = [ el for el in GAME_NUM.row2]
    R3 = [ el for el in GAME_NUM.row3]
    R4 = [ el for el in GAME_NUM.row4]
    GAME_DONE = False
    while GAME_DONE == False:
        if GAME_NUM.pnum == 1:
            XVAL = int(turtle.numinput('Sudoku','X Value'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 0 or YVAL == 1 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                t20.clear()
                                INCHECK = False
                            else:
                                t20.clear()
                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[0] = INVAL
                                INCHECK = False
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                            else:
                                t01.clear()
                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[1] = INVAL
                                INCHECK = False
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                            else:
                                t11.clear()
                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[1] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                            else:
                                t31.clear()
                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[1] = INVAL
                                INCHECK = False    
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 0 or YVAL == 1:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                            else:
                                t22.clear()
                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[2] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                            else:
                                t32.clear()
                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[2] = INVAL
                                INCHECK = False
            if XVAL == 3:
                None
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True                                                       
                        

            
                
    
            
        if GAME_NUM.pnum == 2:
            XVAL = int(turtle.numinput('Sudoku', ' X VALUE'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t10.clear()
                            else:
                                t10.clear()
                                t10.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[0] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t20.clear()
                            else:
                                t20.clear()
                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[0] = INVAL
                                INCHECK = False
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                            else:
                                t11.clear()
                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[1] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t21.clear()
                            else:
                                t21.clear()
                                t21.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[1] = INVAL
                                INCHECK = False
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t12.clear()
                            else:
                                t12.clear()
                                t12.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[2] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                            else:
                                t22.clear()
                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[2] = INVAL
                                INCHECK = False
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku', 'Y INPUT'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t13.clear()
                            else:
                                t13.clear()
                                t13.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[3] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku', 'Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECL = False
                                t23.clear()
                            else:
                                t23.clear()
                                t23.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[3] = INVAL
                                INCHECK = False
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
              
                    
                        
            
        if GAME_NUM.pnum == 3:
            XVAL = int(turtle.numinput('Sudoku','X Value'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t10.clear()
                            else:
                                t10.clear()
                                t10.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[0] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t20.clear()
                            else:
                                t20.clear()
                                t20.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[0] = INVAL
                                INCHECK = False
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t13.clear()
                            else:
                                t13.clear()
                                t13.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[3] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t23.clear()
                            else:
                                t23.clear()
                                t23.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[3] = INVAL
                                INCHECK = False
            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t02.clear()
                            else:
                                t02.clear()
                                t02.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[2] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                            else:
                                t32.clear()
                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[2] = INVAL
                                INCHECK = False

            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                            else:
                                t01.clear()
                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[1] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                            else:
                                t31.clear()
                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[1] = INVAL
                                INCHECK = False
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
        if GAME_NUM.pnum == 4:
            XVAL = int(turtle.numinput('Sudoku', 'X Input'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t00.clear()
                            else:
                                t00.clear()
                                t00.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[0] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t30.clear()
                            else:
                                t30.clear()
                                t30.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[0] = INVAL
                                INCHECK = False
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t01.clear()
                            else:
                                t01.clear()
                                t01.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[1] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t31.clear()
                            else:
                                t31.clear()
                                t31.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[1] = INVAL
                                INCHECK = False

            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t02.clear()
                            else:
                                t02.clear()
                                t02.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[2] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t32.clear()
                            else:
                                t32.clear()
                                t32.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[2] = INVAL
                                INCHECK = False

            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t03.clear()
                            else:
                                t03.clear()
                                t03.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[3] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t33.clear()
                            else:
                                t33.clear()
                                t33.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[3] = INVAL
                                INCHECK = False
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True
                                
        if GAME_NUM.pnum == 5:
            XVAL = int(turtle.numinput('Sudoku','X Input'))
            if XVAL > 3 or XVAL < 0:
                XVAL = None
            if XVAL == 0:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t00.clear()
                            else:
                                t00.clear()
                                t00.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[0] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t30.clear()
                            else:
                                t30.clear()
                                t30.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[0] = INVAL
                                INCHECK = False
            if XVAL == 3:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Value'))
                    if YVAL == 1 or YVAL == 2:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 0:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t03.clear()
                            else:
                                t03.clear()
                                t03.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R1[3] = INVAL
                                INCHECK = False
                    if YVAL == 3:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INVAL = None
                                INCHECK = True
                            if INVAL == 0:
                                INCHECK = False
                                t33.clear()
                            else:
                                t33.clear()
                                t33.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R4[3] = INVAL
                                INCHECK = False
            if XVAL == 1:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t11.clear()
                            else:
                                t11.clear()
                                t11.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[1] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t21.clear()
                            else:
                                t21.clear()
                                t21.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[1] = INVAL
                                INCHECK = False
                                
                        

            if XVAL == 2:
                YCHECK = True
                while YCHECK == True:
                    YVAL = int(turtle.numinput('Sudoku','Y Input'))
                    if YVAL == 0 or YVAL == 3:
                        YCHECK = True
                        YVAL = None
                    if YVAL == 1:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t12.clear()
                            else:
                                t12.clear()
                                t12.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R2[2] = INVAL
                                INCHECK = False
                    if YVAL == 2:
                        YCHECK = False
                        INCHECK = True
                        while INCHECK == True:
                            INVAL = int(turtle.numinput('Sudoku','Input Value'))
                            if INVAL > 4 or INVAL < 0:
                                INCHECK = True
                                INVAL = None
                            if INVAL == 0:
                                INCHECK = False
                                t22.clear()
                            else:
                                t22.clear()
                                t22.write(INVAL, move=False, align='center', font=('Arial', 16, 'normal'))
                                R3[2] = INVAL
                                INCHECK = False
            SUBMIT = str(turtle.textinput('Sudoku','Submit? Y/N'))
            if SUBMIT == 'Y' or SUBMIT == 'y':            
                TL = [R4[0],R4[1],R3[0],R3[1]] 
                TR = [R4[2],R4[3],R3[2],R3[3]]
                BL = [R2[0],R2[1],R1[0],R1[1]]
                BR = [R2[2],R2[3],R1[2],R1[3]]
                C1 = [R4[0],R3[0],R2[0],R1[0]]
                C2 = [R4[1],R3[1],R2[1],R1[1]]
                C3 = [R4[2],R3[2],R2[2],R1[2]]
                C4 = [R4[3],R3[3],R2[3],R1[3]]
                if R1.count(1) == 1 and R1.count(2) == 1 and R1.count(3) == 1 and R1.count(4) == 1:
                    if R2.count(1) == 1 and R2.count(2) == 1 and R2.count(3) == 1 and R2.count(4) == 1:
                        if R3.count(1) == 1 and R3.count(2) == 1 and R3.count(3) == 1 and R3.count(4) == 1:
                            if R4.count(1) == 1 and R4.count(2) == 1 and R4.count(3) == 1 and R4.count(4) == 1:
                                if C1.count(1) ==1 and C1.count(2) == 1 and C1.count(3) == 1 and C1.count(4) == 1:
                                    if C2.count(1) ==1 and C2.count(2) == 1 and C2.count(3) == 1 and C2.count(4) == 1:
                                        if C3.count(1) ==1 and C3.count(2) == 1 and C3.count(3) == 1 and C3.count(4) == 1:
                                            if C4.count(1) ==1 and C4.count(2) == 1 and C4.count(3) == 1 and C4.count(4) == 1:
                                                if TL.count(1) ==1 and TL.count(2) == 1 and TL.count(3) == 1 and TL.count(4) == 1:
                                                    if TR.count(1) ==1 and TR.count(2) == 1 and TR.count(3) == 1 and TR.count(4) == 1:
                                                        if BL.count(1) ==1 and BL.count(2) == 1 and BL.count(3) == 1 and BL.count(4) == 1:
                                                            if BR.count(1) ==1 and BR.count(2) == 1 and BR.count(3) == 1 and BR.count(4) == 1:
                                                                GAME_DONE = True                                                       
                        

                
            
    

def drawgrid():###########------------- Setup Function ---------------##################
    turtle.speed(5)
    turtle.delay(2)
    HIDETURTLES()
    drawsquare()
    boldhoriz()
    drawhoriz()
    boldvert()
    drawvert()
    numbot()
    numside()
    TURTLEBOX()

def drawsquare(): #500x500 square with center at 0,0
    board.penup()
    board.pensize(4)
    board.goto(-250,-250)
    board.pendown()
    board.forward(500)
    board.left(90)
    board.forward(500)
    board.left(90)
    board.forward(500)
    board.left(90)
    board.forward(500)
    board.left(90)


def drawhoriz():
    board.pensize(1)
    board.penup()
    board.goto(-250, -250/2)
    board.pendown()
    board.forward(500)
    board.penup()
    board.goto(-250,250/2)
    board.pendown()
    board.forward(500)

def boldhoriz():
    board.penup()
    board.goto(-250,0)
    board.pendown()
    board.forward(500)

def drawvert():
    board.pensize(1)
    board.penup()
    board.goto(-250/2,250)
    board.pendown()
    board.forward(500)
    board.penup()
    board.goto(250/2,250)
    board.pendown()
    board.forward(500)
    

def boldvert():
    board.right(90)
    board.penup()
    board.pensize(4)
    board.goto(0,250)
    board.pendown()
    board.forward(500)
    board.penup()

def numbot():
    board.penup()
    v = -250 + (500/8)
    b = 0
    board.left(90)
    board.goto(v, -250 - (500/16))
    while b < 4:
        board.write(b, move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        b = b + 1

def numside():
    board.left(90)
    v = -250 + (500/12)
    b = 0
    board.penup()
    board.goto(-250 - (500/16),v)
    while b < 4:
        board.write(b, move=False, align='center', font=('Arial', 16, 'normal'))
        board.forward(500/4)
        b = b + 1
    board.right(90)

def HIDETURTLES():
    board.ht()
    turtle.ht()
    numbers.ht()
    t00.ht()
    t00.penup()
    t01.ht()
    t01.penup()
    t02.ht()
    t02.penup()
    t03.ht()
    t03.penup()
    t10.ht()
    t10.penup()
    t11.ht()
    t11.penup()
    t12.ht()
    t12.penup()
    t13.ht()
    t13.penup()
    t20.ht()
    t20.penup()
    t21.ht()
    t21.penup()
    t22.ht()
    t22.penup()
    t23.ht()
    t23.penup()
    t30.ht()
    t30.penup()
    t31.ht()
    t31.penup()
    t32.ht()
    t32.penup()
    t33.ht()
    t33.penup()
    rules1.ht()
    rules1.penup()
    rules2.ht()
    rules2.penup()

def TURTLEBOX():
    x = -250 + 500/8
    y = -250 + 500/12
    dx = 500/4
    dy = 500/4
    t00.goto(x,y)
    t01.goto(x + dx, y)
    t02.goto(x + 2*dx, y)
    t03.goto(x + 3*dx, y)
    t10.goto(x, y + dy)
    t11.goto(x + dx, y + dy)
    t12.goto(x + 2*dx, y + dy)
    t13.goto(x + 3*dx, y + dy)
    t20.goto(x, y + 2*dy)
    t21.goto(x + dx, y + 2*dy)
    t22.goto(x + 2*dx, y + 2*dy)
    t23.goto(x + 3*dx, y + 2*dy)
    t30.goto(x, y + 3*dy)
    t31.goto(x + dx, y + 3*dy)
    t32.goto(x + 2*dx, y + 3*dy)
    t33.goto(x + 3*dx, y + 3*dy)

def RULES():
    rules1.goto(0,250 + 500/6)
    rules1.write('To input numbers, put in the X value, the Y value, and the value you would like to enter. If the value you enter is invalid, the game will prompt you for another value.', move=False, align='center', font=('Arial', 16, 'normal'))
    




Sudoku()
    

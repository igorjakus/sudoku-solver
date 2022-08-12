import numpy as np


def sudoku(puzzle):
    # repeat until solved
    while 0 in puzzle:
        solve(puzzle)
    return puzzle

def solve(puzzle):
    for y in range(9):
        for x in range(9):
            # if unsolved square
            if puzzle[y][x] == 0:
                # if there's one possible number
                nums = possibilities(puzzle, x, y)
                if len(nums) == 1:
                    # put that number
                    puzzle[y][x] = nums.pop()

def possibilities(puzzle, x , y):
    # EXCLUDE NUMBERS THAT ARE NOT POSSIBLE
    possible_numbers = {1, 2, 3, 4, 5, 6, 7, 8 , 9}

    # 1. elimination of rows and columns
    for i in range(9):
        possible_numbers.discard(puzzle[i][x]) # rows
        possible_numbers.discard(puzzle[y][i]) # columns
    
    # 2. elimination of 3x3 square
    x0 = (x // 3) * 3 # x position of first square in our 3x3 square
    y0 = (y // 3) * 3 # y position of first square in our 3x3 square
    # look through that 3x3 square
    for i in range(x0, x0+3):
        for j in range(y0, y0+3):
             possible_numbers.discard(puzzle[j][i])

    return possible_numbers


if __name__ == '__main__':    
    arr = np.array([[5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]])
            
    solved = sudoku(arr)
    print(solved)

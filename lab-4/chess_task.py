board = [0] * 8  # creating board
import time


def test(queen, col):
    for i in range(1, queen):
        if (board[queen - i - 1] == col): return 0  # Test vertical
        if (board[queen - i - 1] == col - i): return 0  # Test diagonal 1 (\)
        if (board[queen - i - 1] == col + i): return 0  # Test diagonal 2 (/)
    return 1


def play(queen):
    for col in range(1, len(board) + 1):
        if (test(queen, col)):  # If I can play the queen...
            board[queen - 1] = col  # Add queen to the solution Array
            if (queen == len(board) and board
            == [4, 2, 5, 8, 6, 1, 3, 7]):  # If the last queen was played, this is a solution
                for i in range(len(board)):
                    for j in range(board[i] - 1):
                        print(". ", end='')
                    print(board[i], end='')
                    count = 0
                    while count != len(board) - board[i]:
                        print(" .", end='')
                        count += 1
                    print()
                print("---------------------------")
            else:
                play(queen + 1)  # If not last queen, play the next one
            board[queen - 1] = 0  # Clean the solution Array


play(1)  # Start putting first queen

import functions

board = functions.Sudoku("puzzle.txt")
board.print_table()
board.find_empty()
board.solver()
print()
print()
print()
board.print_table()
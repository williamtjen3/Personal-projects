class Sudoku:

    def __init__(self, filename):
        file = open(filename)
        self.board = []
        for line in file:
            line = line.strip("\n").strip(",").split(",")
            line = [int(el) for el in line]
            self.board.append(line)
        
        self.iterations = 0
    
    def print_table(self):

        for i,line in enumerate(self.board):
            if i % 3 == 0:
                print(''.join(["-"]*(len(line)*3)))

            for i2, el in enumerate(line):
                if i2 % 3 == 0:
                    print("|",end=" ")
                print(el, end=" ")
            print()
            
    def find_empty(self):
        for r, row in enumerate(self.board):
            for c, col in enumerate(row):
                if self.board[r][c] == 0:
                    return (r,c)
        
        return None

    def valid(self, val, row, column):
        col_val = [r[column] for r in self.board]
        if val == 0:
            return False

        #check row
        if val in self.board[row]:
            return False
        
        #check column
        if val in col_val:
            return False
        
        #check 3x3 square
        box_row = row // 3
        box_col = column // 3
        for r in range(box_row*3,box_row*3+3):
            for c in range(box_col*3,box_col*3+3):
                if val == self.board[r][c]:
                    return False
        
        return True

    def solver(self):
        empty = self.find_empty()
        if not empty:
            return True

        if empty != None:
            for val in range(1,10):
                valid_bool = self.valid(val,empty[0],empty[1])
                if valid_bool == True:
                    self.board[empty[0]][empty[1]] = val
                    if self.solver():
                        return True
                    
                    self.board[empty[0]][empty[1]] = 0
        
        return False
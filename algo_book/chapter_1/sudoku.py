# Implementing a sudoku solver

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self._check_valid()
        self._check_solved()

    def solve(self):
        while not self._check_solved():
            for i in range(self.size):
                for j in range(self.size):
                    num = self._get_number(i, j)
                    if not num:
                        continue
                    else:
                        self.sudoku[i][j] = num 
        print(self.sudoku)
                    
                    
    def _get_number(self, i, j):
        for num in range(1,10):
            if not self._check_number(num, i, j):
                continue
            else:
                return num
        return False
            
    def _check_number(self,num, i, j):
        return (self._check_row( num, i) and
                self._check_col(num, j) and
                self._check_block(num, i, j))

    def _check_row(self, num, i):
        if num not in self.sudoku[i]:
            return True
        else:
            return False

    def _check_col(self, num, j):
        for row in self.sudoku:
            if num != row[j]:
                continue
            else:
                return False
        return True

    def _check_block(self,num, i, j):
        return True

    def _check_valid(self):
        if self._check_size():
            return self._check_type()
        raise RuntimeError('Error : Invalid Sudoku Puzzle')
            
    
    def _check_type(self):
        for row in self.sudoku:
            for num in row:
                if isinstance(num ,int):
                    continue
                else:
                    raise ValueError(f'Error : Element {num} in {row} is not integer')
        return True

    def _check_size(self):
        col = len(self.sudoku)
        for row in self.sudoku:
            if len(row) == col:
                continue
            else:
                raise ValueError('Error : Incorrect Sudoku Dimension')
        self.size= col
        return True


    

    def _check_solved(self):
        for row in self.sudoku:
            if 0 in row:
                return False
            else:
                continue
        return True

    def _get_element(self):
        pass


puzzle = [
  [6, 8, 0, 0, 4, 7, 0, 0, 0],
  [7, 3, 4, 0, 6, 2, 5, 0, 0],
  [2, 0, 0, 5, 0, 0, 8, 7, 4],
  [0, 0, 0, 2, 5, 0, 0, 1, 0],
  [0, 0, 0, 0, 8, 0, 0, 0, 0],
  [5, 6, 0, 9, 1, 3, 0, 0, 7],
  [0, 0, 1, 7, 2, 0, 3, 0, 0],
  [9, 2, 0, 0, 4, 0, 8, 0, 1],
  [0, 7, 0, 0, 0, 1, 0, 5, 6]
] 

sp = Sudoku(puzzle)
print(sp.solve())

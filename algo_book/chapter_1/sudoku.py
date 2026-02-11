# Implementing a sudoku solver

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self._check_valid()
        self._find_empty()

    def solve(self):
        index = 0
        while index < len(self.empty):
            i, j = self.empty[index]
            num = self.sudoku[i][j]+1
            val=self._check_digit(i,j,num)
            if val!=None:
                self.sudoku[i][j] = val
                index +=1
            else:
                self.sudoku[i][j] = 0
                index -= 1

            if index < 0:
                raise RuntimeError('Unsolvable Sudoku')


    def _check_digit(self,i, j, start_num):

        row_start = i//3 * 3
        col_start = j//3 *3
        row_lst =  self.sudoku[i]
        col_lst = [row[j] for row in self.sudoku]
        block_lst = [col for row in self.sudoku[row_start : row_start + 3] for col in row[col_start:col_start + 3] ]
        for num in range(start_num, 10):
            row_check = num not in row_lst
            col_check = num not in col_lst
            block_check = num not in block_lst
            if (row_check and col_check and block_check):
                return num
        return None

    def _find_empty(self):
        self.empty = []
        for i in range(self.size):
            for j in range(self.size):
                if self.sudoku[i][j] == 0:
                    self.empty.append((i,j))


    def _check_valid(self):
        if self._check_size():
            return self._check_type()
        raise RuntimeError('Error : Invalid Sudoku Puzzle')
            
    
    def _check_type(self):
        for row in self.sudoku:
            for num in row:
                if not isinstance(num ,int):
                    raise ValueError(f'Error : Element {num} in {row} is acceptable')
                if num > 9 or num < 0:
                    raise ValueError(f'Error : Element {num} in {row} is acceptable')
        return True

    def _check_size(self):
        for row in self.sudoku:
            if len(row) != len(self.sudoku):
                raise ValueError('Error : Incorrect Sudoku Dimension')
        self.size= len(self.sudoku)
        return True

puzzle =[
  [0, 0, 0, 9, 0, 5, 0, 4, 0],
  [0, 9, 1, 8, 0, 0, 0, 0, 2],
  [3, 0, 0, 0, 0, 0, 0, 0, 0],
  [2, 0, 0, 3, 0, 0, 0, 0, 0],
  [6, 0, 0, 0, 0, 0, 0, 0, 7],
  [0, 7, 3, 0, 0, 8, 5, 0, 0],
  [0, 6, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 9, 0, 2, 0, 0],
  [0, 8, 7, 1, 0, 0, 0, 0, 9]
]


sp = Sudoku(puzzle)
sp.solve()
print(sp.sudoku)

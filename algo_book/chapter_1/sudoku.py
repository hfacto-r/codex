# Implementing a sudoku solver

class Sudoku:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.cols = self.rows = self.check_valid()

    def check_valid(self):
        pass
        
    def _check_size(self):
        col = len(self.sudoku)
        for row in self.sudoku:
            if len(row) == col:
                continue
            else:
                raise RuntimeError
        return col

    def solver(self):
        pass


    def _check_solved(self):
        for row in self.sudoku:
            if 0 in row:
                return False
            else:
                continue
        return True

puzzle = [
    [6, 8, 7, 3, 0, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 5],
    [6, 8, 7, 3, 5, 8, 1, 9, 3],
]

sp = Sudoku(puzzle)
sp.solver()

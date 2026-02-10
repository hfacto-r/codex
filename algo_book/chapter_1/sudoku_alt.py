#Sudoku solver

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


def solve(puzzle):
    size = 9
    block_sets = [ set() for _ in range(size)]
    row_sets = [ set() for _ in range(size)]
    col_sets = [ set() for _ in range(size)]
    empty_cells = []


    def prelim_run(puzzle, size):
        for row in range(size):
            for col in range(size):
                cell = puzzle[row][col]
                if cell == 0:
                    empty_cells.append((row,col))
                else:
                    blk_id = ((row//3) * 3) + col//3
                    block_sets[blk_id].add(cell)
                    row_sets[row].add(cell)
                    col_sets[col].add(cell)

    def check_value(val, row, col):
        blk_id = ((row//3) * 3) + col//3
        return (val not in row_sets[row] and val not in col_sets[col] and val not in block_sets[blk_id])




solve(puzzle)

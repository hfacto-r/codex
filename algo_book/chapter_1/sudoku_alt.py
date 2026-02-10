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
    digit_sets = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    block_sets = [ set() for _ in range(size)]
    row_sets = [ set() for _ in range(size)]
    col_sets = [ set() for _ in range(size)]
    possible_values = []
    empty_cells = []

    def get_blkid(row, col):
        return ((row//3) * 3) + col//3

    def prelim_run(puzzle, size):
        for row in range(size):
            for col in range(size):
                cell = puzzle[row][col]
                if cell == 0:
                    empty_cells.append((row,col))
                else:
                    block_sets[get_blkid(row,col)].add(cell)
                    row_sets[row].add(cell)
                    col_sets[col].add(cell)
        
        for row in range(size):
            for col in range(size):
                vals = list(digit_sets - (row_sets[row] | col_sets[col] | block_sets[get_blkid(row,col)]))
                possible_values.append(vals)


    def check_value(val, row, col):
        blk_id = ((row//3) * 3) + col//3
        return (val not in row_sets[row] and val not in col_sets[col] and val not in block_sets[blk_id])

    def get_value(val, row, col):
        pos = (row * size) + col
        value_list = sorted(possible_values[pos])
        for value in value_list:
            if value > cell and check_value(cell, row, col):
                return value

    prelim_run(puzzle, size)
    print(possible_values[0],block_sets[0] | row_sets[0] | col_sets[0] )
solve(puzzle)









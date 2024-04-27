import tkinter as tk

def is_valid(board, row, col, num):
    # Check if num is already used in current row
    if num in board[row]:
        return False
    
    # Check if num is already used in current column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if num is already used in current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Undo the current cell if no solution found
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def solve_puzzle():
    # Convert input values to integers
    puzzle = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entry_widgets[i][j].get()
            if entry:
                row.append(int(entry))
            else:
                row.append(0)
        puzzle.append(row)

    if solve_sudoku(puzzle):
        for i in range(9):
            for j in range(9):
                entry_widgets[i][j].delete(0, tk.END)
                entry_widgets[i][j].insert(0, puzzle[i][j])
    else:
        print("No solution exists for the given Sudoku puzzle.")

root = tk.Tk()
root.title("Sudoku Solver")

entry_widgets = []
for i in range(9):
    row_widgets = []
    for j in range(9):
        entry = tk.Entry(root, width=3)
        entry.grid(row=i, column=j)
        row_widgets.append(entry)
    entry_widgets.append(row_widgets)

solve_button = tk.Button(root, text="Solve", command=solve_puzzle)
solve_button.grid(row=9, columnspan=9)

root.mainloop()

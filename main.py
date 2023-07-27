import tkinter as tk
from tkinter import messagebox

# Global variables
N = 9  # Size of the Sudoku grid
grid = [[0 for _ in range(N)] for _ in range(N)]

def is_valid_move(row, col, num):
    # Check if placing 'num' in (row, col) is valid
    # (No duplicate numbers in row, column, or 3x3 subgrid)
    for i in range(N):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell():
    # Find the next empty cell in the grid
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku():
    row, col = find_empty_cell()
    if row is None or col is None:
        return True

    for num in range(1, 10):
        if is_valid_move(row, col, num):
            grid[row][col] = num

            if solve_sudoku():
                return True

            grid[row][col] = 0

    return False

def print_grid():
    # Function to print the Sudoku grid
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()

def on_solve():
    solve_sudoku()
    update_grid()

def on_reset():
    global grid
    grid = [[0 for _ in range(N)] for _ in range(N)]
    update_grid()

def update_grid():
    for i in range(N):
        for j in range(N):
            cell_value = grid[i][j]
            if cell_value != 0:
                cells[i][j].delete(0, tk.END)
                cells[i][j].insert(0, str(cell_value))
            else:
                cells[i][j].delete(0, tk.END)

def on_cell_edit(row, col, event):
    try:
        value = int(event.widget.get())
        if 1 <= value <= 9:
            grid[row][col] = value
        else:
            event.widget.delete(0, tk.END)
            event.widget.insert(0, str(grid[row][col]))
    except ValueError:
        event.widget.delete(0, tk.END)
        event.widget.insert(0, str(grid[row][col]))

def create_board(root):
    global cells
    cells = [[None for _ in range(N)] for _ in range(N)]

    sudoku_frame = tk.Frame(root, bg="#EFEFEF")  # Add background color to the Sudoku grid
    sudoku_frame.pack(pady=10)

    for i in range(N):
        for j in range(N):
            # Determine the 3x3 subgrid indices
            subgrid_row, subgrid_col = i // 3, j // 3
            bg_color = "#FFFFFF" if (subgrid_row + subgrid_col) % 2 == 0 else "#ECECEC"
            
            cell_frame = tk.Frame(sudoku_frame, width=40, height=40, bg=bg_color, borderwidth=1, relief="solid")  # Add background and border to cells
            cell_frame.grid(row=i, column=j)
            cell_value = grid[i][j]
            cell_entry = tk.Entry(cell_frame, font=("Arial", 20), width=2, justify="center")
            cell_entry.insert(0, str(cell_value))
            cell_entry.bind("<FocusOut>", lambda e, row=i, col=j: on_cell_edit(row, col, e))
            cell_entry.pack(fill="both", expand=True)
            cells[i][j] = cell_entry

    button_frame = tk.Frame(root, bg="#EFEFEF")  # Add background color to the button frame
    button_frame.pack(pady=10)

    solve_button = tk.Button(button_frame, text="Solve", command=on_solve, font=("Arial", 14), bg="#4CAF50", fg="white")  # Customize the Solve button
    solve_button.pack(side=tk.LEFT, padx=10)

    reset_button = tk.Button(button_frame, text="Reset", command=on_reset, font=("Arial", 14), bg="#f44336", fg="white")  # Customize the Reset button
    reset_button.pack(side=tk.RIGHT, padx=10)

def main():
    root = tk.Tk()
    root.title("Sudoku Solver")

    # Use a custom font for the entire GUI
    root.option_add("*Font", ("Helvetica", 12))

    create_board(root)

    root.mainloop()

if __name__ == "__main__":
    main()

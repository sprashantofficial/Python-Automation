import tkinter as tk
from tkinter import messagebox

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")

        self.entries = [[None for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                entry = tk.Entry(master, width=2, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=1, pady=1)
                self.entries[i][j] = entry

        solve_button = tk.Button(master, text='Solve', command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    def get_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                if val == '':
                    row.append(0)
                elif val.isdigit() and 1 <= int(val) <= 9:
                    row.append(int(val))
                else:
                    messagebox.showerror("Invalid input", "Please enter digits 1-9 only.")
                    return None
            board.append(row)

        return board

    def fill_board(self, board):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if board[i][j] != 0:
                    self.entries[i][j].insert(0, str(board[i][j]))

    def solve_sudoku(self):
        board = self.get_board()
        if board and self.solve(board):
            self.fill_board(board)
        else:
            messagebox.showerror("Error", "No solution exist!")

    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        row, col = find

        for i in range(1, 10):
            if self.is_valid(board, i, (row, col)):
                board[row][col] = i
                if self.solve(board):
                    return True
                board[row][col] = 0

        return False

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)

        return None

    def is_valid(self, board, num, pos):
        row, col = pos

        for i in range(9):
            if board[row][i] == num and col != i:
                return False
            if board[i][col] == num and row != i:
                return False

        box_x = col // 3
        box_y = row // 3

        # row=5, col=7
        # box_y= 5//3 = 1 box_x = 7 // 3 = 2
        # (3, 6)
        # (6, 9)

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num:
                    return False

        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()









import chess
import chess.svg
import chess.pgn
import tkinter as tk
from tkinter import messagebox, simpledialog

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ajedrez")
        self.board = chess.Board()
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.player_turn = chess.WHITE
        self.update_status()

    def draw_board(self):
        self.canvas.delete("all")
        board_svg = chess.svg.board(board=self.board)
        self.board_image = tk.PhotoImage(data=board_svg)
        self.canvas.create_image(0, 0, anchor="nw", image=self.board_image)

    def handle_click(self, event):
        col = event.x // 50
        row = event.y // 50
        square = chess.square(col, 7 - row)

        if self.board.turn == self.player_turn:
            move_str = simpledialog.askstring("Mueve una pieza", "Ingresa tu movimiento (por ejemplo, 'e2 e4'):")
            try:
                move = chess.Move.from_uci(move_str)
                if move in self.board.legal_moves:
                    self.board.push(move)
                    self.draw_board()
                    self.switch_player()
                    self.update_status()
                    self.check_game_over()
                else:
                    messagebox.showerror("Movimiento inválido", "Movimiento no válido. Inténtalo de nuevo.")
            except ValueError:
                messagebox.showerror("Movimiento inválido", "Movimiento no válido. Inténtalo de nuevo.")

    def switch_player(self):
        self.player_turn = not self.player_turn

    def update_status(self):
        if self.player_turn == chess.WHITE:
            self.root.title("Ajedrez - Turno de las Blancas")
        else:
            self.root.title("Ajedrez - Turno de las Negras")

    def check_game_over(self):
        if self.board.is_game_over():
            result = self.board.result()
            messagebox.showinfo("Fin del juego", f"Resultado: {result}")
            self.root.quit()

def main():
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()



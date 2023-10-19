import chess
import chess.svg
import chess.pgn
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import io

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
        self.board_image = self.svg_to_image(board_svg)
        self.canvas.create_image(0, 0, anchor="nw", image=self.board_image)

    def svg_to_image(self, svg_data):
        svg_data_bytes = svg_data.encode("utf-8")
        svg_data_stream = io.BytesIO(svg_data_bytes)
        svg_data_image = Image.open(svg_data_stream)
        return ImageTk.PhotoImage(svg_data_image)

    # Resto del código...

if __name__ == "__main__":
    main()



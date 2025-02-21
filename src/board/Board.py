from ..system.Packages import Packages as pkg
from .BoardRenderer import BoardRenderer
from ..game.pieces.Piece import Piece
from .Cell import Cell

class Board:
    def __init__(self):
        # _Init_
        self.table = self._initialize_board()
        
    def _initialize_board(self) -> list[list[Cell]]:
        """Cria o tabuleiro inicial com as células vazias."""
        
        white_cell = "whte_cell"
        black_cell = "dark_cell"
        
        # Define the table with white and black cells
        return [
            [(Cell(black_cell) if (nx + ny) % 2 == 0 else Cell(white_cell)) for nx in range(8)]
            for ny in range(8)
        ]
        
    def insert_in_table(self, cell_obj: Piece) -> None:
        x, y = cell_obj.get_coords()
        self.table[y][x].set_piece(cell_obj)

    def get_cell(self, coords: tuple[int, int]) -> Cell:
        x, y = coords
        return self.table[y][x]

    def get_piece(self, coords: tuple[int, int]) -> Piece:
        return self.get_cell(coords).get_piece()
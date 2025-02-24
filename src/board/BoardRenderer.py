from .Cell import Cell
from ..system._methods import clear_screen
from ..system.Packages import Packages as pkg
from ..game.pieces.Piece import Piece

class BoardRenderer:
    brd_skins = pkg.BOARD_SKINS
    letters = pkg.LETTERS_DICT
        
    def print_formatted_table(self, table: list[list[Cell]], team_turn: str) -> None:
        """Print the board on console."""

        clear_screen()
        for ny in range(7, -1, -1):
            # Print the numbers
            print(f"{ny+1} ", end="")
            
            # Print the objects
            for nx in range(8):
                cell = table[ny][nx]
                print(self.print_cell(cell, team_turn), end="")
            print()

        # Print the letters
        print("   ", end="")
        for letter in self.letters.keys():
            print(letter, end="  ")
        print("\n")
        
    def print_cell(self, cell : Cell, team_turn: str) -> str:
            pre_fmt, pos_fmt = "\033[1m", "\033[0;0m"
            wall = self.brd_skins["wall"]
            piece = cell.get_piece()
            
            # Set skin face
            obj = cell.get_face()
            
            pre_fmt = self.get_piece_color(piece, team_turn)

            pre_fmt += self.get_cell_color(cell, team_turn)
                
            return pre_fmt + wall + obj + wall + pos_fmt

    def get_piece_color(self, piece: Piece, team_turn: str) -> str:
        """Set piece highlight color."""
        # If not empty cell
        if piece:
            # Orange if selected
            if piece.is_selected:
                return "\033[33m"  
            # White if my turn
            if piece.get_team() == team_turn:
                return "\033[37m"
        return ""

    def get_cell_color(self, cell: Cell, team_turn: str) -> str:
        """Set cell background color."""
        piece = cell.get_piece()
        if cell.is_possible_movement:
            if piece:
                if piece.get_team() != team_turn:
                    return "\033[41m"
            else:
                return"\033[44m"
        return "\033[40m" if cell.get_type() == "dark_cell" else "\033[47m"
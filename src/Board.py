from .system.Packages import Packages as pkg
from .system._methods import clear_screen
from .game.pieces.Piece import Piece

class Board:
    def __init__(self):
        self.letters = pkg.LETTERS_DICT
        self.brd_skins = pkg.BOARD_SKINS_DICT
        
        # _Init_
        self.table = self._initialize_board()
        
    def _initialize_board(self) -> None:
        """Cria o tabuleiro inicial com as células vazias."""
        
        white_cell = Empty_Cell(self.brd_skins["whte_cell"])
        black_cell = Empty_Cell(self.brd_skins["dark_cell"])
        
        # Define the table with white and black cells
        return [
            [(black_cell if (nx + ny) % 2 == 0 else white_cell) for nx in range(8)]
            for ny in range(8)
        ]
        
    def print_formatted_table(self, team_turn: str) -> None:
        """Print the board on console."""
        
        def print_cell(cell_obj: Piece | Empty_Cell, team_turn: str) -> str:
            obj = cell_obj.get_face()
            wall = self.brd_skins["cell_wall"]
            pre_fmt, pos_fmt = "", ""
            
            if cell_obj.team == team_turn:
                pre_fmt, pos_fmt = "\033[37m\033[1m", "\033[0;0m"
            if cell_obj.is_selected:
                pre_fmt, pos_fmt = "\033[33m\033[1m", "\033[0;0m"
            if cell_obj.is_possible_movement:
                pre_fmt, pos_fmt = "\033[34m\033[1m", "\033[0;0m"
            if cell_obj.is_possible_kill:
                pre_fmt, pos_fmt = "\033[31m\033[1m", "\033[0;0m"
                
            return pre_fmt + wall + obj + wall + pos_fmt

        # Print table
        clear_screen()
        for ny in range(7, -1, -1):
            # Print the numbers
            print(f"{ny+1} ", end="")
            
            # Print the objects
            for nx in range(8):
                print(print_cell(self.table[ny][nx], team_turn), end=" ")
            print()

        # Print the letters
        print("   ", end="")
        for letter in self.letters.keys():
            print(letter, end="   ")
        print("\n")

    def insert_in_table(self, coords: tuple[int, int], cell_obj: Piece) -> None:
        x, y = coords
        self.table[y][x] = cell_obj
        
    def get_piece(self, coords: tuple[int, int]) -> Piece:
        x, y = coords
        return self.table[y][x]
        
    
### Class to support get_face()
class Empty_Cell:
    def __init__(self, face: str):
        # Cell appearance
        self.face = face
        self.team = ""
        
        # Color config
        self.is_selected = False
        self.is_possible_kill = False
        self.is_possible_movement = False
        
    def get_face(self) -> str:
        return self.face
###
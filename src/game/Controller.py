from ..system._methods import input_interpreter, throw_error
from ..Board import Board, Empty_Cell
from .pieces.Piece import Piece
from .pieces.Pawn import Pawn
from .pieces.Rook import Rook
from .pieces.Knight import Knight
from .pieces.Bishop import Bishop
from .pieces.Queen import Queen
from .pieces.King import King
import time

class Controller:
    def __init__(self):
        self.board = Board()
        self.team_turn: None | str = None
        self.selected_piece: None | Piece = None
        
        self._initialize_pieces()
    
    def _initialize_pieces(self) -> None:
        # Define positions
        piece_positions = {
            Pawn: [(n, 1, 'white') for n in range(8)] + [(n, 6, 'black') for n in range(8)],
            Rook: [(0, 0, 'white'), (7, 0, 'white'), (0, 7, 'black'), (7, 7, 'black')],
            Knight: [(1, 0, 'white'), (6, 0, 'white'), (1, 7, 'black'), (6, 7, 'black')],
            Bishop: [(2, 0, 'white'), (5, 0, 'white'), (2, 7, 'black'), (5, 7, 'black')],
            Queen: [(3, 0, 'white'), (3, 7, 'black')],
            King: [(4, 0, 'white'), (4, 7, 'black')],
        }
    
        # Instance positions
        for piece_class, positions in piece_positions.items():
            for n, (x, y, team) in enumerate(positions):
                self.board.insert_in_table(cell_obj=piece_class(id_n=n, team=team), coords=[x, y])
        
    def new_turn(self):
        for team in ["white", "black"]:
            # declare team turn
            self.set_team_turn(team)
        
            # Select Piece
            self.select_piece()
            
            # Do Action
            self.move()
        
    def select_piece(self) -> bool | Piece:
        # Check if its valid
        while True:
            try:
                entry = input("Select a piece: ")
                x, y = input_interpreter(entry)
                selected_piece = self.board.get_piece((x, y))

            except:
                throw_error("Invalid position")
            
            else:
                # Check if its not empty
                if isinstance(selected_piece, Empty_Cell):
                    throw_error("No piece in this position!")
                    
                elif selected_piece.team != self.team_turn:
                    throw_error("Select a piece of your team!")
                    
                else:
                    break
        
        # Add new
        selected_piece.set_selected(True)
        self.selected_piece = selected_piece
                
        self.show_table()
    
    def move(self):
        # logic
        input()
        
        # Remove selected
        if self.selected_piece != None:
            self.selected_piece.set_selected(False)
            
        self.show_table()
            
    def set_team_turn(self, team: str) -> None:
        self.team_turn = team
        self.show_table()
        
    def show_table(self) -> None:
        self.board.print_formatted_table(self.team_turn)

if __name__=="__main__":
    controller = Controller()
    controller.select_piece("A1")
    controller.show_table()
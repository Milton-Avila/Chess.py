from ..system._methods import input_interpreter, throw_error
from ..board.Board import Board, Cell, BoardRenderer
from .pieces.Piece import Piece
from .pieces.Pawn import Pawn
from .pieces.Rook import Rook
from .pieces.Knight import Knight
from .pieces.Bishop import Bishop
from .pieces.Queen import Queen
from .pieces.King import King

class Controller:
    def __init__(self):
        self.board = Board()
        self.team_turn: None | str = None
        self.sel_cell: None | Cell = None
        self.sel_piece: None | Piece = None
        self.boardRenderer = BoardRenderer()
        
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
                self.board.insert_in_table(cell_obj=piece_class(id_n=n, coords=([x, y]), team=team))
            
    def _set_team_turn(self, team: str) -> None:
        self.team_turn = team

        self._show_table()
                
    def _show_table(self) -> None:
        self.boardRenderer.print_formatted_table(self.board.table, self.team_turn)
        
    def new_turn(self):
        for team in ["white", "black"]:
            # declare team turn
            self._set_team_turn(team)
        
            # Select Piece
            selected = False
            while not selected:
                selected = self.select_piece()
            
            # Do Action
            moved = False
            while not moved:
                moved = self.move()
        
    def select_piece(self) -> bool | Piece:
        # Check if its valid
        try:
            entry = input("Select a piece: ")
            x, y = input_interpreter(entry)
            self.sel_cell = self.board.get_cell((x, y))
            self.sel_piece = self.sel_cell.get_piece()
            
            # Check if its not empty
            if self.sel_piece == None:
                throw_error("No piece in this position!")
                return False
            
            # Check if right team
            elif self.sel_piece.team != self.team_turn:
                throw_error("Select a piece of your team!")
                return False

        except Exception:
            throw_error("Invalid position")
            return False
        
        # Add new
        self.sel_piece.set_selected(True)
        self._show_table()
        return True
    
    def move(self):
        if not self.get_possible_moves():
            return False

        if not self.do_move():
            return False
        
        return True
        
    def get_possible_moves(self) -> bool:
        sel_x, sel_y = self.sel_piece.get_coords()
        possible_moves = []

        for mov_x, mov_y in self.sel_piece.get_possible_moves():
            pos_x, pos_y = sel_x + mov_x, sel_y + mov_y

            if 0 <= pos_x < 8 and 0 <= pos_y < 8:  # Garante que está dentro do tabuleiro
                try:
                    move_cell = self.board.get_cell((pos_x, pos_y))
                    move_cell.set_possible_movement(True)
                    possible_moves.append(move_cell)
                except IndexError:
                    pass
        
        self._show_table()
        self.possible_moves = possible_moves
        return True
        
    def do_move(self) -> bool:
        while True:
            try:
                # Select move
                entry = input("Select your destiny: ")
                sel_move_coords = input_interpreter(entry)
                sel_move_cell = self.board.get_cell(sel_move_coords)

                # Check if move is valid
                if sel_move_cell not in self.possible_moves:
                    throw_error("Invalid move! Choose a valid position.")
                    continue
                # Check if not ally
                if sel_move_cell.get_piece():
                    if sel_move_cell.get_piece().get_team() == self.team_turn:
                        throw_error("Invalid move! Can't move into an ally.")
                        continue

                # Execute move
                sel_move_cell.set_piece(self.sel_piece)
                self.sel_piece.coords = sel_move_coords
                self.sel_cell.set_piece(None)

                # Reset selected
                self.sel_piece.set_selected(False)
                for move_cell in self.possible_moves:
                    move_cell.set_possible_movement(False)

                self._show_table()
                return True  # Movimento realizado com sucesso

            except Exception:
                throw_error("Invalid input! Please enter a valid position.")
        
if __name__=="__main__":
    pass
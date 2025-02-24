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
                self.sel_cell = self.board.get_cell((x, y))
                self.sel_piece = self.sel_cell.get_piece()

            except:
                throw_error("Invalid position")
            
            else:
                # Check if its not empty
                if self.sel_piece == None:
                    throw_error("No piece in this position!")
                
                # Check if right team
                elif self.sel_piece.team != self.team_turn:
                    throw_error("Select a piece of your team!")
                    
                else:
                    break
        
        # Add new
        self.sel_piece.set_selected(True)
                
        self.show_table()
    
    def move(self):
        # Define locations
        sel_piece_coords = self.sel_piece.get_coords()
        sel_x, sel_y = sel_piece_coords
        moves_list = self.sel_piece.get_possible_moves()

        # See possible moves
        possible_moves_objs: list[Cell] = []
        for mov_x, mov_y in moves_list:
            # Define positions
            pos_x = sel_x + mov_x
            pos_y = sel_y + mov_y

            # Check index range
            if (pos_x >= 0) and (pos_y >= 0):
                try:
                    # Append moves
                    move_cell = self.get_cell((pos_x, pos_y))
                    move_cell.set_possible_movement(True)
                    possible_moves_objs.append(move_cell)

                except:
                    pass

        self.show_table()

        # Select move
        sel_move_coords: tuple[int, int] = input_interpreter(input("Select your destiny: "))
        
        # Move if possible
        if self.get_cell(sel_move_coords) in possible_moves_objs:
            sel_move_cell = self.board.get_cell(sel_move_coords)
            sel_move_cell.set_piece(self.sel_piece)
            self.sel_piece.coords = sel_move_coords
            self.sel_cell.set_piece(None)

        # Reset selected
        self.sel_piece.set_selected(False)
        for move_cell in possible_moves_objs:
            move_cell.set_possible_movement(False)
        
        self.show_table()
            
    def set_team_turn(self, team: str) -> None:
        self.team_turn = team

        self.show_table()
        
    def get_board(self) -> list[list[Cell]]:
        return self.board.table
    
    def get_cell(self, coords: tuple[int, int]) -> Cell:
        x, y = coords
        
        return self.get_board()[y][x]
            
    def show_table(self) -> None:
        self.boardRenderer.print_formatted_table(self.get_board(), self.team_turn)

if __name__=="__main__":
    controller = Controller()
    controller.select_piece("A1")
    controller.show_table()
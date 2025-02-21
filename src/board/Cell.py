from ..system.Packages import Packages as pkg
from ..game.pieces.Piece import Piece

###
class Cell:
    def __init__(self, cell_type: str):
        self.brd_skins = pkg.BOARD_SKINS
        self.piece: None | Piece = None
        
        # Cell appearance
        self.face = self.brd_skins[cell_type]
        self.cell_type = cell_type
        
        # Color config
        self.is_possible_movement = False
        
    def get_face(self) -> str:
        if self.piece:
            return self.piece.get_face()
        
        return self.face
        
    def get_type(self) -> str:
        return self.cell_type
    
    def get_piece(self) -> Piece | None:
        return self.piece
    
    def set_piece(self, piece: Piece | None) -> None:
        if piece:
            self.piece = piece
        else:
            self.piece.set_selected(False)
            self.piece = None
    
    # Color method
    def set_possible_movement(self, state: bool) -> None:
        self.is_possible_movement = state
###
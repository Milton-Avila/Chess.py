from ..system.Packages import Packages as pkg

class Piece:
    def __init__(self, team: str):
        self.team = team
        
        # Color config
        self.is_selected = False
        self.is_possible_kill = False
        self.is_possible_movement = False
        
        # Pre-instance
        self.face: str = ""
    
    def get_face(self) -> str:
        return self.face
        
    def set_face(self, skin_n):
        self.face = pkg.PIECES_SKINS[self.team][skin_n]
    
    # Color methods
    def set_selected(self, state: bool) -> None:
        self.is_selected = state
        
    def set_possible_kill(self, state: bool) -> None:
        self.is_possible_kill = state
        
    def set_possible_movement(self, state: bool) -> None:
        self.is_possible_movement = state
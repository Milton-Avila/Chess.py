from ...system.Packages import Packages as pkg

class Piece:
    def __init__(self, team: str, coords: tuple[int, int]):
        self.team = team
        self.coords = coords
        
        # Color config
        self.is_selected = False
        
        # Pre-instance
        self.face: str = ""
    
    def get_face(self) -> str:
        return self.face
        
    def set_face(self, skin_n):
        self.face = pkg.PIECES_SKINS[self.team][skin_n]
    
    def get_coords(self) -> tuple[int, int]:
        return self.coords
    
    def get_id(self) -> str:
        return self.id
    
    def get_team(self) -> str:
        return self.team

    def get_possible_moves(self) -> list[tuple[int | str, int | str]]:
        pass
    
    # Color methods
    def set_selected(self, state: bool) -> None:
        self.is_selected = state
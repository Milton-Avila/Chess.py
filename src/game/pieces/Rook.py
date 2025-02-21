from .Piece import Piece

class Rook(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_rook_" + str(id_n)
        self.set_face(1)
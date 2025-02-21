from .Piece import Piece

class Bishop(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_bishop_" + str(id_n)
        self.set_face(3)
        
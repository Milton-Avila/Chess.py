from .Piece import Piece

class King(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_king_" + str(id_n)
        self.set_face(5)
         
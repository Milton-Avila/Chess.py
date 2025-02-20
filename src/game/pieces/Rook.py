from .Piece import Piece

class Rook(Piece):
    def __init__(self, id_n, team):
        super().__init__(team)
        
        self.id = team + "_rook_" + str(id_n)
        self.set_face(1)
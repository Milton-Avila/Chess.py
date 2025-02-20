from .Piece import Piece

class Knight(Piece):
    def __init__(self, id_n, team):
        super().__init__(team)
        
        self.id = team + "_knight_" + str(id_n)
        self.set_face(2)
        
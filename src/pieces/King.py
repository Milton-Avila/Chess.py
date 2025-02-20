from .Piece import Piece

class King(Piece):
    def __init__(self, id_n, team):
        super().__init__(team)
        
        self.id = team + "_king_" + str(id_n)
        self.set_face(5)
        
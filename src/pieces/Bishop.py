from .Piece import Piece

class Bishop(Piece):
    def __init__(self, id_n, team):
        super().__init__(team)
        
        self.id = team + "_bishop_" + str(id_n)
        self.set_face(3)
        
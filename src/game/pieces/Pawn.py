from .Piece import Piece

class Pawn(Piece):
    def __init__(self, id_n: int, team: str) -> None:
        super().__init__(team)
        
        self.id = team + "_pawn_" + str(id_n)
        self.set_face(0)
        
        # Class exclusive
        self.already_moved = False
        
    def get_id(self) -> str:
        return self.id
        
    def get_possible_moves(self) -> list[str]:
        # Pawn move 2 cells if it is its first move
        if not self.already_moved:
            y_len = 2
        else:
            y_len = 1
            
        # Move up if in white team
        if self.team == "white":
            y_len *= -1
            
        # ***
        print(y_len)
     
# Testing
if __name__=="__main__":
    p1 = Pawn('1', "black")
    print(p1.get_possible_moves())
    print(p1.get_face())
    print(p1.id)
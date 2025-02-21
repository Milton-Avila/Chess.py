from .Piece import Piece

class Pawn(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]) -> None:
        super().__init__(team, coords)
        
        self.id = team + "_pawn_" + str(id_n)
        self.set_face(0)
        
        # Class exclusive
        self.already_moved = False
        
    def get_possible_moves(self) -> list[tuple[int, int]]:
        possibilities_list = []

        # Pawn move 2 cells if it is its first move
        if not self.already_moved:
            possibilities_list.append((0, 2))
            self.already_moved = True

        possibilities_list.append((0, 1))

        # Move up if in white team
        if self.team == "black":
            return [(nx, ny*-1) for nx, ny in possibilities_list]
            
        return possibilities_list
     
# Testing
if __name__=="__main__":
    p1 = Pawn('1', "black")
    print(p1.get_possible_moves())
    print(p1.get_face())
    print(p1.id)
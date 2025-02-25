from .Piece import Piece

class Rook(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_rook_" + str(id_n)
        self.set_face(1)
         
    def get_possible_moves(self) -> list[tuple[int | str, int | str]]:
        possibilities_list: list[tuple[int | str, int | str]] = []

        possibilities_list = [("n", 0), ("-n", 0), (0, "n"), (0, "-n")]
            
        return possibilities_list
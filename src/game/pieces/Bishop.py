from .Piece import Piece

class Bishop(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_bishop_" + str(id_n)
        self.set_face(3)
         
    def get_possible_moves(self) -> list[tuple[str, str]]:
        possibilities_list: list[tuple[str, str]] = []

        tup = ("n", "-n")

        [[possibilities_list.append((x, y)) for y in tup] for x in tup]

        return possibilities_list
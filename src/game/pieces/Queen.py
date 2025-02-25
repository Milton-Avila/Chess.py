from .Piece import Piece

class Queen(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_king_" + str(id_n)
        self.set_face(4)
         
    def get_possible_moves(self) -> list[tuple[int | str, int | str]]:
        possibilities_list: list[tuple[int | str, int | str]] = []

        tup = ("n", "-n", 0)

        [[possibilities_list.append((x, y)) for y in tup] for x in tup]
        possibilities_list.remove((0, 0))

        return possibilities_list
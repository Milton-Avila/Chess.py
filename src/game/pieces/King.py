from .Piece import Piece

class King(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_king_" + str(id_n)
        self.set_face(5)
         
    def get_possible_moves(self) -> list[tuple[int, int]]:
        possibilities_list: list[tuple[int, int]] = []

        tup1, tup2 = (-1, 0, 1), (-1, 0, 1)
        
        [[possibilities_list.append((x, y)) for x in tup1] for y in tup2]
        [[possibilities_list.append((x, y)) for x in tup2] for y in tup1]
        possibilities_list.remove((0, 0))
            
        return possibilities_list
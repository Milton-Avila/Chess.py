from .Piece import Piece

class Knight(Piece):
    def __init__(self, id_n: int, team: str, coords: tuple[int, int]):
        super().__init__(team, coords)
        
        self.id = team + "_knight_" + str(id_n)
        self.set_face(2)
        
    def get_possible_moves(self) -> list[tuple[int, int]]:
        possibilities_list = []

        tup1, tup2 = (1, -1), (2, -2)
        
        [[possibilities_list.append((nx, ny)) for nx in tup1] for ny in tup2]
        [[possibilities_list.append((nx, ny)) for nx in tup2] for ny in tup1]
            
        return possibilities_list
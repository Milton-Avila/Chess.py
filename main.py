import os, time

class Piece:
    def __init__(self, id: int, xy: list) -> None:
        self.Skins1: list = ['p', 't', 'k', 'b', 'q', 'w']
        self.Skins2: list = ['♙', '♖', '♘', '♗', '♕', '♔']

        self.Skins: list = self.Skins2
        self.id: int = id
        self.skin: str
        self.type: str
        self.alive: bool = True
        self.xy: list = xy

    def getSkin(self) -> str:
        return self.skin

class Pawn(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.moved: bool = False
        self.skin: str = self.Skins[0]
        self.type: str = 'Pawn'

class Rook(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[1]
        self.type: str = 'Rook'

class Knight(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[2]
        self.type: str = 'Knigh'

class Bishop(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[3]
        self.type: str = 'Bishop'

class Queen(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[4]
        self.type: str = 'Queen'

class King(Piece):
    def __init__(self, id: int, xy: list) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[5]
        self.type: str = 'King'

class Chess:
    def __init__(self) -> None:
        self.Letters: dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.Team: dict = {'Ally': 0, 'Enemy': 1}

        self.selectedPiece: Piece
        self.turn: str = 'Ally'
        self.allys: dict = {}
        self.enemy: dict = {}
        self.pieces: list = [self.allys, self.enemy]
        self.allyCaptured: list = []
        self.enemyCaptured: list = []

        self.createPieces()
        self.createFrame()
        self.updateFrame()

    def passTurn(self) -> None:
        if self.turn == 'Ally':
            self.turn == 'Enemy'
        else: self.turn == 'Ally'

    def movePiece(self, piece: Piece, xy: list) -> None:
        match piece.type:
            case 'Pawn':
                self.movePawn(piece, xy)
            case 'Rook':
                pass
            case 'Knigh':
                pass
            case 'Bishop':
                pass
            case 'Queen':
                pass
            case 'King':
                pass

    def movePawn(self,) -> None:
        pass

    # def selectPiece(self) -> None:
    #     xy: list = input('Insert the coordinates of the selected piece: ')
    #     selected: Piece = self.table[-xy[1]][self.Letters.get(xy[0])]

    #     if selected != []:
    #         self.selectedPiece = selected
    #         self.highlightSelected(self.allys[1])
    #         pass

    def highlightSelected(self, piece: Piece) -> None:
        pass

    def inputOnFrame(self, xy: list, value: Piece, update: bool = True) -> None:
        self.table[-(xy[1])][self.Letters.get(xy[0])] = value
        if update: self.updateFrame()

    def updateFrame(self, highlight: Piece = None) -> None:
        _aux: bool = True
        _count: int = 9
        os.system('cls')
        
        for i in self.table:
            _count -= 1
            print(f'{_count}', end='  ')
            
            for j in i:
                print((('| |' if _aux else '|-|') if j==[] else (f'|{j.getSkin()}|' if j!=highlight else (f'\033[1m'+'|{j}|'+'\033[0;0m'))), end=' ')
                if _aux:
                    _aux = False
                else: _aux = True
            print()
            
            if _aux:
                _aux = False
            else: _aux = True
        print('    ', end=''), [print(l, end='   ') for l in self.Letters], print('\n')

    def createFrame(self) -> None:
        self.table: list = [[[] for _ in range(8)] for _ in range(8)]
        [[(self.inputOnFrame(self.pieces[i][p].xy, self.pieces[i][p], False), print(p)) for p in self.pieces[i]] for i in range(0,2)]

    def createPieces(self) -> None:
        # Pawns
        [self.createPiece(Pawn, [l,2], 'Ally') for l in self.Letters]
        [self.createPiece(Pawn, [l,7], 'Enemy') for l in self.Letters]

        # Rooks
        [self.createPiece(Rook, [l,1], 'Ally') for l in ['A', 'H']]
        [self.createPiece(Rook, [l,8], 'Enemy') for l in ['A', 'H']]

        # Knights
        [self.createPiece(Knight, [l,1], 'Ally') for l in ['B', 'G']]
        [self.createPiece(Knight, [l,8], 'Enemy') for l in ['B', 'G']]

        # Bishops
        [self.createPiece(Bishop, [l,1], 'Ally') for l in ['C', 'F']]
        [self.createPiece(Bishop, [l,8], 'Enemy') for l in ['C', 'F']]
        
        # Queen
        self.createPiece(Queen, ['D',1], 'Ally')
        self.createPiece(Queen, ['D',8], 'Enemy')
        
        # King
        self.createPiece(King, ['E',1], 'Ally')
        self.createPiece(King, ['E',8], 'Enemy')

    def createPiece(self, piece: Piece, xy: list, team: str) -> Piece:
        Piece_ = piece(len(self.pieces[self.Team.get(team)]), xy)
        self.pieces[self.Team.get(team)].update({Piece_.id: Piece_})

    def getPiecesOnboard(self) -> list:
        return self.pieces

def main():
    while True:
        chess = Chess()

        # time.sleep(1)

        # Chess.inputOnFrame(['A', 5], 't')

        chess.updateFrame()

        # chess.selectPiece()
        input()

if __name__ == '__main__': main()
import os, time

class Piece:
    def __init__(self, id: int, xy: list, ally: int = 0) -> None:
        self.Skins1: list = [['p', 't', 'k', 'b', 'q', 'w'], ['P', 'T', 'K', 'B', 'Q', 'W']]
        self.Skins2: list = [['♙', '♖', '♘', '♗', '♕', '♔'], ['♟', '♜', '♞', '♝', '♛', '♚']]
        self.Skins3: list = [[], []]            # Free 2 custom

        self.Skins: list = self.Skins2          # Select Preferred skin
        self.id: int = id
        self.skin: str
        self.type: str
        self.alive: bool = True
        self.xy: list = xy

    def getSkin(self) -> str:
        return self.skin

class Pawn(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy, ally)
        self.moved: bool = False
        self.skin: str = self.Skins[ally][0]
        self.type: str = 'Pawn'

class Rook(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[ally][1]
        self.type: str = 'Rook'

class Knight(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[ally][2]
        self.type: str = 'Knigh'

class Bishop(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[ally][3]
        self.type: str = 'Bishop'

class Queen(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[ally][4]
        self.type: str = 'Queen'

class King(Piece):
    def __init__(self, id: int, xy: list, ally: int) -> None:
        super().__init__(id, xy)
        self.skin: str = self.Skins[ally][5]
        self.type: str = 'King'

class Chess:
    def __init__(self) -> None:
        self.Letters: dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.Team: dict = {'Enemy': 0, 'Ally': 1}
        self.BoardSkin: dict = {'cellWall': '|', 'darkCell': '-'}   # Select preferred theme

        self.selectedPiece: Piece | None = None
        self._aux: bool = True
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
                self.movePawn(piece, xy)
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

    def moveRook(self,) -> None:
        pass

    #...

    def selectPiece(self) -> None:
        while True:
            try:
                self.clearLine(), print()
                xy: str = input('Insert the coordinates of the selected piece: ')
                selectedPiece: Piece | list = self.table[-int(xy[1])][self.Letters.get(xy[0])]

                if selectedPiece != []:
                    self.selectedPiece = selectedPiece

                else:
                    print('Selected a blank space, select a piece')   
                    time.sleep(1)
                    self.clearLine()
                break

            except:
                print('Invalid input, try again.')
                time.sleep(1)
                self.clearLine()

    def inputOnFrame(self, xy: list, value: Piece, update: bool = True) -> None:
        self.table[-(xy[1])][self.Letters.get(xy[0])] = value
        if update: self.updateFrame()

    def getCell(self, type: int) -> str:
        match type:
            case 1:
                return f"{self.BoardSkin.get('cellWall')} {self.BoardSkin.get('cellWall')}"
            case 2:
                return f"{self.BoardSkin.get('cellWall')}{self.BoardSkin.get('darkCell')}{self.BoardSkin.get('cellWall')}"

    def updateFrame(self) -> None:
        _count: int = 9
        os.system('cls')
        
        for i in self.table:
            _count -= 1
            print(f'{_count}', end='  ')
            
            for j in i:
                if j==[]:
                    print(f'{self.getCell(1)}' if self._aux else f'{self.getCell(2)}', end=' ')

                elif self.selectedPiece != None:

                    if j == self.selectedPiece:
                        print('\033[33m\033[1m'+f'|{j.getSkin()}|', end='\033[0;0m ')
                    
                    else:
                        print(f'|{j.getSkin()}|', end=' ')

                else:
                    print(f'|{j.getSkin()}|', end=' ')

                self.updAux()
            print()

            self.updAux()
        print('    ', end=''), [print(l, end='   ') for l in self.Letters], print('\n')

    def createFrame(self) -> None:
        self.table: list = [[[] for _ in range(8)] for _ in range(8)]
        [[(self.inputOnFrame(self.pieces[i][p].xy, self.pieces[i][p], False)) for p in self.pieces[i]] for i in range(0,2)]

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
        Piece_ = piece(len(self.pieces[0]) + len(self.pieces[1]), xy, self.Team.get(team))
        self.pieces[self.Team.get(team)].update({Piece_.id: Piece_})

    def clearLine(self) -> None:
        print("\033[A                                                                                                                            \033[A")

    def getPiecesOnboard(self) -> list:
        return self.pieces
    
    def updAux(self) -> None:
        if self._aux:
            self._aux = False
        else: self._aux = True

def main():
    chess = Chess()
    while True:

        chess.updateFrame()

        chess.selectPiece()

        # chess.inputOnFrame(['A', 5], Pawn(99, ['E', 4]))

if __name__ == '__main__': main()
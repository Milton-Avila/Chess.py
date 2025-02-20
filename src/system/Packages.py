from settings import Settings

class Packages:
    PIECES_SKINS_DICT: dict[str, dict[str, list[str]]] = {
        'letters': {'black': ['p', 't', 'k', 'b', 'q', 'w'], 'white': ['P', 'T', 'K', 'B', 'Q', 'W']},
        'pieces': {'black': ['♙', '♖', '♘', '♗', '♕', '♔'], 'white': ['♟', '♜', '♞', '♝', '♛', '♚']},
        'custom': {'black': [], 'white': []},    # Free 2 custom
    }
    BOARD_SKINS_DICT: dict[str, str] = {
        'cell_wall': '|',
        'dark_cell': '-',
        'whte_cell': ' ',
    }
    LETTERS_DICT: dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    # Define skins according to settings
    PIECES_SKINS = PIECES_SKINS_DICT[Settings.sel_skin]
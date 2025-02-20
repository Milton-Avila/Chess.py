from .Packages import Packages as pkg
import os

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    
def input_interpreter(coords: str) -> tuple[int, int]:
    x = pkg.LETTERS_DICT[coords[0]]
    y = int(coords[1])-1
    
    return (x, y)
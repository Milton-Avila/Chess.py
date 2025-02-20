from .Packages import Packages as pkg
import os, time

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    
def throw_error(error_msg: str) -> None:
    print(error_msg)
    time.sleep(1)
    print("\033[A                                             \033[A")
    print("\033[A                                             \033[A")
    
def input_interpreter(coords: str) -> tuple[int, int]:
    x = pkg.LETTERS_DICT[coords[0]]
    y = int(coords[1])-1
    
    return (x, y)
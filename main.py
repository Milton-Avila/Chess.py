from src.game.Controller import Controller

def main():
    controller = Controller()
    
    while True:
        controller.new_turn()
        
if __name__ == "__main__":
    main()

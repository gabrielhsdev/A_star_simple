from ..display import Display

class gameState:
    """Class for the game state
    Attributes:
        pathfinder (Pathfinder): pathfinder object
        pygame (pygame): pygame module
        state (str): state of the game
        display (Display): display object
    """
    def __init__(self, pathfinder, pygame):
        """Constructor for gameState class
        Parameters:
            pathfinder (Pathfinder): pathfinder object
            pygame (pygame): pygame module
        Returns:
            None
        """
        self.pathfinder = pathfinder
        self.state = 'play'
        self.display = Display(pygame) 
        self.pygame = pygame
    

    def gameLoop(self):
        """Main game loop
        Parameters:
            None
        Returns:
            None
        """
        if self.state == 'play': 
            self.pathfinder.pathfind()
            self.display.drawBoard(self.pathfinder)
        return None


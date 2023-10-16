class Display:
   """Display class for the pathfinder game
   Attributes:
      pygame (pygame): pygame module
      screenW (int): screen width
      screenH (int): screen height
   """
   screenW = None
   screenH = None
   colors = {}
   def __init__(self, pygame):
      """Constructor for Display class
      Parameters:
         pygame (pygame): pygame module
      Returns:
         None
      """
      self._pygame = pygame
   
      # Get screen width and height
      infoObject = pygame.display.Info()
      self._screenW = infoObject.current_w
      self._screenH = infoObject.current_h
   
   def setColors(self):
      """Sets the colors for the display
      Parameters:
         None
      Returns:
         None
      """
      self.colors["white"] = (255, 255, 255)
      self.colors["black"] = (0, 0, 0)
      self.colors["red"] = (255, 0, 0)
      self.colors["green"] = (0, 255, 0)
      self.colors["blue"] = (0, 0, 255)
      self.colors["yellow"] = (255, 255, 0)
      return None

   def drawBoard(self, board):
      """Draws the board on the screen
      Parameters:
         board (Board): board to draw
      Returns:
         None
      """
      rows = board.getRows() 
      cols = board.getCols()
      for x in range(rows):
         for y in range(cols):
            node = board.getNode(x, y)

            # Calculate node size
            nodeW = self._screenW / cols
            nodeH = self._screenH / rows
            size = (nodeW, nodeH)
            
            # Set node color
            color = "white"
            if node == board.getStart() or node == board.getFinish():
               color = "yellow"
            elif node in board.path:
               color = "blue"
            elif node in board.closedList:
               color = "red"
            elif node in board.openList:
               color = "green"
            elif node.isWall:
               color = "black"
            else:
               color = "white"

            self.drawNode(node, size, color) 
   
   def drawNode(self, node, size, color = "white"):
      """Draws a node on the screen
      Parameters:
         node (Node): node to draw
      Returns:
         None
      """
      pygame = self._pygame
      screen = pygame.display.get_surface()
      if node.isWall:
         color = "black"

      # The filled square
      pygame.draw.rect(screen, color, pygame.Rect(node.screenPosition, size))
      
      # Draw the border, always black
      pygame.draw.rect(screen, "black", pygame.Rect(node.screenPosition, size), 1)

      stats = {
         "p": str(node.getCoord()),
         "f": "f: " + str(node.getF()),
         "g": "g: " + str(node.getG()),
         "h": "h: " + str(node.getH()),
      }
   
      font = pygame.font.Font('freesansbold.ttf', 12)
      
      posSum = 5;
      for stat in stats:
         # Text is key + value 
         text = str(stats[stat])
         textSurface = font.render(text, True, (0, 0, 0))
         textRect = textSurface.get_rect()
         textRect.topleft = (node.screenPosition[0] + 5, node.screenPosition[1] + posSum)
         screen.blit(textSurface, textRect)
         posSum += 12

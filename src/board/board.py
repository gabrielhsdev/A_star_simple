from ..node import Node
class Board:
    """Represents a board of the game.
    Attributes:
        rows (int): number of rows in board
        cols (int): number of columns in board
    """
    def __init__(self, rows, cols, screenW, screenH):
        self._rows = rows
        self._cols = cols
        self._nodes = [[Node(x, y) for y in range(cols)] for x in range(rows)]
        
        # Calculate node screen positions based on screen width and height and number of rows and columns
        nodeW = screenW / cols
        nodeH = screenH / rows
        for x in range(rows):
            for y in range(cols):
                node = self.getNode(x, y)
                node.screenPosition = (nodeW * y, nodeH * x)

        return None


    def getNode(self, x, y):
        """Returns the node at the given coordinates.
        Parameters:
            x (int): x coordinate of node
            y (int): y coordinate of node
        Returns:
            Node: node at given coordinates
        """
        if x < 0 or x >= self._rows or y < 0 or y >= self._cols:
            print("Error: getNode() called with invalid coordinates | x = " + str(x) + ", y = " + str(y))
            return None
        else:
            return self._nodes[x][y]

    def getRows(self):
        """Returns the number of rows in the board.
        Parameters:
            None
        Returns:
            int: number of rows in board
        """
        return self._rows

    def getCols(self):
        """Returns the number of columns in the board.
        Parameters:
            None
        Returns:
            int: number of columns in board
        """
        return self._cols

    def testNodes(self):
        """Tests the nodes in the board.
        Parameters:
            None
        Returns:
            None
        """
        for x in range(self._rows):
            for y in range(self._cols):
                node = self.getNode(x, y)
                print("Node at (" + str(x) + ", " + str(y) + ")")
        return None

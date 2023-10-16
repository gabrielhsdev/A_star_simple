class Node:
    """Node class for A* algorithm
    Attributes:
        f (int): f value of node
        g (int): g value of node
        h (int): h value of node
        parentNode (Node): parent node of current node
        coord (tuple): coordinate of node in grid
        screenPosition (tuple): screen position of node
        isWall (bool): whether node is a wall
    """ 
    f = 0
    g = 0
    h = 0
    _coord = (None, None)
    parentNode = None
    screenPosition = (0, 0)
    isWall = False

    def __init__(self, x, y):
        """Constructor for Node class
        Parameters:
            x (int): x coordinate of node in grid
            y (int): y coordinate of node in grid
        Returns:
            None
        """
        self._coord = (x, y)
        return None
    
    def getCoord(self):
        """Returns the coordinate of the node
        Parameters:
            None
        Returns:
            tuple: coordinate of node
        """
        return self._coord

    def getF(self):
        """Returns the f value of the node
        Parameters:
            None
        Returns:
            int: f value of node
        """
        return self.f

    def getG(self):
        """Returns the g value of the node
        Parameters:
            None
        Returns:
            int: g value of node
        """
        return self.g

    def getH(self):
        """Returns the h value of the node
        Parameters:
            None
        Returns:
            int: h value of node
        """
        return self.h

    def setF(self, f):
        """Sets the f value of the node
        Parameters:
            f (int): f value to set
        Returns:
            None
        """
        self.f = f
        return None
    
    def setG(self, g):
        """Sets the g value of the node
        Parameters:
            g (int): g value to set
        Returns:
            None
        """
        self.g = g
        return None
    
    def setH(self, h):
        """Sets the h value of the node
        Parameters:
            h (int): h value to set
        Returns:
            None
        """
        self.h = h
        return None

    def toString(self):
        """Returns a string representation of the node
        Parameters:
            None
        Returns:
            str: string representation of node
        """
        return "Node at " + str(self._coord) + " | f: " + str(self.getF()) + ", g: " + str(self.getG()) + ", h: " + str(self.getH())

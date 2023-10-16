from ..board import Board
class Pathfinder(Board):
    """Represents a pathfinder board.
    Attributes:
        openList (dict): dictionary of nodes in open list
        closedList (dict): dictionary of nodes in closed list
        currentNode (Node): current node
        _start (Node): start node
        _finish (Node): finish node
    """
    openList = []
    closedList = {}
    currentNode = None
    _start = None
    _finish = None
    path = []
    pathFound = False

    def __init__(self, rows, cols, screenW, screenH, start, finish, map = None):
        """Constructor for Pathfinder class
        Parameters:
            rows (int): number of rows in board
            cols (int): number of columns in board
            screenW (int): screen width
            screenH (int): screen height
            start (tuple): start coordinates
            finish (tuple): finish coordinates
        Returns:
            None
        """
        super().__init__(rows, cols, screenW, screenH)
        self._start = self.getNode(start[0], start[1])
        self._finish = self.getNode(finish[0], finish[1])

        # Set map to walls
        if map:
            self.setMap(map)

        # Put start node in open list
        self.openList.append(self._start)
    
    def setMap(self, map):
        """Set blocks in map to walls.
        Parameters:
            map (list(list(int))): map of walls
        Returns:
            None
        """
        for x in range (self.getRows()):
            for y in range (self.getCols()):
                if map[x][y] == 1 and (x, y) != self._start.getCoord() and (x, y) != self._finish.getCoord():
                    self.getNode(x, y).isWall = True
    
    def pathfind(self):
        """Pathfinds from start node to finish node.
        Parameters:
            None
        Returns:
            None
        """
        run = True

        # While open list is not empty
        while len(self.openList) > 0 and run and not self.pathFound:
            # Run once per game loop
            run = False

            # Get node with lowest f value
            self.currentNode = self.openList[0]
            for node in self.openList:
                if node.getF() < self.currentNode.getF():
                    self.currentNode = node

            # If current node is finish node, path has been found
            if self.currentNode == self._finish:
                self.pathFound = True
            # Move current node from open list to closed list
            self.openList.remove(self.currentNode)
            self.closedList[self.currentNode] = True

            # Get current node's neighbors
            neighbors = self.getNeighbors(self.currentNode)

            # For each neighbor
            for neighbor in neighbors:
                # If neighbor is in closed list, skip it
                if neighbor in self.closedList:
                    continue

                # Calculate g value
                g = self.currentNode.getG() + 1

                # If neighbor is not in open list, add it
                if neighbor not in self.openList:
                    self.openList.append(neighbor)
                # Else if neighbor's g value is less than calculated g value, skip it
                elif g >= neighbor.getG():
                    continue

                # Set neighbor's parent node to current node
                neighbor.parentNode = self.currentNode

                # Calculate neighbor's g, h, and f values
                neighbor.setG(self.calcG(neighbor)) 
                neighbor.setH(self.calcH(neighbor))
                neighbor.setF(neighbor.g + neighbor.h)
        
        if self.pathFound == True and self.path == []:
            print("Path found")
            # Get path from finish node to start node
            path = []
            node = self._finish
            while node != self._start:
                path.append(node)
                node = node.parentNode
                print(node.getCoord())
            path.append(self._start)
            path.reverse()
            self.path = path


    
    def getNeighbors(self, node):
        """Returns the neighbors of the given node.
        Parameters:
            node (Node): node to get neighbors of
        Returns:
            list(Node): list of neighbors
        """
        neighbors = []
        # Check nodes 8 directions around current node
        for x in range(-1, 2):
            for y in range(-1, 2):
                # Skip current node
                if x == 0 and y == 0:
                    continue
                
                # Check if neighbor is out of bounds
                if node.getCoord()[0] + x < 0 or node.getCoord()[0] + x >= self._rows or node.getCoord()[1] + y < 0 or node.getCoord()[1] + y >= self._cols:
                    continue

                # Get neighbor node
                neighbor = self.getNode(node.getCoord()[0] + x, node.getCoord()[1] + y)

                # If neighbor is not a wall, add it to list
                if neighbor and not neighbor.isWall:
                    neighbors.append(neighbor)
        
        return neighbors

    def calcG(self, node):
        """Calculates the h value of the given node.
        Parameters:
            node (Node): node to calculate h value of
        Returns:
            int: h value of node
        """
        # Just the sum of square of differences in x and y coordinates from start node
        return (node.getCoord()[0] - self._start.getCoord()[0]) ** 2 + (node.getCoord()[1] - self._start.getCoord()[1]) ** 2

    def calcH(self, node):
        """Calculates the h value of the given node.
        Parameters:
            node (Node): node to calculate h value of
        Returns:
            int: h value of node
        """
        # Just the sum of square of differences in x and y coordinates from finish node
        return (node.getCoord()[0] - self._finish.getCoord()[0]) ** 2 + (node.getCoord()[1] - self._finish.getCoord()[1]) ** 2

    def getStart(self):
        """Returns the start node.
        Parameters:
            None
        Returns:
            Node: start node
        """
        return self._start
    
    def getFinish(self):
        """Returns the finish node.
        Parameters:
            None
        Returns:
            Node: finish node
        """
        return self._finish


#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     #			              	
# Project 1: Conway's Game of Life 				     #			          
# Class: Cell					   		     #					                          
# Created On: 8/1/2016             				     #			              
#--------------------------------------------------------------------#

class Cell:
    """A cell which will know its coordinates as well as well as its
       current state (alive or dead)"""
        
    def __init__(self, x, y, rows=0, columns=0):
        """Construct a Cell with coordinates and the size of the world"""
        # The coordinate for this cell in the world
        self.x = x
        self.y = y
        self.coordinates = (x, y)

        # The number of rows and columns in the game world
        self.rows = rows
        self.columns = columns

        # The current state for this cell (0 = dead, 1 = alive)
        self.state = 0
        
        # Create a list of all of this cell's neighbors based on its coordinates
        if self.rows != 0 and self.columns != 0:
            self.find_neighbors()

    def cycle(self):
        """TO-DO Method which implements the rules of Conway's Game of Life for a cell"""

    def update_world(self, update):
        """TO-DO Updates the current board configuration"""
        self.world = update
    
    
    #-------------------------#
    #                         #
    #     Update Methods      #
    #                         #
    #-------------------------#
    
    def check_rules(self):
        """TO-DO Checks which rules of the game apply to this cell on this frame
           and then updates its state accordingly"""
           
        # Count living neighbors
        alive = 0
        for cell in self.neighbors:
            if cell.state == 1:
                alive = alive + 1
                
        # Is this Cell alive or dead currently?
        if self.state == 1:
            if alive < 2 or alive > 3:
                # Cell dies from under or over population
                self.state = 0
        else:
            if alive == 3:
                # Cell comes back to life
                self.state = 1
    
    #-------------------------#
    #                         #
    #    Neighbors Methods    #
    #                         #
    #-------------------------#
    
    def find_neighbors(self):
        """Create a list of the neighbors of this cell"""
        self.neighbors = []
        
        # Check to see if this Cell is a corner
        location = self.is_corner()
        if location != False:
            self.calc_neighbors_corner(location)
            return

        # Check to see if this Cell is on an edge
        location = self.is_edge()
        if location != False:
            self.calc_neighbors_edge(location)
            return

        # Cell must be an interior one
        self.calc_neighbors_interior()

    def calc_neighbors_corner(self, location):
        """Calculate the neighbors of a corner cell"""
        if location == 'tl':
            self.neighbors.extend([Cell(self.x, self.y+1), Cell(self.x+1, self.y),
                                   Cell(self.x+1, self.y+1)])
        elif location == 'tr':
            self.neighbors.extend([Cell(self.x, self.y-1), Cell(self.x+1, self.y),
                                   Cell(self.x+1, self.y-1)])
        elif location == 'bl':
            self.neighbors.extend([Cell(self.x-1, self.y), Cell(self.x-1, self.y+1),
                                   Cell(self.x, self.y+1)])
        else:
             self.neighbors.extend([Cell(self.x-1, self.y), Cell(self.x-1, self.y-1),
                                   Cell(self.x, self.y-1)])

    def calc_neighbors_edge(self, location):
        """Calculate the neighbors of an edge cell"""
        if location == 'le':
            self.neighbors.extend([Cell(self.x-1, self.y), Cell(self.x-1, self.y+1),
                                   Cell(self.x, self.y+1),
                                   Cell(self.x+1, self.y), Cell(self.x+1, self.y+1)])
        elif location == 're':
            self.neighbors.extend([Cell(self.x-1, self.y), Cell(self.x-1, self.y-1),
                                   Cell(self.x, self.y-1),
                                   Cell(self.x+1, self.y), Cell(self.x+1, self.y-1)])
        elif location == 'te':
            self.neighbors.extend([Cell(self.x, self.y-1), Cell(self.x, self.y+1),
                                   Cell(self.x+1, self.y-1), Cell(self.x+1, self.y),
                                   Cell(self.x+1, self.y+1)])
        else:
            self.neighbors.extend([Cell(self.x, self.y-1), Cell(self.x, self.y+1),
                                   Cell(self.x-1, self.y-1), Cell(self.x-1, self.y),
                                   Cell(self.x-1, self.y+1)])

    def calc_neighbors_interior(self):
        """Calculate the neighbors of an interior cell"""
        # Cells to this Cell's left and right
        self.neighbors.extend([Cell(self.x, self.y-1), Cell(self.x, self.y+1)])

        # Cells in the row above this Cell
        self.neighbors.extend([Cell(self.x-1, self.y), Cell(self.x-1, self.y-1),
                          Cell(self.x-1, self.y+1)])

        # Cells in the row below this Cell
        self.neighbors.extend([Cell(self.x+1, self.y), Cell(self.x+1, self.y-1),
                          Cell(self.x+1, self.y+1)])
        
    def print_neighbors(self):
        """Print the coordinates of all of this Cell's neighbor cells"""
        print("This Cell: %s" % str(self.coordinates))
        location = self.is_corner()
        print("Is a corner? %s" % str(location))
        location = self.is_edge()
        print("Is an edge? %s" % str(location)) 
        for i in range(len(self.neighbors)):
            print(str(self.neighbors[i].coordinates))
    
    def is_corner(self):
        """Return True if this Cell is in a corner and False otherwise"""
        if self.x == 0:
            if self.y == 0:
                return 'tl'
            elif self.y == self.columns - 1:
                return 'tr'
            else:
                return False
        elif self.x == self.rows - 1:
            if self.y == 0:
                return 'bl'
            elif self.y == self.columns - 1:
                return 'br'
            else:
                return False
        else:
            return False

    def is_edge(self):
        """Return True if this Cell is on an edge and False otherwise"""
        if self.x > 0 and self.x < self.rows - 1:
            if self.y == 0:
                return 'le'
            elif self.y == self.columns - 1:
                return 're'
            else:
                return False
        elif self.x == 0:
            if self.y > 0 and self.y < self.columns - 1:
                return 'te'
            else:
                return False
        elif self.x == self.rows - 1:
            if self.y > 0 and self.y < self.columns - 1:
                return 'be'
            else:
                return False
        else:
            return False
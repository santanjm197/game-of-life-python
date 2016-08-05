#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     			     #         	
# Project 1: Conway's Game of Life 				     			     #     
# Class: Cell                                                        #
# Created On: 8/1/2016             				                     #
#--------------------------------------------------------------------#

from tkinter import *

class Cell:
    """A cell which will know its coordinates as well as well as its
       current state (alive or dead)"""
        
    def __init__(self, x, y, rows=0, columns=0, window=None):
        """Construct a Cell with coordinates and the size of the world"""
        # The coordinate for this cell in the world
        self.x = x
        self.y = y
        self.coordinates = (x, y)

        # The number of rows and columns in the game world
        self.rows = rows
        self.columns = columns
        
        # The window that this Cell's canvas will be attached to
        self.window = window

        # The current state for this cell (0 = dead, 1 = alive)
        self.state = 0
        
        # Create a list of all of this cell's neighbors based on its coordinates
        if self.rows != 0 and self.columns != 0:
            self.find_neighbors()
            
            # Create this Cell's canvas and place it in its parent window in
            # a grid; its row and column will be simply its x and y coordinates
            self.canvas = Canvas(self.window, height=50, width=50,
                                 bg='blue', relief=RIDGE)
            self.canvas.grid(row=self.x, column=self.y)

    #-------------------------#
    #                         #
    #     Update Methods      #
    #                         #
    #-------------------------#
    
    def update_state(self, update):
        """Updates the current board configuration"""
        # Update the states of this Cell's neighbors based on the new world setup
        for coords in self.neighbors.keys():
            self.neighbors[coords] = update[coords]
        
        # Use this new information to decide how to change on the next cycle
        self.check_rules()
        
        # Change the color of this cell on the board:
        # Blue = dead, Red = alive
        if self.state == 0:
            self.canvas.config(bg='blue')
        else:
            self.canvas.config(bg='red')
            
        
        # Now return this Cell's (possibly) changed state
        return self.state
    
    def check_rules(self):
        """Checks which rules of the game apply to this cell on this frame
           and then updates its state accordingly"""
           
        # Count living neighbors
        alive = 0
        for neighbor in dict.keys(self.neighbors):
            if self.neighbors[neighbor] == 1:
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
        self.neighbors = {}
        
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
        # top-left corner
        if location == 'tl':
            self.neighbors[(self.x, self.y+1)] = 0
            self.neighbors[(self.x+1, self.y)] = 0
            self.neighbors[(self.x+1, self.y+1)] = 0
        # top-right corner
        elif location == 'tr':
            self.neighbors[(self.x, self.y-1)] = 0
            self.neighbors[(self.x+1, self.y)] = 0
            self.neighbors[(self.x+1, self.y-1)] = 0
        # bottom-left corner
        elif location == 'bl':
            self.neighbors[(self.x-1, self.y)] = 0
            self.neighbors[(self.x-1, self.y+1)] = 0
            self.neighbors[(self.x, self.y+1)] = 0
        # bottom-left corner
        else:
            self.neighbors[(self.x-1, self.y)] = 0
            self.neighbors[(self.x-1, self.y-1)] = 0
            self.neighbors[(self.x, self.y-1)] = 0

    def calc_neighbors_edge(self, location):
        """Calculate the neighbors of an edge cell"""
        # left edge
        if location == 'le':
            self.neighbors[(self.x-1, self.y)] = 0
            self.neighbors[(self.x-1, self.y+1)] = 0
            self.neighbors[(self.x, self.y+1)] = 0
            self.neighbors[(self.x+1, self.y)] = 0
            self.neighbors[(self.x+1, self.y+1)] = 0
        # right edge
        elif location == 're':
            self.neighbors[(self.x-1, self.y)] = 0
            self.neighbors[(self.x-1, self.y-1)] = 0
            self.neighbors[(self.x, self.y-1)] = 0
            self.neighbors[(self.x+1, self.y)] = 0
            self.neighbors[(self.x+1, self.y-1)] = 0
        # top edge
        elif location == 'te':
            self.neighbors[(self.x, self.y-1)] = 0
            self.neighbors[(self.x, self.y+1)] = 0
            self.neighbors[(self.x+1, self.y-1)] = 0
            self.neighbors[(self.x+1, self.y)] = 0
            self.neighbors[(self.x+1, self.y+1)] = 0
        # bottom edge
        else:
            self.neighbors[(self.x, self.y-1)] = 0
            self.neighbors[(self.x, self.y+1)] = 0
            self.neighbors[(self.x-1, self.y-1)] = 0
            self.neighbors[(self.x-1, self.y)] = 0
            self.neighbors[(self.x-1, self.y+1)] = 0

    def calc_neighbors_interior(self):
        """Calculate the neighbors of an interior cell"""
        # Cells to this Cell's left and right
        self.neighbors[(self.x, self.y-1)] = 0
        self.neighbors[(self.x, self.y+1)] = 0

        # Cells in the row above this Cell
        self.neighbors[(self.x-1, self.y)] = 0
        self.neighbors[(self.x-1, self.y-1)] = 0
        self.neighbors[(self.x-1, self.y+1)] = 0

        # Cells in the row below this Cell
        self.neighbors[(self.x+1, self.y)] = 0
        self.neighbors[(self.x+1, self.y-1)] = 0
        self.neighbors[(self.x+1, self.y+1)] = 0
    
    def is_corner(self):
        """Return True if this Cell is in a corner and False otherwise"""
        if self.x == 0:
            if self.y == 0:
                return 'tl' # top-left corner
            elif self.y == self.columns - 1:
                return 'tr' # top-right corner
            else:
                return False
        elif self.x == self.rows - 1:
            if self.y == 0:
                return 'bl' # bottom-left corner
            elif self.y == self.columns - 1:
                return 'br' # bottom-right corner
            else:
                return False
        else:
            return False

    def is_edge(self):
        """Return True if this Cell is on an edge and False otherwise"""
        if self.x > 0 and self.x < self.rows - 1:
            if self.y == 0:
                return 'le' # left edge
            elif self.y == self.columns - 1:
                return 're' # right edge
            else:
                return False
        elif self.x == 0:
            if self.y > 0 and self.y < self.columns - 1:
                return 'te' # top edge
            else:
                return False
        elif self.x == self.rows - 1:
            if self.y > 0 and self.y < self.columns - 1:
                return 'be' # bottom edge
            else:
                return False
        else:
            return False
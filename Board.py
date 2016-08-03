#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     			     #             	
# Project 1: Conway's Game of Life 				                     #		          
# Class: Board					   		                             #
# Created On: 8/1/2016             				                     #			              
#--------------------------------------------------------------------#

from Cell import Cell
from time import sleep

class Board:
    """The board on which the game will be played, controls how fast the steps are,
       the starting seed for the board and the rules of the game"""
    
    def __init__(self):
        """Default constructor for the Board class, creates a 10x10 board"""
        # Set the height of width of the board
        self.rows = 4
        self.columns = 4

        # Construct the game world
        self.construct_world()


    def construct_world(self):
        """Construct and return the game world based on a given height and width"""
        # Initialize the world with the right number of rows
        self.world = [0] * self.rows

        for i in range(self.rows):
            # Initialize each row with the right number of columns
            self.world[i] = [0] * self.columns
            for j in range(self.columns):
                self.world[i][j] = Cell(i, j, self.rows, self.columns)
            

    def print_world(self):
        """Prints the current world configuration"""
        for row in self.world:
            for cell in row:
                print(cell.state, end=' ')
            print()

    def print_cells(self):
        """Test method to print some cells' neighbor coordinates"""
        self.world[1][1].print_neighbors()
        print()
        self.world[1][2].print_neighbors()
        print()
        self.world[2][1].print_neighbors()
        print()
        self.world[2][2].print_neighbors()

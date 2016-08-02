#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     #			              	
# Project 1: Conway's Game of Life 				     #		          
# Class: Board					   		     #
# Created On: 8/1/2016             				     #			              
# Description: The board on which the game will be played,           #
#              controls how fast the steps are, the starting         #
#	       seed for the board and the rules of the game          #
#--------------------------------------------------------------------#

from Cell import Cell

class Board:

    def __init__(self):
        """Default constructor for the Board class, creates a 10x10 board"""
        # Set the height of width of the board
        self.rows = 10
        self.columns = 10

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
                self.world[i][j] = Cell(i, j)
            

    def print_world(self):
        """Prints the current world configuration"""
        for row in self.world:
            for cell in row:
                print(cell.state, end=' ')
            print()

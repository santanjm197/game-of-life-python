#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     			     #             	
# Project 1: Conway's Game of Life 				                     #		          
# Class: Board					   		                             #
# Created On: 8/1/2016             				                     #			              
#--------------------------------------------------------------------#

from Cell import Cell
from time import sleep
from copy import deepcopy, copy

class Board:
    """The board on which the game will be played, controls how fast the steps are,
       the starting seed for the board and the rules of the game"""
    
    def __init__(self):
        """Default constructor for the Board class, creates a 10x10 board"""
        # Set the height of width of the board
        self.rows = 15
        self.columns = 15

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
            
        self.set_seed()
        
    def set_seed(self):
        """TO-DO Sets the starting seed for the world (which cells are alive)"""
        self.world[2][1].state = 1
        self.world[2][2].state = 1
        self.world[3][2].state = 1
        self.world[1][2].state = 1
        self.world[1][3].state = 1
        
        # Begin the simulation
        self.game_loop()
        
    def game_loop(self):
        """The main loop of the simulation"""
        for n in range(8):
            self.print_world()
            
            # Temp variable that will be altered
            temp_world = deepcopy(self.world)
            
            # Now we need to update each Cell with this new world configuration
            for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    temp_world[i][j].state = temp_world[i][j].update_state(self.world)
                
            self.world = deepcopy(temp_world)
        
        
        # Now we need to update each Cell with this new world configuration
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                temp_world[i][j].state = temp_world[i][j].update_state(self.world)
            


    def print_world(self):
        """Prints the current world configuration"""
        for row in self.world:
            for cell in row:
                print(cell.state, end=' ')
            print()
        print()
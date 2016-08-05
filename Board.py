#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     			     #             	
# Project 1: Conway's Game of Life 				                     #		          
# Class: Board					   		                             #
# Created On: 8/1/2016             				                     #			              
#--------------------------------------------------------------------#

from Board_GUI import Board_GUI
from Cell import Cell
from time import sleep
from copy import deepcopy, copy
from tkinter import *

class Board():
    """The board on which the game will be played, controls how fast the steps are,
       the starting seed for the board and the rules of the game"""
    
    def __init__(self):
        """Default constructor for the Board class, creates a 10x10 board"""
        # Set the height of width of the board
        self.rows = 10
        self.columns = 10 
        
        # Create the window on which the simulation will be displayed
        self.window = Board_GUI(Tk())
        self.window.grid()
        # CURRENTLY NOT WORKING (Sets the program to quit when the GUI
        # is closed)
        self.window.master.protocol("WM_DELETE_WINDOW", quit)
        
        # Construct the game world
        self.construct_world()


    #-------------------------------------#
    #                                     #
    #     World Construction Methods      #
    #                                     #
    #-------------------------------------#

    def construct_world(self):
        """Construct and return the game world based on a given height and width"""
        # Initialize the world with the right number of rows
        self.world = [0] * self.rows

        for i in range(self.rows):
            # Initialize each row with the right number of columns
            self.world[i] = [0] * self.columns
            for j in range(self.columns):
                # Add Cells to at each position in the row
                self.world[i][j] = Cell(i, j, self.rows, self.columns, self.window)
            
        # Set the starting seed for the simulation
        self.set_seed()
        
    def set_seed(self):
        """TO-DO Sets the starting seed for the world (which cells are alive)"""
        # This is a 'glider' pattern at the moment
        self.world[0][1].state = 1
        self.world[0][3].state = 1
        self.world[1][2].state = 1
        self.world[1][3].state = 1
        self.world[2][2].state = 1
        
        # Begin the simulation
        self.game_loop()
        
        
    #-----------------------------#
    #                             #
    #     Simulation Methods      #
    #                             #
    #-----------------------------#
    
    def game_loop(self):
        """The main loop of the simulation"""
        while True:
            # Get a map of every Cell's coordinates with its current state
            cell_states = self.get_states()
            
            # Now we need to update each Cell with this new world configuration
            for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    self.world[i][j].state = self.world[i][j].update_state(cell_states)
                
            # Update the GUI with the new world state
            self.window.update()
            
            # Have the game sleep just briefly so we can actually see
            # what is happening
            sleep(0.5)


    def get_states(self):
        """Returns a Map of every Cell in the world's coordinates to its
           state in the current frame of the simulation"""
        cell_states = {}
        for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    cell_states[self.world[i][j].coordinates] = self.world[i][j].state
        
        return cell_states
#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     			     #             	
# Project 1: Conway's Game of Life 				                     #		          
# Class: Board					   		                             #
# Created On: 8/1/2016             				                     #			              
#--------------------------------------------------------------------#

from Board_GUI import Board_GUI
from Cell import Cell
from time import sleep
#from copy import deepcopy, copy
from tkinter import *
from time import time
import random
from math import floor

class Board():
    """The board on which the game will be played, controls how fast the steps are,
       the starting seed for the board and the rules of the game"""
    
    def __init__(self, rows, columns):
        """Default constructor for the Board class, creates a 10x10 board"""
        # Set the height of width of the board
        self.rows = rows
        self.columns = columns
        
        # The smallest number of cycles that any currently dead cell 
        # has been dead
        self.min_dead_cycles = 0
        
        # The smallest number of cycles that any currently living cell 
        # has been alive
        self.min_living_cycles = 0
              
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
        """Sets the starting seed for the world (which cells are alive)"""
        # This is a 'glider' pattern at the moment
        for i in range(500):
            x = random.randrange(0, len(self.world) - 1)
            y = random.randrange(0, len(self.world) - 1)
            self.world[x][y].state = 1
        
        
        # Begin the simulation
        self.game_loop()
        
    
    #-----------------------------#
    #                             #
    #     Simulation Methods      #
    #                             #
    #-----------------------------#
    
    def game_loop(self):
        """The main loop of the simulation"""
        # The starting time for the simulation (in ms)
        start_time = int(floor(time() * 1000))
        
        # What will be the ending time for the simulation (in ms) if it halts
        end_time = 0
        
        # Begin the loop
        while True:
            # Get a map of every Cell's coordinates with its current state
            cell_states = self.get_states()
            
            # Now we need to update each Cell with this new world configuration
            for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    self.world[i][j].state = self.world[i][j].update_state(cell_states)
                
            # Update the GUI with the new world state
            self.window.update()
            
            # Check if the simulation has reached a stopping point
            # That is, all cells have been either alive or dead for an
            # extended period of time.  If so, terminate the simulation
            if self.world_stopped():
                end_time = int(floor(time() * 1000))
                break
            
            # Have the game sleep just briefly so we can actually see
            # what is happening
            sleep(0.1)
        
        # The total run time for the simulation from start to halt
        run_time = end_time - start_time
        
        print("The simulation has halted in: ", str(run_time), "ms")
        exit()

    def get_states(self):
        """Returns a Map of every Cell in the world's coordinates to its
           state in the current frame of the simulation"""
        cell_states = {}
        for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    cell_states[self.world[i][j].coordinates] = self.world[i][j].state
        
        return cell_states
    
    def world_stopped(self):
        """Returns True if all cells in the world have been dead/alive for
           an extended period of time (i.e. the simulation has stopped)"""
        # Will stay true if all currently dead cells have been dead at least
        # 25 cycles
        dead_threshold = True
        
        # Will stay true if all currently living cells have been alive at
        # least 20 cycle
        living_threshold = True
        
        for i in range(len(self.world)):
                for j in range(len(self.world[i])):
                    # The currently examined cell
                    curr = self.world[i][j]
                    
                    # Has this cell been dead for less than 25 cycles?
                    # Then clearly the simulation hasn't come to a stop yet
                    if curr.state == 0 and curr.dead_cycles < 25:
                        dead_threshold = False
                    # Otherwise, has this cell been alive for less than 20 cycles?
                    # Then clearly the simulation hasn't come to a stop yet
                    elif curr.state == 1 and curr.living_cycles < 20:
                        living_threshold = False
                        
        # If both the living and dead thresholds are still true, then we
        # know that the simulation has settled to a stop and so we can terminate
        if dead_threshold and living_threshold:
            return True
        else:
            return False
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
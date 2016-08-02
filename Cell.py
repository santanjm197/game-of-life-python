#--------------------------------------------------------------------#
# Author: Joseph Santantasio       				     #			              	
# Project 1: Conway's Game of Life 				     #			          
# Class: Cell					   		     #					                          
# Created On: 8/1/2016             				     #			              
# Description: A cell which will know its coordinates as well        #
#              as well as its current state (alive or dead)          #
#--------------------------------------------------------------------#

class Cell:

    def __init__(self):
        """Default constructor for the Cell class"""
        
        # The coordinate for this cell in world
        self.coordinates = (0, 0)
        
        # The current state for this cell (0 = dead, 1 = alive)
        self.state = 0
        
    def __init__(self, x, y):
        """Constructor which takes a x and a y coordinate"""
        
        self.coordinates = (x, y)
        
        self.state = 0
        
        # Create a list of all of this cell's neighbors based on its coordinates
        self.find_neighbors()
        
    def find_neighbors(self):
        """TO-DO Create a list of the neighbors of this cell"""
        

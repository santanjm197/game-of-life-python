#-------------------------------------------------------------#
# Author: Joseph Santantasio       							  #	
# Project 1: Conway's Game of Life 							  #
# Class: Board					   							  #
# Created On: 8/1/2016             							  #
# Description: The board on which the game will be played,    #
#              controls how fast the steps are, the starting  #
#			   seed for the board and the rules of the game   #
#-------------------------------------------------------------#

class Board:

	def __init__(self):
		"""Default constructor for the Board class, creates a 10x10 board"""

		# Set the height of width of the board
		self.rows = 10
		self.columns = 10

		# Construct the game world
		self.world = self.construct_world()


	def construct_world(self):
		"""Construct and return the game world based on a given height and width"""

		return [([0] * self.rows)] * self.columns

	def print_world(self):
		"""TO-DO Prints the board in its current configuration"""



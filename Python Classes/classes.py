#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:20:33 2022

@author: abhay
"""

# defining a class

class CellDemo:
    pass         # creating an empty class
    
cell_1 = CellDemo()     # instance 1
cell_2 = CellDemo()     # instance 2

'''
    Both cell_1 and cell_2 are different
    entities and of type object
'''

print(cell_1)
print(cell_2)

#=================================#

# setting properties

cell_1.name = "Cell One"
cell_1.x = 0
cell_1.y = 0

cell_2.name = "Cell Two"
cell_2.x = 4
cell_2.y = 8

#========================================#

# Populating classes
import math

class Cell:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def cell_distance(self, other_cell):
        distance = math.sqrt((self.x - other_cell.x)**2 + (self.y - other_cell.y)**2)
        
        
cell1 = Cell("Cell One", 0, 0)
cell2 = Cell("Cell Two", 5, 10)

print(cell1.name)
    
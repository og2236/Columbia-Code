# -----------------------------------------------------------------------------
# EPIDEMI MAP
#
# by | Oskar Garcia OG2236 |
# Columbia University | ENGIE1006 | Spring 2019
# Take-Home Project4 – V.1.0
#
# -----------------------------------------------------------------------------

# -- Imports
import random

import math
from matplotlib import pyplot as plt
import numpy as np


# -- Sample Code & Pre-Defined Functions
def image_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3))
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 1.0
            # purple pixels
            # set 3 color components 
            img[x+50, y+50,:] = (.5,.0,.5)
            # green pixels
            img[x+100,y+100,green] = 1.0
    plt.imshow(img)

def normpdf(x, mean, sd):
    """
    Return the value of the normal distribution 
    with the specified mean and standard deviation (sd) at
    position x.
    You do not have to understand how this function works exactly. 
    """
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def pdeath(x, mean, sd):
    start = x-0.5
    end = x+0.5
    step =0.01    
    integral = 0.0
    while start<=end:
        integral += step * (normpdf(start,mean,sd) + normpdf(start+step,mean,sd)) / 2
        start += step            
    return integral    
    

#
# -- Global Infection Variables -----------------------------------------------
    
recovery_time = 7 # recovery time in time-steps
virality = 0.9    # probability that a neighbor cell is infected in 
                  # each time step                                                  

# -----------------------------------------------------------------------------
#
# -- Cell Class ---------------------------------------------------------------
class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y 
        self.state = 'S'
        self.time = 0
                
    #
    # -- Infect Method
    def infect(self):
        self.time = 0
        self.state = 'I'
        
    #
    # -- Recover Method --> Converts an infrected cell into a healthy one
    def recover(self):
        self.time = 0
        self.state = 'S'
        
    #
    # -- Die Method --> Converts an infected cell into dead or 'resistant' 
    def die(self):
        self.time = 0
        self.state = 'R'
    
    
    def process(self, adjacent_cells):
        
        global virality
        global recovery_time
        
        # -- Checks for infection, recovers if sufficient time has elapsed
        if self.state == 'I' and self.time == recovery_time:
            
            self.recover()
            
        
        # -- Checks for infection, kills cell according to pdeath  
        elif self.state == 'I' and random.random() <= pdeath(self.time, 5, 0.5):
            
            self.die()
        
        # -- Checks for infection, and infects neighboring cells
        elif self.state == 'I' and 0 < self.time:
            
            for cell in adjacent_cells:
                
                if cell.state == 'S' and random.random() <= virality:
                    
                    cell.infect()
                    
            self.time += 1
            
        else:
            
            self.time += 1
            
            
# -----------------------------------------------------------------------------
#
# -- Map Class ----------------------------------------------------------------
class Map(object):
    
    
    def __init__(self):
        self.height = 150
        self.width = 150
        self.cells = {}
        
        #
        # -- Encodes the colors within a dictionary
        self.colors = {'S':(0.0, 1.0, 0.0), 'R':(0.5, 0.5, 0.5),
                       'I':(1.0, 0.0, 0.0)}
        
        
    #
    # -- Add Cell Method
    def add_cell(self, cell):
        self.cells[cell.x, cell.y] = cell
        
        
    #
    # -- Display Method
    def display(self):
        
        img = np.zeros((150,150,3))
        
        for coordinate in self.cells:
            
            temp_color = self.cells[coordinate].state
            
            img[coordinate[0], coordinate[1],:] = self.colors[temp_color]
        
        plt.imshow(img)
        
    
    #
    # -- Adjacet Cells Method
    def adjacent_cells(self, x, y):
        
        adjacent = []
        
        north = (x + 1, y)
        
        if north in self.cells:
            
            adjacent.append(self.cells[north])
        
        south = (x - 1, y)
        
        if south in self.cells:
            
            adjacent.append(self.cells[south])
        
        east = (x, y + 1)
            
        if east in self.cells:
            
            adjacent.append(self.cells[east])
            
        west = (x, y - 1)
            
        if west in self.cells:
            
            adjacent.append(self.cells[west])
        
        return adjacent
    
    
    def time_step(self):
        
        for coord in self.cells:
            
            neighbors = self.adjacent_cells(coord[0], coord[1])
            
            self.cells[coord].process(neighbors)
        
        self.display()

# -----------------------------------------------------------------------------
        
# -- Read Map Function---------------------------------------------------------
def read_map(filename):
    
    mappy = Map()
    
    file_in = open(filename, 'r')
    
    for line in file_in:
       
        xy_pair = line.split(',')
        
        x_val = int(xy_pair[0])
        y_val = int(xy_pair[1])

        new_cell = Cell(x_val, y_val)
        
        mappy.add_cell(new_cell)
        
    return mappy

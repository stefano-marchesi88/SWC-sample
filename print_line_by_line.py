import numpy as np

def readasnumpy(filename):
   """
   This function takes a textfile and returns a numpy array that is the transpose
   """
   arr1 = np.loadtxt(filename)
   return arr1.T

def readlinebyline(filename):
    """
    This function reads a file line by line and gives on screen the result
    """

    f = open(filename,'r')
    for line in f:
#        x,y = [int(i) for i in line.split]
        print line
    f.close()
    
#readlinebyline('data1.txt')
def printtonewtext(filename):
    """
    This function takes a textfile and prints in a new textfile the square of the second column
    """
    f = open (filename,'r')
    g = open ('data3.txt', 'w')
    for line in f:
        print >> g, int(line.split()[1])**2
    g.close()
    f.close()

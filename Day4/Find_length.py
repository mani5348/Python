#WAP to create a function find_length (integer,intger) input is two integer for a and c line return the exact length of line b
import math
def find_length(height,base):
    hyp1=((height*height)+(base*base))
    print(math.sqrt(hyp1))
height=int(input("enter the height of trinangle: "))
base=int(input("enter the base of trinangle:"))
find_length(height,base)
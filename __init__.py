import sys
from world.use_turtle import use_turtle

args = sys.argv
is_turtle = 'turtle' in args

def using_turtle():
    if not is_turtle:
        return False, None
    
    return is_turtle, use_turtle()
        
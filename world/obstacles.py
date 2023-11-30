import random

def get_obstacles():
    number = random.randint(1, 10)
    myobstacles = []
    if number != 0:
        for i in range(number):
            x = random.randint(-100, 100)
            y = random.randint(-200, 200)
            myobstacles.append((x,y))
        return myobstacles    
    return []

def is_position_blocked(obstacles, position_x, position_y):
    if len(obstacles) != 0:
        print(position_x,position_y)
        for positions in obstacles:
            if positions[0] <= position_x <= positions[0] + 4 or positions[1] <= position_y <= positions[1] + 4:
                return True
        return False
    return False

def is_path_blocked(obstacles, x1, y1, x2, y2):
    if x1 != x2 and y1 != y2:
        raise ValueError("Robot can only move in right angles")
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if is_position_blocked(obstacles, x1, y):
                return True
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if is_position_blocked(obstacles, x, y1):
                print_obstacles(obstacles)
                return True    
    return False
            
def print_obstacles(obstacles):
    print(
        f"- At position {obstacles[0]},{obstacles[1]} (to {obstacles[0]+ 4},{obstacles[1]+ 4})")
    
if __name__ == "__main__":
    print("Here")
    obstacles = get_obstacles()
    #print(obstacles)
    is_path_blocked(obstacles, 1, 1, 1, 1)
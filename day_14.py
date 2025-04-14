# Day 14 - Robots 
import re 
import numpy as np

def parse_input(input_file_path):
    f = open(input_file_path, 'r')
    lines = [re.split('p=| v=|,|\n', l) for l in f.readlines()] # Split at p= and v= and , 
    lines = [list(filter(None, l)) for l in lines]# Remove empty entries from list. First two numbers = position, last two = velocity
    return lines
    
def locations_to_x_y(locations, grid_dimensions):
    # Turn the given locations into traditional x and y coordinates p0,0 = top left 
    # keep x cordinate the same, but invert y coordinate e,g, height - y
    for y in locations:
        y[1] = grid_dimensions[1] - int(y[1]) -1 # The -1 is for 0 base indexing
    return locations

def location_after_steps(input_locations_and_velocities, number_steps):
    # For each line of input_locations_and_velocities, add veloctiy * steps the location
    # Element 1 + element 3 * number_steps 
    # Element 2 + element 4 * number_steps
    # Return a list of the new positions
    new_positions = []
    for line in input_locations_and_velocities:
        new_x = int(line[0]) + int(line[2]) * number_steps
        new_y = int(line[1]) + int(line[3]) * number_steps
        new_positions.append((new_x, new_y))
    return new_positions
    
def map_locations_back_to_grid(new_positions, grid_dimensions):
    # As the grid wraps around, we need to map the new positions back to the grid.
    # Divide x by grid width and get the remainder as the new x position
    # Divide y by grid height and get the remainder as the new y position
    original_grid = []
    for robot in new_positions:
        x = robot[0] % grid_dimensions[0]
        y = robot[1] % grid_dimensions[1]
        original_grid.append((x, y))
    return original_grid

def calculate_saftey_factor(original_grid, width, height):
    mid_line_width = (width // 2)
    mid_line_height = (height // 2)
    
    saftey_factor = 0 
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in original_grid:
        rx = robot[0]
        ry = robot[1]
        if rx < mid_line_width and ry < mid_line_height:
            q1 += 1
        if rx < mid_line_width and ry > mid_line_height:
            q2 += 1
        if rx > mid_line_width and ry < mid_line_height:
            q3 += 1
        if rx > mid_line_width and ry > mid_line_height:
            q4 += 1
    return q1 * q4 * q2 * q3
    

def test_part_1():
    test_input = ['p=0,4 v=3,-3', 
                'p=6,3 v=-1,-3', 
                'p=10,3 v=-1,2', 
                'p=2,0 v=2,-1', 
                'p=0,0 v=1,3', 
                'p=3,0 v=-2,-2', 
                'p=7,6 v=-1,-3', 
                'p=3,0 v=-1,-2', 
                'p=9,3 v=2,3', 
                'p=7,3 v=-1,2', 
                'p=2,4 v=2,-3', 
                'p=9,5 v=-3,-3']
    lines = [re.split('p=| v=|,', l) for l in test_input] # Split at anything thats not a list. 
    lines = [list(filter(None, l)) for l in lines]
    print('Input:')
    print(lines)
    new_positions = locations_to_x_y(lines, (11, 7))
    print('Adjusted y')
    print(new_positions)
    new_positions= location_after_steps(new_positions, 1)
    original_grid = map_locations_back_to_grid(new_positions, (11, 7))
    print('Original grid:')
    print(original_grid)
    safety_factor = calculate_saftey_factor(original_grid, 11, 7)
    print(f"Safety factor: {safety_factor}")



if __name__ == "__main__":
    test_part_1()

    file_path_input = '/Users/mahony/Downloads/aoc_2024_day_14.txt'
    lines = parse_input(file_path_input)
    print(lines[0])
    new_positions = location_after_steps(lines, 100)
    print(new_positions[0])
    original_grid = map_locations_back_to_grid(new_positions, (101, 103))
    print(original_grid[0])
    print(calculate_saftey_factor(original_grid, width=101, height=103))

# Search Topological Map
# Depth First Search Algorithm 
# Find the number of 9's that can be reached from each 0

import numpy as np 

def parse_input(input_file_path):
    """
    Parse the input into a dictionary, key = tuple of the x and y co-ordinate, value = the number e.g. the 'height' on the map
    e.g. {(0, 0) : 5 } at the top left of the map the height is 5
    """
    puzzle_map = {}
    with open(input_file_path, 'r') as f:
        for row_index, row in enumerate(f):
            line = row.strip()
            for character_index, character in enumerate(line):
                puzzle_map[(row_index, character_index)] = int(character)
    return puzzle_map


def start_locations(puzzel_map):
    """
    Returns list of tuples of start locations (x, y )
    """
    starts = []
    for key, value in puzzel_map.items():
        if value == 0:
            starts.append(key)
    return starts


def build_graph(puzzel_map):
    """
    Input: puzzel_map = dict of the puzzle input, keys = (x, y) value = value at that coordinate
    Retuns: graph = dict where the key is each node and the values are each neighboring nodes. 
    """
    graph = {}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for (x, y) in puzzel_map.keys():
        neighbours = []
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in puzzel_map:  # Check if the neighbor exists in the grid - solves edge cases
                neighbours.append(neighbor)
        graph[(x, y)] = neighbours
    return graph    


def count_trails(puzzel_map, puzzel_graph, start_location):
    """
    Uses a recursive depth first search to count the number of 9's that can be reached from each 0

    Input: 
        puzzel_map = tuple of the x and y co-ordinate, value = the height at that location
        puzzel_graph = graph = dict where the key is each node and the values are each neighboring nodes. 
        start_location = list of tuples of start locations (x, y )
    Output: 
        Number of 9's that can be reached from a 0, e.g. how many "hiking trails" there are from that start point 
    """
     # e.g. the set of availble 9's you can get to. 

    def depth_first_search(node, visited, trail_ends):
        if node in visited:
            return 
        visited.add(node) # Add curent node to the list of those visited
        if puzzel_map[node] == 9: 
            trail_ends.add(node) # if node = 9 add it to the set of possible 9's you can get to e.g. trail_ends
        for neighbor in puzzel_graph[node]: # Go through all neighbors at that node 
            if neighbor not in visited and puzzel_map[neighbor] == puzzel_map[node] + 1: # if the neighbour hasnt been visited and is 1 more then proceed
                depth_first_search(neighbor, visited, trail_ends) # Recursively perform this function
    
    number_trails = 0
    for start in start_location:
        # Reset the locations visited and the number of trail ends for each new start location. 
        visited = set()
        trail_ends = set() 
        depth_first_search(start, visited, trail_ends)
        number_trails += len(trail_ends)
    return number_trails












def test_datasets():
    test_input = [
        '89010123',
        '78121874',
        '87430965',
        '96549874',
        '45678903',
        '32019012',
        '01329801',
        '10456732']
    puzzle_map = {}
    for row_index, row in enumerate(test_input):
        line = row.strip()
        for character_index, character in enumerate(line):
            puzzle_map[(row_index, character_index)] = int(character)
    start = start_locations(puzzle_map)
    puzzle_graph = build_graph(puzzle_map)
    count = count_trails(puzzle_map, puzzle_graph, start)
    return puzzle_map, start, puzzle_graph, count

def run_tests_part_1():
    puzzle_map, start, puzzle_graph, count = test_datasets()
    print(f'Test {count}')
    if count == 36:
        return True 
    
def run_test_part_2():
    puzzle_map, start, puzzle_graph, count = test_datasets()
    pass


def main():
    puzzle_input_path = '/Users/mahony/Downloads/aoc_2024_day_10.txt'
    puzzle_map = parse_input(puzzle_input_path)
    start = start_locations(puzzle_map)
    puzzle_graph = build_graph(puzzle_map)
    count = count_trails(puzzle_map, puzzle_graph, start)
    print(f'Part 1 = {count}')

if __name__ == "__main__":
    if run_tests_part_1():
        main()
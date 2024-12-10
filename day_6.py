def run_tests_part_1():
    test_input_map =["....#.....",
                     ".........#",
                     "..........",
                     "..#.......",
                     ".......#..",
                     "..........",
                     ".#..^.....",
                     "........#.",
                     "#.........",
                     "......#..."]
    test_locations_visited_map = ['....#.....',
                                  '....XXXXX#',
                                  '....X...X.',
                                  '..#.X...X.',
                                  '..XXXXX#X.',
                                  '..X.X.X.X.',
                                  '.#XXXXXXX.',
                                  '.XXXXXXX#.',
                                  '#XXXXXXX..',
                                  '......#X..']
    test_locations_visited_map = [list(row) for row in test_locations_visited_map]
    test_output_result = 41

    locations_visited = guard_traverse_map(test_input_map)
    count = count_locations(locations_visited)

    return test_output_result==count

    
def parse_input_data(input_file_path):
    """
    Output: list of strings e.g. ['....#.....', '.........#']
    """
    with open(input_file_path) as f:
        puzzle_input = f.read().split()
    
    print(f"The puzzle input is a list of length {len(puzzle_input)} which contain {len(puzzle_input[0])} positions")

    return puzzle_input

def find_guard(map):
    """
    Input: Map, this is the puzzle input e.g a list of strings with the positions
    Ouput: 
        Tuple of the 'guard' position as a tuple e.g. the row and column 'n' is at  and the 
        Guard shape, as the guard can be pointing four ways 
    """
    guard_shapes = ['<', '>', '^', 'v']
    for (row_num, row) in enumerate(map):
        for (col_num, position) in enumerate(row):
            if position in guard_shapes:
                return ((row_num, col_num), position)


def get_next_step(row_num, col_num, position, puzzle_map):
    # If the row or the column number are 130 / the max, the guard has reached the end of the map 
    # return the row and column index of the next step 
    if row_num == len(puzzle_map) or col_num == len(puzzle_map):
        print(f'The guard is leaving the map! as the row = {row_num} column = {col_num} {len(puzzle_map)}')
        return None, None, None 
    else:
        if position == '^':
            new_row, new_col = (row_num-1 ,col_num)
        elif position == '>':
            new_row, new_col = (row_num, col_num+1)
        elif position == 'v':
            new_row, new_col = (row_num+1, col_num)
        else: # Position must be <
            new_row, new_col = (row_num, col_num-1)
        if new_row == len(puzzle_map) or new_col == len(puzzle_map):
            print(f'The guard is leaving the map! as the row = {row_num} column = {col_num} {len(puzzle_map)}')
            return None, None, None 
        else:
            next_step = puzzle_map[new_row][new_col]
            if next_step == '#':
            # hit blockage therefore must rotate 90 degrees 
                if position == '^':
                    new_position = '>'
                elif position == '>':
                    new_position = 'v'
                elif position == 'v':
                    new_position = '<'
                else:
                    new_position = '^'
                return get_next_step(row_num, col_num, new_position, puzzle_map)

            else:
                return new_row, new_col, position


def guard_traverse_map(puzzle_map):
    """
    This function copys the map to a new locations visited map, turning the places the guard has been to X 
    Once the get_next_step function breaks i.e. The guard is leaving the map, return the locations visited. 
    """
    # Starting positions
    ((row_num, col_num), position) = find_guard(puzzle_map)
    locations_visited = [list(row) for row in puzzle_map] # Deep copy 
    # change ^ to X on locations visited 
    locations_visited[row_num][col_num] = 'X'
    # Get the the next step and position 
    while True:
        new_row, new_col, position = get_next_step(row_num, col_num, position, puzzle_map)
        if new_row is None or new_col is None:
            # Now the guard has left the map so exit this while loop, but first update locations visited 
            locations_visited[row_num][col_num] = 'X'
            break
        # The guard hasn't left so update the positions and stay in while loop
        locations_visited[row_num][col_num] = 'X'
        row_num, col_num = new_row, new_col 
    return locations_visited


def count_locations(locations):
    counts = [row.count('X') for row in locations]
    print(counts)
    return sum(counts)


if __name__ == "__main__":
    if run_tests_part_1():
        print('Test passed')
        puzzle_input = parse_input_data('/Users/mahony/Downloads/aoc_2024_day_6.txt')
        print(count_locations(guard_traverse_map(puzzle_input)))
    

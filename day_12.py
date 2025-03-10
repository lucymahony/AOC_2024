# Calculate area and perimeter of given map 

def parse_input(input_file_path):
    f = open(input_file_path, 'r')
    lines = [l.strip() for l in f.readlines()]
    return lines


def test_part_1():
    test_map = ['RRRRIICCFF',
    'RRRRIICCCF',
    'VVRRRCCFFF',
    'VVRCCCJFFF',
    'VVVVCJJCFE',
    'VVIVCCJJEE',
    'VVIIICJJEE',
    'MIIIIIJJEE',
    'MIIISIJEEE',
    'MMMISSJEEE']
    price = calculate_price(test_map)
    print(f'Test part 1 = {price}')
    expected_price = 1930
    if price != expected_price:
        print(f'Error: expected {expected_price} but got {price}')
    else:
        print('Test part 1 passed')

def test_part_2():
    test_map = [
        'AAAAAA',
        'AAABBA'
        'AAABBA',
        'ABBAAA',
        'ABBAAA',
        'AAAAAA']
    price = calculate_price_2(test_map)
    print(f'Test part 2 = {price}')
    exepected_price = 368
    if price != exepected_price:
        print(f'Error: expected {exepected_price} but got {price}')
    else:
        print('Test part 2 passed')


def search(map_input, row, column, seen_locations):
    """
    Perform a depth-first search (DFS) to calculate the area and perimeter of a region.
        map_input is a list of lists of characters 
    current row / column of symbols
    seen_locations = locations that have been searched before so don't search again
    """
    stack = [(row, column)]
    current_symbol = map_input[row][column]
    area = 0
    perimeter = 0

    while stack:
        r, c = stack.pop()
        if (r, c) in seen_locations:
            continue

        seen_locations.update((r, c))
        area += 1

        # Check neighbors
        for direction_r, direction_c in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            neightbor_r, neightbor_c = r + direction_r, c + direction_c

            if 0 <= neightbor_r < len(map_input) and 0 <= neightbor_c < len(map_input[0]):
                if map_input[neightbor_r][neightbor_c] == current_symbol:
                    stack.append((neightbor_r, neightbor_c))
                else:
                    perimeter += 1
            else:
                # Out of bounds contributes to perimeter
                perimeter += 1

    return area, perimeter, seen_locations


def calculate_price(map_input):
    price = 0
    seen_locations = []
    # Symbol prince is empty dict
    symbol_price = {}
    for row in range(len(map_input)):
        for column in range(len(map_input[0])):
            if map_input[row][column] not in seen_locations:
                # If the symbol hasn't been searched before it wont be in seen_locations
                area, perimeter, seen_locations = search(map_input, row, column, seen_locations)
                # Check if the symbol is in the price list
                if map_input[row][column] not in symbol_price:
                    symbol_price[map_input[row][column]] = area * perimeter
                else:
                    current_price = symbol_price[map_input[row][column]]
                    new_price = current_price + (area * perimeter)
                    symbol_price[map_input[row][column]] = new_price
    # Now sum the prices of all symbols
    keys = symbol_price.keys()
    for key in keys:
        price += symbol_price[key]
    return price


# Part 2 - Counting corners
# As well as the area now need the number of sides which = the number of corners
# Move top left to bottom right and keep a tally of the number of corners
def search_2(map_input, row, column, seen_locations):
    """
    Perform a depth-first search (DFS) to calculate the area, perimeter, and number of corners of a region.
    
    - map_input: A list of lists of characters representing the map.
    - row, column: Starting position of the search.
    - seen_locations: List of already visited locations to prevent redundant searches.
    
    Returns:
        area (int): Total number of cells in the region.
        perimeter (int): Number of edge cells exposed to a different symbol or boundary.
        corners (int): Number of external corners in the region.
        seen_locations (list): Updated list of visited locations.
    """
    stack = [(row, column)]
    current_symbol = map_input[row][column]
    area = 0
    perimeter = 0
    corners = 0

    # Check the map to see if it contains the symbol *, if not padd the map with * to avoid out of bounds errors
    if '*' not in map_input:
        map_input = ['*' + row + '*' for row in map_input]
        map_input = ['*' * len(map_input[0])] + map_input + ['*' * len(map_input[0])]
    else: 
        print('Map already contains *!')

    while stack:
        r, c = stack.pop()
        if (r, c) in seen_locations:
            continue

        seen_locations.update((r, c))
        area += 1

        # if all or just one is different it is a corner
        #123
        #4X5
        #678
        one = map_input[r-1][c-1]
        two = map_input[r-1][c]
        three = map_input[r-1][c+1]
        four = map_input[r][c-1]
        five = map_input[r][c+1]
        six = map_input[r+1][c-1]
        seven = map_input[r+1][c]
        eight = map_input[r+1][c+1]
        #top_left_corner  - 4, 1, 2
        # convex
        if four != current_symbol and two != current_symbol and one != current_symbol:
            corners += 1
        # concave
        elif four == current_symbol and two == current_symbol and one != current_symbol:
            corners += 1
        # horizontal
        elif one == current_symbol and four != current_symbol and two != current_symbol:
            corners += 2
        # Now repeat for the other corners
        # top right corner - 2, 3, 5
        # convex
        if two != current_symbol and three != current_symbol and five != current_symbol:
            corners += 1
        # concave
        elif two == current_symbol and three == current_symbol and five != current_symbol:
            corners += 1
        # horizontal
        elif two == current_symbol and five != current_symbol and three != current_symbol:
            corners += 2
        # bottom left corner - 4, 6, 7
        # convex
        if four != current_symbol and six != current_symbol and seven != current_symbol:
            corners += 1
        # concave
        elif four == current_symbol and six == current_symbol and seven != current_symbol:
            corners += 1
        # horizontal
        elif four == current_symbol and seven != current_symbol and six != current_symbol:
            corners += 2
        # bottom right corner - 5, 7, 8
        # convex
        if five != current_symbol and seven != current_symbol and eight != current_symbol:
            corners += 1
        # concave
        elif five == current_symbol and seven == current_symbol and eight != current_symbol:
            corners += 1
        # horizontal
        elif five == current_symbol and eight != current_symbol and seven != current_symbol:
            corners += 2
            


    return area, corners, seen_locations



def calculate_price_2(map_input):
    price = 0
    seen_locations = set() 
    symbol_data = {}  # Store (total area, total corners) per symbol 
    # The 1's deal with the padding. 
    for row in range(1, len(map_input) -1):
        for column in range(1, len(map_input[0]) -1 ):
            if (row, column) not in seen_locations:
                # Start DFS search
                area, corners, new_seen = search_2(map_input, row, column, seen_locations)
                seen_locations.update(new_seen)  # Merge new seen locations

                symbol = map_input[row][column]
                
                # Accumulate area and corners
                if symbol not in symbol_data:
                    symbol_data[symbol] = (area, corners)
                else:
                    total_area, total_corners = symbol_data[symbol]
                    symbol_data[symbol] = (total_area + area, total_corners + corners)

    # Now compute the final price
    # Remove the * entries from the symbol_data
    symbol_data.pop('*', None)

    for symbol, (total_area, total_corners) in symbol_data.items():
        price += total_area * total_corners

    print(symbol_data)  # Debugging output
    return price



def main():
    #test_part_1()
    test_part_2()
    exit()
    puzzle_input = parse_input('/Users/mahony/Downloads/aoc_2024_day_12.txt')
    price = calculate_price(puzzle_input)
    print(f'Part 1 = {price}')
    price_2 = calculate_price_2(puzzle_input)
    print(f'Part 2 = {price_2}')
    
    
if __name__ == "__main__":
    
    main()
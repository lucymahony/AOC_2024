# Search in word search for all occurances of 'XMAS'

def run_test_part_1():
    test_data = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

    if find_xmas(test_data) == 18:
        print('Find x mas func works')
        return True
    else: 
        print(f'Error in find x mas func returns {find_xmas(test_data)}')
        return False


def run_test_part_2():
    test_data = ['.M.S......','..A..MSMS.','.M.S.MAA..','..A.ASMSM.','.M.S.M....','..........','S.S.S.S.S.','.A.A.A.A..','M.M.M.M.M.','..........']
    if find_mas_cross(test_data) == 9:
        print('Find mas cross works')
        return True
    else:
        print(f'Error in find_mas_cross func returns {find_mas_cross(test_data)}')


def find_xmas(word_search):
    """
    Part 1 - Get all the XMAS occurances in the cross word.
    Input: List of strings that make up the cross word
    Output: 
    """
    count = 0 
    for row_num, row in enumerate(word_search):
        for letter_num, letter in enumerate(row):
            if letter == 'X':
                #Search surroundings for 'MAS' 
                horizontal_forward = (0, 1) 
                horizontal_backward = (0, -1) 
                vertical_up = (-1, 0)
                vertical_down= (1, 0)
                diag_up_left= (-1, -1)
                diag_up_right= (-1, 1)
                diag_down_left= (1, -1)
                diag_down_right= (1, 1)
                directions = [horizontal_forward, horizontal_backward, vertical_up, vertical_down, diag_up_left, diag_up_right, diag_down_left, diag_down_right] 
                for direction in directions:
                    row_offset, col_offset = direction
                    try:
                        # Ensure indices are within bounds before accessing the elements
                        if all(0 <= (row_num + i * row_offset) < len(word_search) and 0 <= (letter_num + i * col_offset) < len(word_search[0]) for i in range(1, 4)):
                            diagonal_word = ''.join([word_search[(row_num + i * row_offset)][(letter_num + i * col_offset)] for i in range(1, 4)])
                            if diagonal_word == 'MAS':
                                count += 1
                    except IndexError:
                        # Indices go out of bounds
                        continue
    return count


def find_mas_cross(word_search):
    """
    Similar to find_xmas but the center of a match is A and 'MAS' or 'SAM' for both diagonals 

    The A can't be at row 0 or column 0 or the final row or column
    """
    count = 0 
    for row_num in range(1, (len(word_search)-1)):
        for letter_num in range(1, (len(word_search[row_num])-1)):
            letter = word_search[row_num][letter_num]
            if letter == 'A':
                try:
                    # Diag left 
                    diag_word_left = word_search[(row_num -1 )][(letter_num -1)] + word_search[(row_num +1 )][(letter_num +1)]
                    diag_word_right = word_search[(row_num + 1 )][(letter_num -1)] + word_search[(row_num -1 )][(letter_num +1)]

                    if diag_word_left in ['MS', 'SM'] and diag_word_right in ['MS', 'SM']:
                        print(diag_word_left, diag_word_right)
                        count += 1
                except IndexError:
                    continue
    return count


if __name__ == "__main__":
    with open('/Users/mahony/Downloads/aoc_2024_day_4.txt') as f:
        puzzle_input = f.read().split('\n') # List of strings where each element is a new line of input string e.g. ['MMMSXXMASM', 'MSAMXMSMSA']
    
    if run_test_part_1():
        # If tests pass try puzzle input data
        print(f'Solution to part 1 :{find_xmas(puzzle_input)}')
    
    if run_test_part_2():
        #pass
        print(f'Solution to part 2 :{find_mas_cross(puzzle_input)}')
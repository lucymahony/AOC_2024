import itertools
from tqdm import tqdm

def test_check_all_operations():
    test_dict = {
        190: [10, 19],
        3267: [81, 40, 27],
        83: [17, 5],
        156: [15, 6],
        7290: [6, 8, 6, 15],
        161011: [16, 10, 13],
        192: [17, 8, 14],
        21037: [9, 7, 18, 13],
        292: [11, 6, 16, 20],
    }
    
    assert check_all_operations(190, test_dict) == True, "Test case 1 failed"
    assert check_all_operations(3267, test_dict) == True, "Test case 2 failed"
    assert check_all_operations(292, test_dict) == True, "Test case 3 failed"
    assert check_all_operations(83, test_dict) == False, "Test case 4 failed"
    assert check_all_operations(156, test_dict) == False, "Test case 4 failed"
    assert check_all_operations(21037, test_dict) == False, "Test case 4 failed"
    

    print("All test cases passed!")


def parse_input(input_file_path):
    puzzel_dict = {}
    with open(input_file_path) as f:
        puzzel_input = f.read().split('\n')
        for line in puzzel_input:
            key, values = line.strip().split(':')
            values = [int(x) for x in values.split()]
            puzzel_dict[int(key)] = values
    return puzzel_dict

def check_all_operations(key, dict):
    """
    Input:
        key : int() e.g. 32584018
        dict: contains values that are lists of ints e.g. dict[32584018] = [19, 27, 548, 60, 7]
    Output:
        bool. if given all posible arangements of opereators +, * if any of them = the key
    """
    equation_numbs = dict[key]
    number_operators = len(equation_numbs) - 1
    all_arangements_operators = list(itertools.product(['*', "+"], repeat=number_operators))
    for operators in all_arangements_operators:
        for i in range(len(equation_numbs) - 1):
            if i == 0:
                expression = '' + str(equation_numbs[i]) + str(operators[i]) + str(equation_numbs[i+1])
            else:
                expression = '' +str(expression)  + str(operators[i]) + str(equation_numbs[i+1])
            expression = eval(expression) 
        if expression == key:
            return True
    return False # If the expression never == key then False will be returned 


def check_all_operations_part_two(key, dict):
    """
    Input:
        key : int() e.g. 32584018
        dict: contains values that are lists of ints e.g. dict[32584018] = [19, 27, 548, 60, 7]
    Output:
        bool. if given all posible arangements of opereators +, *, concat if any of them = the key
    """
    equation_numbs = dict[key]
    number_operators = len(equation_numbs) - 1
    all_arangements_operators = list(itertools.product(['*', "+", 'concat'], repeat=number_operators))
    for operators in all_arangements_operators:
        for i in range(len(equation_numbs) - 1):
            if i == 0:
                if operators[i] == 'concat':
                    expression = int(str(equation_numbs[i]) + str(equation_numbs[i+1]))
                else:
                    expression = '' + str(equation_numbs[i]) + str(operators[i]) + str(equation_numbs[i+1])
                    expression = eval(expression) 
            else:
                if operators[i] == 'concat':
                    expression = int(str(expression) + str(equation_numbs[i+1]))
                else:
                    expression = '' +str(expression)  + str(operators[i]) + str(equation_numbs[i+1])
                    expression = eval(expression) 
        if expression == key:
            return True
    return False # If the expression never == key then False will be returned 


def sum_correct_calibrations(dict):
    """
    For each key in the puzzel input dict, if check_all_operations =True for that sum the values. 
    Input:
        dict : Puzzle input formatted as a dict e.g. test_dict = {
        190: [10, 19],
        3267: [81, 40, 27]}
    Output: Int thats a sum of True keys from check_all_operations
    """
    sum = 0 
    keys_to_check = list(dict.keys())
    for key in keys_to_check:
        if check_all_operations(key, dict):
            sum += key
    return sum 


def sum_correct_calibrations_part_two(dict):
    sum = 0 
    keys_to_check = list(dict.keys())
    for key in tqdm(keys_to_check):
        if check_all_operations_part_two(key, dict):
            sum += key
    return sum 


def main():
    puzzle_input = parse_input('/Users/mahony/Downloads/aoc_2024_day_7.txt')
    test_check_all_operations()
    #print(f'Part 1 = {sum_correct_calibrations(puzzle_input)}')
    print(f'Part 2 = {sum_correct_calibrations_part_two(puzzle_input)}')


if __name__ == "__main__":
    main()
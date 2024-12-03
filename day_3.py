# Scan input file for correctly formated functions and perform them
import re 


def run_tests():
    example_input='xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    example_functions=['mul(2,4)', 'mul(5,5)', 'mul(11,8)', 'mul(8,5)']
    example_function_output=[8, 25, 88, 40]
    example_end_result=sum(example_function_output)

    if find_functions(example_input) == example_functions:
        print('find_functions works')
    else: 
        print('Error in find_functions')
    
    if perform_function(example_functions[0]) == 8:
        print('perform function works')
    else:
        print(f'Error {example_functions[0]}')
    if find_perform_and_sum(example_input) == example_end_result:
        print('find_perform_and_sum works')
    else: 
        print(f'Error {find_perform_and_sum(example_input)}')

    # Part 2
    example_input_disabler="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    if find_perform_and_sum(example_input_disabler, enabler_activated=True) == 48:
        print('Part 2 works')
    else:
        print(f'Error in Part 2 {find_perform_and_sum(example_input_disabler, enabler_activated=True)}')

def find_functions(string):
    """
    Input: str containing functions and other characters 
    Output: list of strs with functions that match the regex pattern 
    """
    # mul = starts with mul
    # \( = a (
    # [0-9] = a digit
    # {1,3} = between 1 and 3 digits 

    matches = re.findall("mul\(*[0-9]{1,3}\,[0-9]{1,3}\)", string)
    return matches


def perform_function(string):
    """
    Input: str containing a correctly formated func e.g. 'mul(2,4)'
    """
    
    number_1 = re.findall(r"mul\(([^,]+),", string) # Match between ( and ,
    number_2 =  re.findall(r",([^)]+)\)", string) # Match between , and )

    number_1 = int(number_1[0]) # Convert to int
    number_2 = int(number_2[0])

    multiply = number_1 * number_2 

    return multiply


def find_enabled_text(string):
    """
    Input: string containing functions and other characters e.g. 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)
    Output: string with the sequence between the enabled part
    Required for part 2 
    """
    # Filter the input string to contain only the data between do e.g. excude after 'don't"
    # From any 'do' to the next 'dont'

    # The string starts as enabled so add 'do()' to the start of the sequence
    # In the case that the input doesnt end in 'don't()' add it to the end 

    string = 'do()' + string + 'don\'t()'
    # (.*?) matches everything between do() and don't() not the \ just stops it being a special character
    enabled_string_matches = re.findall(r"do\(\)(.*?)don\'t\(\)", string, re.DOTALL) # NOTE THE RE.DOTALL is key ! as it matches across lines. 
    enabled_string = "".join(enabled_string_matches) # This joins all the matches together to one string 
    return enabled_string



def find_perform_and_sum(string, enabler_activated=False):
    """
    Given the input data, finds the functions, performs them and sums the output
    Input: String e.g xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5)
    Output: Int e.g. 161
    enabler_activated=True for part 2 
    """
    if enabler_activated:
        string = find_enabled_text(string)

    functions = find_functions(string)
    sum = 0
    for func in functions:
        result = perform_function(func)
        sum += result
    return sum 


if __name__ == "__main__":
    # run_tests()
    input_text_file = '/Users/mahony/Downloads/aoc_2024_day_3.txt'
    with open(input_text_file) as f:
        input = f.read()
    print('PART 1 = ', find_perform_and_sum(input))
    print('PART 2 = ', find_perform_and_sum(input, enabler_activated=True))


# Part 1: which updates are already in the right order.

def process_puzzle_input(puzzle_input):
    """
    Input: str of puzzle input 
    Output: 
        ordering_rules: list of tuples, within which the 1st int is the before number and the secod is the after number
        numbers_of_update: list of lists, within which is ints which are the 'updates' 


    """
    ordering_rules, numbers_of_update = puzzle_input.split('\n\n') # Theres a blank line spliting the inputs

    # Ordering rules to a list of tuples on each line split by a |
    ordering_rules = ordering_rules.split('\n')
    ordering_rules = [pair.split('|') for pair in ordering_rules]
    ordering_rules = [tuple(map(int, pair)) for pair in ordering_rules] # tuple required before map otherwise it is a map function iterator 

    numbers_of_update = numbers_of_update.split('\n') # Each line is an 'update'
    numbers_of_update = list(filter(None, numbers_of_update)) # Remove blanks 
    numbers_of_update = [list(map(int, update.split(','))) for update in numbers_of_update] # Each update is an int seperated by , 
    

    return ordering_rules, numbers_of_update


def determine_update_correct(update, ordering_rules):
    """
    Input: 
        update: list of ints e.g. [73, 61, 24, 42, 64, 66, 18, 15, 29]
        ordering_rules: list of tuples e.g. (73, 89)
    Output: bool if the order of the update matches the ordering rules 
    """

    # Check all possible rule violations?

    for i in range(len(update) -1):
        page = update[i]
        # Search for it in ordering rules 
        if (update[i], update[i+1]) in ordering_rules:
            print('Found!')
        else:
            print(f'not present {(update[i], update[i+1])}')




if __name__ == "__main__":
    with open('/Users/mahony/Downloads/aoc_2024_day_5.txt') as f:
        puzzle_input = f.read()
    ordering_rules, numbers_of_update = process_puzzle_input(puzzle_input)
    print(ordering_rules[0])
    print(numbers_of_update[0])
    determine_update_correct(numbers_of_update[0], ordering_rules)


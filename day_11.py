# Counting mutating stones 
from tqdm import tqdm 
from itertools import chain
from collections import defaultdict

def parse_input(input_file_path):
    """
    Returns a list of ints, each one a 'stone'
    """
    with open(input_file_path) as f:
        input = f.read().strip().split()
        stones = [int(x) for x in input]
    return stones

def permute_stone(stone):
    """
    stone is an int
    """
    if stone == 0:
        new_stone = [1]
    # if the length of the integer is divisable by 2 with no remainders the number of digits is even 
    elif (len(str(stone))%2) == 0: 
        half_point = int(len(str(stone)) / 2)

        new_stone = [int(str(stone)[:half_point]), int(str(stone)[half_point:])] # conversion to ints removes trailing 0's
    else:
        new_stone = [stone *2024]
    return new_stone

def blinking(original_stones, number_blinks):
    #for _ in tqdm(range(number_blinks)):
    #    list_new_stones = []
    #    for stone in new_stones:
    #        list_new_stones.append(permute_stone(stone))
    #    new_stones =[x for xs in list_new_stones for x in xs]

    # Reolaced with itertools.chain.from_iterable with map to aviod repeatedly extending a list
    # Also utilizes the laxy evaluation map 
    stones = original_stones
    for _ in tqdm(range(number_blinks)):
        stones = list(chain.from_iterable(map(permute_stone, stones)))
    return len(stones)

def faster_blinking(original_stones, number_blinks):
    """
    By using a dictionary computations on stones with the same number aren't unncessarily repeated
    The dictionary key - the number of the stone, value = the number of stones with that value
    """

    stones: dict[str, int] = {k: 1 for k in original_stones} # There is one stone of each in the input
    for _ in tqdm(range(number_blinks)):
        new_stones = defaultdict(int) # Blank default dict 
        for stone, num in stones.items():
            for new_stone in permute_stone(stone):
                new_stones[new_stone] += num # Increase the count by the value from the permute_stone for each stone 
                #- for this step its important that defaultdict() rather than dict() to be able to add unscene values without KeyError
        stones = new_stones
    return sum(stones.values()) # Sum all the values in the dict e.g. all the stone counts 


def test_part_1():
    test_stones = [125, 17]
    number_after_6 = blinking(test_stones, 6)
    number_after_25 = blinking(test_stones, 25)
    if number_after_6 ==22 and number_after_25 ==55312:
        print(f'Test part 1 passed')
        return True
    

def main():
    puzzle_input_path = '/Users/mahony/Downloads/aoc_2024_day_11.txt'
    puzzle_input = parse_input(puzzle_input_path)
    print(f"Part 1 = {blinking(puzzle_input, 25)}")
    print(f"Part 2 = {faster_blinking(puzzle_input, 75)}")



if __name__ == "__main__":
    #test_part_1()
    main()
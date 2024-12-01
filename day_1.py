# Day_1
# Given two lists, sort them and sum the difference of the values at each index 
import numpy as np 

def read_in_input(input_file_path):
    """
    Output: numpy array, no header 
    """
    df = np.loadtxt(input_file_path, dtype=int) 
    if df.shape[1] != 2:
        raise ValueError('There should be 2 columns of the dataset')
    return df



def sum_pairwise_difference(df):
    """
    Input: df = dataframe with two columns
    Output: int of the total of the difference of the two columns once sorted at each index 
    """
    # Sort the columns 
    df = np.sort(df, axis=0) # axis= 0 means sorting is performed column wise e.g both columns sorted independently 
    # Get the absolute difference btween each pair 
    diff = np.diff(df) 
    abs_difference = np.abs(diff) # This removes the negatives
    # Sum the differences down the column
    sum_diff = np.sum(abs_difference, axis=0)
    return sum_diff



def similarity_score_freq(df):
    """
    Input: df = dataframe with two columns
    Output: int of similarity score 

    Similarity score = The sum of the frequence of each int in column 1 in column 2 multiplied by its value 

    """

    # function to get the frequency in column 2 df[:, 1] gets all the second column values. : = all rows ,1 = the second column
    unique_values, counts = np.unique(df[:,1], return_counts=True)
    counts_dict = dict(zip(unique_values, counts)) # A dictionary of the frequency of occurances of each value in column 2 
    similarity_scores = [i * counts_dict.get(int(i), 0) for i in df[:,0]] 
    # df[:,0] is column 1  
    # get(, 0) means that if i is not in the dict 0 will bee returned. Without this you get an error in this case. 

    return sum(similarity_scores)


if __name__ == "__main__":
    # Test dataset
    test_df = np.array([[1, 2],
                         [3, 4], 
                         [0, 15]])
    test_result_part_a = [17]
    test_output_part_a = sum_pairwise_difference(test_df)
    if  test_output_part_a == test_result_part_a:
        print('Test dataset works')
    else:
        print(f'Error : {test_output_part_a}')

    test_result_part_b = [0]
    test_output_part_b = similarity_score_freq(test_df)
    if test_output_part_b == test_result_part_b:
        print('Test works for part b ')
    else: print(f'Error : {test_output_part_b}')

    # AOC dataset
    input_file_path = '/Users/mahony/Downloads/aoc_2024_day_1.txt'
    df = read_in_input(input_file_path)
    print('PART A')
    print(sum_pairwise_difference(df))
    print('PART B')
    print(similarity_score_freq(df))
import pandas as pd 


def read_in_data(input_file_path):
    # Read in the data as a list of lists 
    # Each nested list is a 'report' which consists of ints which are 'levels'
    with open(input_file_path) as f:
        records = [line.rstrip() for line in f] # Split by the line split and remove trailing characters
        records = [line.split() for line in records] # Split each line into a list 
        records = [list(map(int, line)) for line in records] # Turn strings to ints 
    return records


def determine_if_report_is_safe(report):
    """
    Given a list of ints (e.g. a record) determine if they are 'safe'
    Safe = all decreasing or increasing, differences between 1 and 3 
    Input = list of ints
    Output = str of 'SAFE' or 'UNSAFE'
    """

    # Get the difference between the consecutive values in a report 
    difference = [report[i+1] - report[i] for i in range(len(report) -1)]

    # See if these difference is either 1, 2, 3 or -1, -2, -3 by the length of the difference of the sets. 
    positive_set = set([1, 2, 3])
    negative_set = set([-1, -2, -3])

    if len(set(difference) - (positive_set)) == 0 : # All sets in + set
        status = 'SAFE'
    elif len(set(difference) - (negative_set)) == 0: 
        status = 'SAFE'
    else:
        status = 'UNSAFE'
    return status


def add_dampener(report):
    """
    Given a list, remove 1 step at each position and if any of the new reports are safe, return safe
    Input: a list e.g. [8 6 4 4 1]
    Test 6 4 4 1, 8441, 8641, 8641, 8644 as being safe and if any are return SAFE
    Output: 'SAFE' or 'UNSAFE'
    """
    new_reports = []
    for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        new_reports.append(copy)
    status = [determine_if_report_is_safe(report) for report in new_reports]
    if 'SAFE' in status:
        return 'SAFE'
    else:
        return 'UNSAFE'
       

def count_safe_reports(reports, with_dampener=False):
    safe = 0 
    for report in reports:
        if determine_if_report_is_safe(report) == 'SAFE':
            safe += 1
    if with_dampener:
        safe = 0 
        for report in reports:
            if add_dampener(report) == 'SAFE':
                safe += 1
    return safe


def run_tests():
    print(determine_if_report_is_safe([7, 6, 4, 2, 1]))
    print(determine_if_report_is_safe([1, 2, 7, 8, 9]))


if __name__ == "__main__":
    run_tests()
    input_file_path ='/Users/mahony/Downloads/aoc_2024_day_2.txt'
    data = read_in_data(input_file_path)
    print(count_safe_reports(data))
    print(count_safe_reports(data, with_dampener=True))
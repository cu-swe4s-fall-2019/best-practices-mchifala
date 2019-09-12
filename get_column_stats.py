import sys
import math
import argparse


def main(file_name, col_num):
    """
    This script calculates the mean and standard deviation of a column in a data file.

    Parameters:
    ___________
        - file_name(str): The file of interest
        - col_num(int): The specific column we want to analyze

    Returns:
    ________
        - None; the mean and standard deviation are printed to stdout
    """

    # Open user-defined file
    try:
        f = open(file_name, 'r')

    except FileNotFoundError:
        print("Data file not found. Please check file name and directory.")
        sys.exit(1)

    except PermissionError:
        print("Invalid permissions for data file.")
        sys.exit(1)

    V = []

    # Append each element of the user-defined column to a list
    try:
        for l in f:
            A = [int(x) for x in l.split()]
            V.append(A[col_num])

    except ValueError:
        print("Data file contains a value with invalid input type.")
        sys.exit(1)

    except IndexError:
        print("Column number does not exist in data file.")
        sys.exit(1)

    # Calculate mean of the elements in list
    try:
        mean = sum(V)/len(V)

    except ZeroDivisionError:
        print("Column is empty. Cannot perform calculations")
        sys.exit(1)

    # Calculate standard deviation of the elements in list
    try:
        stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

    except ZeroDivisionError:
        print("Column is empty. Cannot perform calculations")
        sys.exit(1)

    # Print results
    print('mean:', mean)
    print('stdev:', stdev)

    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Column stats input")

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file (with extension)',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='Column number to be analyzed',
                        required=True)

    args = parser.parse_args()
    main(args.file_name, args.col_num)

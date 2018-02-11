# Joseph Worsfold


def read_sudoku(file_name):
    """Reads and returns in a sudoku problem from a file."""
    stream = open(file_name)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))


def convertToSets(problem):
    """Given a two-dimensional array `problem` of integers, create and
    return a new two-dimensional array of sets."""
    new_lst = [[y for y in x] for x in problem]
    for row in range(len(new_lst)):
        for column in range(len(new_lst[0])):
            if new_lst[row][column] == 0:
                new_lst[row][column] = set(range(1, 10))
            else:
                new_lst[row][column] = set([new_lst[row][column]])
    return new_lst


def convertToInts(problem):
    """Given a two-dimensional array `problem` of sets, create and return a
    new two-dimensional array of integers."""
    new_lst = [[y for y in x] for x in problem]
    for row in range(len(new_lst)):
        for column in range(len(new_lst[0])):
            if len(new_lst[row][column]) > 1:
                new_lst[row][column] = 0
            else:
                new_lst[row][column] = next(iter(new_lst[row][column]))
    return new_lst


def getRowLocations(rowNumber):
    """Given a `rowNumber`, return a list of all nine "locations" 
    row, column)`  tuples) in that row."""
    return [(rowNumber, columnNumber) for columnNumber in range(9)]


def getColumnLocations(columnNumber):
    """Given a `columnNumber`, return a list of all nine "locations"
    (`(row, column)`  tuples) in that column."""
    return [(rowNumber, columnNumber) for rowNumber in range(9)]


def getBoxLocations(location):
    """Return a list of all nine "locations"  (`(row, column)`  tuples) in
    the same box as the given `location`."""
    row, column = location
    if row / 3 < 1 and column / 3 < 1:  # top, left box
        box_locations = [(x, y) for x in range(3) for y in range(3)]
    elif row / 3 < 1 and 1 <= column / 3 < 2:  # top, middle box
        box_locations = [(x, y) for x in range(3) for y in range(3, 6)]
    elif row / 3 < 1 and 2 <= column / 3 < 3:  # top, right box
        box_locations = [(x, y) for x in range(3) for y in range(6, 9)]
    elif 1 <= row / 3 < 2 and column / 3 < 1:  # middle, left box
        box_locations = [(x, y) for x in range(3, 6) for y in range(3)]
    elif 1 <= row / 3 < 2 and 1 <= column / 3 < 2:  # middle, middle box
        box_locations = [(x, y) for x in range(3, 6) for y in range(3, 6)]
    elif 1 <= row / 3 < 2 and 2 <= column / 3 < 3:  # middle, right box
        box_locations = [(x, y) for x in range(3, 6) for y in range(6, 9)]
    elif 2 <= row / 3 < 3 and column / 3 < 1:  # bottom, left box
        box_locations = [(x, y) for x in range(6, 9) for y in range(3)]
    elif 2 <= row / 3 < 3 and 1 <= column / 3 < 2:  # bottom, middle box
        box_locations = [(x, y) for x in range(6, 9) for y in range(3, 6)]
    else:  # bottom, right box
        box_locations = [(x, y) for x in range(6, 9) for y in range(6, 9)]
    return box_locations


def eliminate(problem, location, listOfLocations):
    """For each location in the `listOfLocations`, except `location`, remove
    the number in `location` from the set in each other location."""
    row, column = location
    single_set = problem[row][column]
    count = 0
    for list_location in listOfLocations:
        x, y = list_location
        if (x, y) != (row, column):
            if single_set <= problem[x][y]:
                problem[x][y] -= single_set
                count += 1
    return count


def isSolved(problem):
    """Given a two-dimensional array `problem` of sets, return `True` if
    the Sudoku problem has been solved (every set contains exactly one
    element), and `False` otherwise."""
    for row in range(len(problem)):
        for column in range(len(problem[0])):
            if len(problem[row][column]) != 1:
                return False
    return True


def solve(problem):
    """Given a two-dimensional array `problem` of sets, try to solve it.
    This function changes the array `problem` and returns `True` if the
    problem has been solved, `False` otherwise."""
    solved = False
    while not solved:
        count = 0
        for row in range(len(problem)):
            for column in range(len(problem[0])):
                if len(problem[row][column]) == 1:
                    listOfLocations = (getRowLocations(row) +
                                       getColumnLocations(column) +
                                       getBoxLocations((row, column)))
                    count += eliminate(problem, (row, column), listOfLocations)
        if count == 0:
            return False
        solved = isSolved(problem)
    return True

# Add to solve:
#     For each list of box locations, based on the current location, check
#     if there is a lone number within all the location sets.


def print_sudoku(problem):
    """Prints the Sudoku array (given as a list of lists of integers) in
    the following form, using dots to represent zeros."""
    border = "+-------+-------+-------+"
    for row in range(len(problem)):
        if row in {0, 3, 6}:
            print(border)
        for column in range(len(problem[0])):
            if column in {0, 3, 6}:
                print("| ", end='')
            if problem[row][column] == 0:
                print(". ", end='')
            else:
                print(str(problem[row][column]) + " ", end='')
        print("|")
    print(border)


def main():
    problem = read_sudoku(input("Name the file containing the puzzle: "))
    print_sudoku(problem)
    problemAsSets = convertToSets(problem)
    solved = solve(problemAsSets)
    result = convertToInts(problemAsSets)
    print_sudoku(result)
    if not solved:
        for x in range(len(problemAsSets)):
            for y in range(len(problemAsSets[0])):
                if len(problemAsSets[x][y]) > 1:
                    print("Location " + str((x, y)) + " might be any of " +
                          str(problemAsSets[x][y]))
    ask = input("Do you want to read in and solve another puzzle? (Y/y): ")
    accept = {'Y', 'y', 'Yes', 'yes', 'YES'}
    if ask in accept:
        main()


if __name__ == '__main__':
    main()

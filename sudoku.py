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
    new_lst = [[i for i in j] for j in problem]
    for i in range(len(new_lst)):
        for j in range(len(new_lst[0])):
            if new_lst[i][j] == 0:
                s = set(range(1, 10))
                new_lst[i][j] = s
            else:
                s = set()
                s.add(new_lst[i][j])
                new_lst[i][j] = s
    return new_lst


def convertToInts(problem):
    """Given a two-dimensional array `problem` of sets, create and return a
    new two-dimensional array of integers."""
    new_lst = [[i for i in j] for j in problem]
    for i in range(len(new_lst)):
        for j in range(len(new_lst[0])):
            if len(new_lst[i][j]) > 1:
                new_lst[i][j] = 0
            else:
                new_lst[i][j] = next(iter(new_lst[i][j]))
    return new_lst


def getRowLocations(rowNumber):
    """Given a `rowNumber`, return a list of all nine "locations" 
    row, column)`  tuples) in that row."""
    return [(rowNumber, i) for i in range(9)]


def getColumnLocations(columnNumber):
    """Given a `columnNumber`, return a list of all nine "locations"
    (`(row, column)`  tuples) in that column."""
    return [(i, columnNumber) for i in range(9)]


def getBoxLocations(location):
    """Return a list of all nine "locations"  (`(row, column)`  tuples) in
    the same box as the given `location`."""
    r, c = location
    if r / 3 < 1 and c / 3 < 1:  # top, left box
        box_locations = [(i, j) for i in range(3) for j in range(3)]
    elif r / 3 < 1 and 1 <= c / 3 < 2:  # top, middle box
        box_locations = [(i, j) for i in range(3) for j in range(3, 6)]
    elif r / 3 < 1 and 2 <= c / 3 < 3:  # top, right box
        box_locations = [(i, j) for i in range(3) for j in range(6, 9)]
    elif 1 <= r / 3 < 2 and c / 3 < 1:  # middle, left box
        box_locations = [(i, j) for i in range(3, 6) for j in range(3)]
    elif 1 <= r / 3 < 2 and 1 <= c / 3 < 2:  # middle, middle box
        box_locations = [(i, j) for i in range(3, 6) for j in range(3, 6)]
    elif 1 <= r / 3 < 2 and 2 <= c / 3 < 3:  # middle, right box
        box_locations = [(i, j) for i in range(3, 6) for j in range(6, 9)]
    elif 2 <= r / 3 < 3 and c / 3 < 1:  # bottom, left box
        box_locations = [(i, j) for i in range(6, 9) for j in range(3)]
    elif 2 <= r / 3 < 3 and 1 <= c / 3 < 2:  # bottom, middle box
        box_locations = [(i, j) for i in range(6, 9) for j in range(3, 6)]
    else:  # bottom, right box
        box_locations = [(i, j) for i in range(6, 9) for j in range(6, 9)]
    return box_locations


def eliminate(problem, location, listOfLocations):
    """For each location in the `listOfLocations`, except `location`, remove
    the number in `location` from the set in each other location."""
    r, c = location
    single_set = problem[r][c]
    count = 0
    for i in listOfLocations:
        x, y = i
        if (x, y) != (r, c):
            if single_set <= problem[x][y]:
                problem[x][y] -= single_set
                count += 1
    return count


def isSolved(problem):
    """Given a two-dimensional array `problem` of sets, return `True` if
    the Sudoku problem has been solved (every set contains exactly one
    element), and `False` otherwise."""
    for i in range(len(problem)):
        for j in range(len(problem[0])):
            if len(problem[i][j]) > 1:
                return False
    return True


def solve(problem):
    """Given a two-dimensional array `problem` of sets, try to solve it.
    This function changes the array `problem` and returns `True` if the
    problem has been solved, `False` otherwise."""
    solved = False
    while not solved:
        count = 0
        for i in range(len(problem)):
            for j in range(len(problem[0])):
                if len(problem[i][j]) == 1:
                    location = (i, j)
                    listOfLocations = (getRowLocations(i) +
                                       getColumnLocations(j) +
                                       getBoxLocations(location))
                    count += eliminate(problem, location, listOfLocations)
        if count == 0:
            return False
        solved = isSolved(problem)
    return True


def print_sudoku(problem):
    """Prints the Sudoku array (given as a list of lists of integers) in
    the following form, using dots to represent zeros."""
    border = "+-------+-------+-------+"
    for i in range(len(problem)):
        if i == 0 or i == 3 or i == 6:
            print(border)
        for j in range(len(problem[0])):
            if j == 0 or j == 3 or j == 6:
                print("| ", end='')
            if problem[i][j] == 0:
                print(". ", end='')
            else:
                print(str(problem[i][j]) + " ", end='')
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
        for i in range(len(problemAsSets)):
            for j in range(len(problemAsSets[0])):
                if len(problemAsSets[i][j]) > 1:
                    print("Location " + str((i, j)) + " might be any of " +
                          str(problemAsSets[i][j]))
    ask = input("Do you want to read in and solve another puzzle? (Y/y): ")
    accpt = {'Y', 'y', 'Yes', 'yes', 'YES'}
    if ask in accpt:
        main()


if __name__ == '__main__':
    main()

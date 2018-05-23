Please try and make the best use of loops, constants, *helper* functions, etc.

```
def getBoxLocations(location):
    """Return a list of all nine "locations"  (`(row, column)`  tuples) in
    the same box as the given `location`."""
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
```
You should have been able to write a function which extracted the appropriate box and avoided this deeply nested choice and also didn't use *magic* numbers.

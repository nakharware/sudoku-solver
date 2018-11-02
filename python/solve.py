#!/usr/bin/python

class Cell:
    def __init__(self, value = None):
        if value != None and value > 0 and value < 10:
            self.is_solved = True
            self.solution = value
            self.has_changed = False
            self.possible_values = None
        else:
            self.is_solved = False
            self.solution = None
            self.has_changed = True
            self.possible_values = [x for x in range(1, 10)]

    def solve(self, values):
        self.has_changed = False
        if values != None:
            if not self.is_solved:
                for value in values:
                    if value > 0 and value < 10:
                        try:
                            self.possible_values.remove(value)
                            self.has_changed = True
                            if len(self.possible_values) == 1:
                                self.is_solved = True
                                self.solution = self.possible_values[0]
                        except ValueError:
                            pass
                
        return self.has_changed

class CellGroup:
    def __init__(self):
        self.is_solved = False
        self.has_changed = True
        self.cells = []

    def add_cell(self, cell):
        if len(self.cells) < 9:
            self.cells.append(cell)

    def solve(self):
        solutions = []
        self.has_changed = False
        if not self.is_solved:
            # Find all the solved cells and add their solution to the list of values found
            for cell in self.cells:
                if cell.is_solved:
                    solutions.append(cell.solution)

            # Check we aren't completely solved now
            if len(solutions) == 9:
                self.is_solved = True

            # Remove all the found values from all the cells that are still to be solved
            if len(solutions) > 0 and len(solutions) < 9:
                for cell in self.cells:
                    cell.solve(solutions)
                    if cell.has_changed:
                        self.has_changed = True

if __name__ == "__main__":
    pass

#!/usr/bin/python

import unittest
import solve

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.emptyCell = solve.Cell()
        self.initialisedCell = solve.Cell(9)
        self.initialisedCell2 = solve.Cell(11)
        self.row = solve.CellGroup()
        cell1 = solve.Cell(1)
        self.row.add_cell(cell1)
        cell2 = solve.Cell(3)
        self.row.add_cell(cell2)
        cell3 = solve.Cell(5)
        self.row.add_cell(cell3)
        for index in range(9):
            cell = solve.Cell()
            self.row.add_cell(cell)

    def test_empty_cell(self):
        self.assertEqual(self.emptyCell.possible_values, [1,2,3,4,5,6,7,8,9])
        self.assertFalse(self.emptyCell.is_solved)

    def test_initialised_cell(self):
        self.assertEqual(self.initialisedCell.solution, 9)
        self.assertTrue(self.initialisedCell.is_solved)

    def test_invalid_initialised_cell(self):
        self.assertEqual(self.initialisedCell2.possible_values, [1,2,3,4,5,6,7,8,9])
        self.assertFalse(self.initialisedCell2.is_solved)

    def test_solve_cell(self):
        self.emptyCell.solve([1,3,11])
        self.assertEqual(self.emptyCell.possible_values, [2,4,5,6,7,8,9])

    def test_rowlen(self):
        self.assertEqual(len(self.row.cells), 9)

    def test_row_solve(self):
        self.row.solve()
        self.assertEqual(len(self.row.cells), 9)
        self.assertFalse(self.row.is_solved)
        self.assertEqual(self.row.cells[0].solution, 1)
        self.assertEqual(self.row.cells[1].solution, 3)
        self.assertEqual(self.row.cells[2].solution, 5)
        self.assertEqual(self.row.cells[3].possible_values, [2,4,6,7,8,9])
        self.assertEqual(self.row.cells[4].possible_values, [2,4,6,7,8,9])
        self.assertEqual(self.row.cells[5].possible_values, [2,4,6,7,8,9])
        self.assertEqual(self.row.cells[6].possible_values, [2,4,6,7,8,9])
        self.assertEqual(self.row.cells[7].possible_values, [2,4,6,7,8,9])
        self.assertEqual(self.row.cells[8].possible_values, [2,4,6,7,8,9])

if __name__ == "__main__":
    unittest.main()

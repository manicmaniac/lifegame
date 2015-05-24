#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from lifegame import Cell

class TestCell(unittest.TestCase):
    def test_equal(self):
        cell1 = Cell(0, 0)
        cell2 = Cell(0, 0)
        self.assertEqual(cell1, cell2)

    def test_relative(self):
        cell1 = Cell(0, 0).relative(1, 1)
        cell2 = Cell(2, 2).relative(-1, -1)
        self.assertEqual(cell1, cell2)

    def test_with_neighbors(self):
        cell = Cell(0, 0)
        cell_with_neighbors = cell.with_neighbors()
        self.assertIn(cell, cell_with_neighbors)
        self.assertEqual(9, len(cell_with_neighbors))

    def test_neighbors(self):
        cell = Cell(0, 0)
        neighbors = cell.neighbors()
        self.assertNotIn(cell, neighbors)
        self.assertEqual(8, len(neighbors))


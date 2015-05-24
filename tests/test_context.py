#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import collections
from lifegame import Context, Cell

class TestContext(unittest.TestCase):
    def test_init(self):
        context = Context()
        self.assertIsNotNone(context.rule)

    def test_produce_and_kill(self):
        context = Context()
        cell = Cell(0, 0)
        context.produce(cell)
        self.assertIn(cell, context._living_cells)
        context.kill(cell)
        self.assertNotIn(cell, context._living_cells)

    def test_is_alive(self):
        context = Context()
        cell = Cell(0, 0)
        self.assertFalse(context.is_alive(cell))
        context.produce(cell)
        self.assertTrue(context.is_alive(cell))

    def test__will_survive1(self):
        context = Context()
        cell1 = Cell(0, 0)
        cell2 = Cell(1, 0)
        cell3 = Cell(2, 0)
        context.produce(cell1)
        context.produce(cell2)
        context.produce(cell3)
        self.assertFalse(context._will_survive(cell1))

    def test__will_survive2(self):
        context = Context()
        cell1 = Cell(0, 0)
        cell2 = Cell(1, 0)
        cell3 = Cell(2, 0)
        context.produce(cell1)
        context.produce(cell2)
        context.produce(cell3)
        self.assertTrue(context._will_survive(cell2))

    def test__cells_to_calculate(self):
        '''
        O: alive
        X: dead
           -10123
        -1| XXXXX
         0| XOOOX
         1| XXXXX
        '''
        context = Context()
        cell1 = Cell(0, 0)
        cell2 = Cell(1, 0)
        cell3 = Cell(2, 0)
        context.produce(cell1)
        context.produce(cell2)
        context.produce(cell3)
        cells_to_calculate = context._cells_to_calculate()
        self.assertTrue(len(cells_to_calculate), 12)

    def test_next(self):
        '''
        O: alive
        X: dead
           -10123   -10123
        -1| XXXXX    XXOXX
         0| XOOOX => XXOXX
         1| XXXXX    XXOXX
        '''
        context = Context()
        cell1 = Cell(0, 0)
        cell2 = Cell(1, 0)
        cell3 = Cell(2, 0)
        cell4 = Cell(-1, 1)
        cell5 = Cell(1, 1)
        context.produce(cell1)
        context.produce(cell2)
        context.produce(cell3)
        context.next()
        self.assertFalse(context.is_alive(cell1))
        self.assertTrue(context.is_alive(cell3))
        self.assertFalse(context.is_alive(cell3))
        self.assertTrue(context.is_alive(cell4))
        self.assertTrue(context.is_alive(cell5))


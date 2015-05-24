#!/usr/bin/env python
# -*- coding:utf-8 -*-

from rule import Rule
from cell import Cell

class Context(object):
    def __init__(self, rule=None):
        if rule is None:
            rule = Rule.standard()
        self._rule = rule
        self._living_cells = set()

    def bear(self, cell):
        self._living_cells.add(cell)

    def kill(self, cell):
        self._living_cells.remove(cell)

    def clear(self):
        self._living_cells.clear()

    def is_alive(self, cell):
        return cell in self._living_cells

    def next(self):
        self._living_cells = {cell for cell in self._cells_to_calculate() if self._will_survive(cell)}

    def _will_survive(self, cell):
        if self.is_alive(cell):
            condition = self.rule.survive
        else:
            condition = self.rule.born
        living_neighbors = cell.neighbors() & self._living_cells
        return len(living_neighbors) in condition

    def _cells_to_calculate(self):
        res = set()
        for cell in self._living_cells:
            res.update(cell.with_neighbors())
        return res

    @property
    def rule(self):
        return self._rule

    @property
    def living_cells(self):
        return self._living_cells


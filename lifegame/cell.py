#!/usr/bin/env python
# -*- coding:utf-8 -*-

import collections
import itertools

class Cell(collections.namedtuple('Cell', 'x y')):
    def relative(self, dx, dy):
        return self.__class__(self.x + dx, self.y + dy)

    def with_neighbors(self):
        distances = -1, 0, 1
        return set(itertools.starmap(self.relative, itertools.product(distances, repeat=2)))

    def neighbors(self):
        return self.with_neighbors() - {self}


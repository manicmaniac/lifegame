#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Rule(object):
    def __init__(self, string):
        self._survive, self._born = [tuple(map(int, elem)) for elem in string.split('/')]

    def __eq__(self, other):
        return self._survive == other._survive and self._born == other._born

    @classmethod
    def standard(cls):
        return cls('23/3')

    @property
    def survive(self):
        return self._survive

    @property
    def born(self):
        return self._born


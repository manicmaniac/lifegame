#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from lifegame import Rule

class TestRule(unittest.TestCase):
    def test_init(self):
        rule = Rule('23/3')
        self.assertEqual(rule.survive, (2, 3))
        self.assertEqual(rule.born, (3,))

    def test_standard(self):
        rule = Rule.standard()
        self.assertEqual(rule.survive, (2, 3))
        self.assertEqual(rule.born, (3,))

    def test_equal(self):
        rule1 = Rule.standard()
        rule2 = Rule('23/3')
        self.assertEqual(rule1, rule2)


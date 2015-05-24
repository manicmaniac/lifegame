#!/usr/bin/env python
# -*- coding:utf-8 -*-

import curses
from curses.wrapper import wrapper
import sys
from context import Context
from cell import Cell

class Board(object):
    def __init__(self, window, context=None):
        self._context = context
        self._window = window
        self.is_executing = False

    def start(self):
        self.is_executing = True
        self.step()

    def step(self):
        if self.is_executing:
            y, x = self._window.getyx()
            self._context.next()
            self._window.erase()
            self.draw()
            self._window.move(y, x)

    def stop(self):
        self.is_executing = False

    def clear(self):
        self._context.clear()
        self._window.erase()

    def draw(self):
        for cell in self._context.living_cells:
            self.draw_cell(cell)

    def draw_cell(self, cell):
        x, y = self.points_for_cell(cell)
        if x >= 0 and y >= 0:
            self._window.move(y, x)
            self._window.addstr(y, x, '#')
            self._window.move(y, x)

    def remove_cell(self, cell):
        x, y = self.points_for_cell(cell)
        self._window.move(y, x)
        self._window.addstr(y, x, ' ')
        self._window.move(y, x)

    def toggle_cell(self, x, y):
        cell = self.cell_for_point(x, y)
        if self._context.is_alive(cell):
            self._context.kill(cell)
            self.remove_cell(cell)
        else:
            self._context.bear(cell)
            self.draw_cell(cell)

    def cell_for_point(self, x, y):
        return Cell(x, y)

    def points_for_cell(self, cell):
        return cell.x, cell.y


@wrapper
def main(stdscr):
    board = Board(stdscr, Context())
    while True:
        c = stdscr.getch()
        if c == ord('q'):
            break
        y, x = stdscr.getyx()
        if c == ord('h'):
            stdscr.move(y, x - 1)
        if c == ord('j'):
            stdscr.move(y + 1, x)
        if c == ord('k'):
            stdscr.move(y - 1, x)
        if c == ord('l'):
            stdscr.move(y, x + 1)
        if c == ord(' '):
            board.toggle_cell(x, y)
        if c == curses.KEY_ENTER or c == 10:
            if board.is_executing:
                board.stop()
            else:
                board.start()
    sys.exit()

if __name__ == '__main__':
    main()


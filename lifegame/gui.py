#!/usr/bin/env python
# -*- coding:utf-8 -*-

import Tkinter as tk
import sys
from context import Context
from cell import Cell

class Board(tk.Canvas):
    def __init__(self, master=None, context=None, cnf={}, **kw):
        tk.Canvas.__init__(self, master, cnf, **kw)
        self._context = context
        self.is_executing = False
        self.cell_width = 10
        self.cell_height = 10
        self.cell_color = 'black'
        self.bind('<Button-1>', self.toggle_cell)

    def start(self):
        self.is_executing = True
        self.step()

    def step(self):
        if self.is_executing:
            self._context.next()
            self.delete(tk.ALL)
            self.draw()
            self.after(100, self.step)

    def stop(self):
        self.is_executing = False

    def clear(self):
        self._context.clear()
        self.delete(tk.ALL)

    def draw(self):
        for cell in self._context.living_cells:
            self.draw_cell(cell)

    def draw_cell(self, cell):
        self.create_rectangle(*self.points_for_cell(cell), fill=self.cell_color, tags=self.tag_for_cell(cell))

    def remove_cell(self, cell):
        self.delete(self.tag_for_cell(cell))

    def toggle_cell(self, event):
        cell = self.cell_for_point(event.x, event.y)
        if self._context.is_alive(cell):
            self._context.kill(cell)
            self.remove_cell(cell)
        else:
            self._context.bear(cell)
            self.draw_cell(cell)

    def cell_for_point(self, x, y):
        return Cell(x / self.cell_width, y / self.cell_height)

    def points_for_cell(self, cell):
        return (
            self.cell_width  * cell.x,
            self.cell_height * cell.y,
            self.cell_width  * (cell.x + 1),
            self.cell_height * (cell.y + 1),
        )

    def tag_for_cell(self, cell):
        return '{}.{}'.format(cell.x, cell.y)


class Menu(tk.Menu):
    def __init__(self, master=None, board=None, cnf={}, **kw):
        tk.Menu.__init__(self, master, cnf, **kw)
        self.board = board
        game = tk.Menu(self, tearoff=False)
        game.add_command(label='Start', command=self.board.start)
        game.add_command(label='Stop', command=self.board.stop)
        game.add_command(label='Clear', command=self.board.clear)
        game.add_separator()
        game.add_command(label='Quit', command=sys.exit)
        self.add_cascade(label='Game', menu=game)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('lifegame')
    board = Board(root, context=Context())
    board.draw()
    board.pack(fill=tk.BOTH, expand=True)
    menu = Menu(root, board)
    root.configure(menu=menu)
    root.mainloop()


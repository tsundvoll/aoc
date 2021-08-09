import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


def parse(data):
    tiles = {}
    current_tile = np.zeros((10,10), np.int8)
    current_row = 0
    for line in data:
        if line == '':
            tiles[title] = current_tile
            current_tile = np.zeros((10,10), np.int8)
            current_row = 0
        elif line[0] == 'T':
            _, t_id = line.split(" ")
            title = int(t_id[:-1])
        else:
            current_tile[current_row] = np.array(
                [1 if x=='#' else 0 for x in line]
            )
            current_row += 1
    return tiles


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.canvas = tk.Canvas(root, width=230, height=230)
        self.canvas.pack()
        self.assemble_image('test.txt')  # Answer: 20899048083289
        # self.assemble_image('input.txt')

    def assemble_image(self, filename):
        tiles = parse([x for x in open(filename).read().splitlines()])

        while tiles:
            keys = [key for key in tiles.keys()]
            print(keys)
            first_key = keys[0]
            first_tile = tiles[first_key]
            print(first_tile)
            img = ImageTk.PhotoImage(image=Image.fromarray(first_tile))
            self.canvas.create_image(10, 10, anchor="nw", image=img)
            self.canvas.update()
            break


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


"""
12 x 12 image

Center tile at (11, 11)

Image size: 23 x 23
"""
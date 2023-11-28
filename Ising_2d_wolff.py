"""
This file defines Ising Grid Class
Name: Shangkun LI
Student ID: 20307130215
"""

import numpy as np


class Grid(object):
    """
    Grid is a 2-D, periodic-boundaried and square canvas consisting of spins.
    """

    def __init__(self, size, Jfactor):
        self.size = size
        self.Jfactor = Jfactor
        self.canvas = np.ones([size, size], int)

    def randomize(self):
        self.canvas = np.random.randint(0, 2, [self.size, self.size]) * 2 - 1

    def left(self, x, y):
        if x < 0.5:
            return [self.size - 1, y]
        else:
            return [x - 1, y]

    def right(self, x, y):
        if x > self.size - 1.5:
            return [0, y]
        else:
            return [x + 1, y]

    def up(self, x, y):
        if y < 0.5:
            return [x, self.size - 1]
        else:
            return [x, y - 1]

    def down(self, x, y):
        if y > self.size - 1.5:
            return [x, 0]
        else:
            return [x, y + 1]

    # Cluster Filp (Wolff Algorithm)
    def ClusterFlip(self, temperature):
        # Randomly pick a seed spin
        x = np.random.randint(0, self.size)
        y = np.random.randint(0, self.size)

        # stack is the list of spins in cluster
        sign = self.canvas[x, y]
        P_add = 1 - np.exp(-2.0 * self.Jfactor / temperature)
        stack = [[x, y]]
        lable = np.ones([self.size, self.size], int)
        lable[x, y] = 0

        while len(stack) > 0.5:
            # While stack is not empty, pop and flip a spin
            [current_x, current_y] = stack.pop()
            self.canvas[current_x, current_y] = -sign  # flip the seed spin first

            # Append neighbor spins

            # Left neighbor
            [left_x, left_y] = self.left(current_x, current_y)
            if (
                (self.canvas[left_x, left_y] * sign > 0.5)
                and (lable[left_x, left_y])
                and (np.random.rand() < P_add)
            ):
                stack.append([left_x, left_y])
                lable[left_x, left_y] = 0

            # Right neighbor
            [right_x, right_y] = self.right(current_x, current_y)
            if (
                (self.canvas[right_x, right_y] * sign > 0.5)
                and (lable[right_x, right_y])
                and (np.random.rand() < P_add)
            ):
                stack.append([right_x, right_y])
                lable[right_x, right_y] = 0

            # Up neighbor
            [up_x, up_y] = self.up(current_x, current_y)
            if (
                (self.canvas[up_x, up_y] * sign > 0.5)
                and (lable[up_x, up_y])
                and (np.random.rand()) < P_add
            ):
                stack.append([up_x, up_y])
                lable[up_x, up_y] = 0

            # Down neighbor
            [down_x, down_y] = self.down(current_x, current_y)
            if (
                (self.canvas[down_x, down_y] * sign > 0.5)
                and (lable[down_x, down_y])
                and np.random.rand() < P_add
            ):
                stack.append([down_x, down_y])
                lable[down_x, down_y] = 0

        # Return cluster size
        return self.size * self.size - sum(sum(lable))

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


def display_field(field):
    """
        display the field
    """
    array_to_display = []
    for y in range(len(field.cells)):
        array_to_display.append([])
        for x in range(len(field.cells[y])):
            array_to_display[y].append(field.cells[y][x].type.value)
    plt.pcolormesh(array_to_display, cmap="summer")

    plt.title('Field delimitation', fontweight ="bold")
    plt.show()

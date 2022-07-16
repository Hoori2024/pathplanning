import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.patches as mpatches

def display_field(field):
    """
        display the field
    """

    colors = [
        ['seagreen', "Cell completly inside"],
        ['lightseagreen', "Cell center inside"],
        ['orange', "Cell center outside"],
        ['firebrick', "Cell completly outside"],
        ['yellow', "Cell center on edge"]
    ]


    plt.axes()
    for edge in field.edges:
        line = plt.Line2D((edge[0][0], edge[1][0]), (edge[0][1], edge[1][1]), lw = 3, color='black')
        plt.gca().add_line(line)

    for y in range(len(field.cells)):
        for x in range(len(field.cells[y])):
            pos = (field.cells[y][x].center[0] - 0.5, field.cells[y][x].center[1] - 0.5)
            rectangle = plt.Rectangle(pos , 1, 1, fc=colors[field.cells[y][x].type.value][0])
            plt.gca().add_patch(rectangle)

    for y in range(len(field.cells)):
        for x in range(len(field.cells[y])):
            center = (field.cells[y][x].center[0], field.cells[y][x].center[1])
            plt.plot(center[0], center[1], 'bo')

    legend = []
    for elem in colors:
        legend.append(mpatches.Patch(color=elem[0], label=elem[1]))
    legend = legend[:2] + [legend[4]] + legend[2:4]
    plt.legend(handles=legend, loc='lower left', bbox_to_anchor=(1.05, 0.95))

    plt.title('Field delimitation', fontweight ="bold")
    plt.axis('scaled')
    plt.tight_layout()
    plt.show()

def display_path(field, path):
    """
        display the field and the path
    """

    colors = [
        ['seagreen', "Cell completly inside"],
        ['lightseagreen', "Cell center inside"],
        ['orange', "Cell center outside"],
        ['firebrick', "Cell completly outside"],
        ['yellow', "Cell center on edge"]
    ]


    plt.axes()
    for edge in field.edges:
        line = plt.Line2D((edge[0][0], edge[1][0]), (edge[0][1], edge[1][1]), lw = 3, color='black')
        plt.gca().add_line(line)

    for y in range(len(field.cells)):
        for x in range(len(field.cells[y])):
            pos = (field.cells[y][x].center[0] - 0.5, field.cells[y][x].center[1] - 0.5)
            rectangle = plt.Rectangle(pos , 1, 1, fc=colors[field.cells[y][x].type.value][0])
            plt.gca().add_patch(rectangle)

    for y in range(len(field.cells)):
        for x in range(len(field.cells[y])):
            center = (field.cells[y][x].center[0], field.cells[y][x].center[1])
            plt.plot(center[0], center[1], 'bo')

    for i in range(len(path) - 1):
        line = plt.arrow(path[i][0], path[i][1], path[i + 1][0] - path[i][0], path[i + 1][1] - path[i][1], head_width=0.5, head_length=0.5, color='red')
        plt.gca().add_line(line)

    legend = []
    for elem in colors:
        legend.append(mpatches.Patch(color=elem[0], label=elem[1]))
    legend = legend[:2] + [legend[4]] + legend[2:4]
    plt.legend(handles=legend, loc='lower left', bbox_to_anchor=(1.05, 0.95))

    plt.title('Field delimitation and path', fontweight ="bold")
    plt.axis('scaled')
    plt.tight_layout()
    plt.show()

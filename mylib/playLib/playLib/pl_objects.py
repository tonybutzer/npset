"""
Module Documentation
Goes
HERE
"""

import matplotlib.pyplot as plt
from salishsea_tools import viz_tools

class Play(object):
    """Play is a library for exploring data and python concepts
    The first method is to create a png file from a data array

    Attributes:
        NONE.
    """

    def __init__(self):
        """Return a Play object whose name is *name* and starting
        """

    def pl_create_png(self, fname, array, cmap='prism', 
        xlabel='xlabel', ylabel='ylabel',
        title='TITLE', subtitle='SubTitle'):
        """creates a png file

        Parameters:
            fname:   the name of the output.png file
            array
            cmap
            xlabel
            ylabel
            title
            subtitle

        """
        fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        plt.gca().invert_yaxis()
        title = 'ColorMap== '+cmap
        # title = r'$\sigma_i=15$'
        # plt.title(title)
        plt.title(title, fontsize=20, color='blue')
        plt.suptitle('Temperature on a Cold Day', fontsize=30, color='green')
        #plt.xlabel('X Value Axis')
        t = plt.xlabel('X Value', fontsize=20, color='red')
        plt.ylabel('Temperature in Celsius', fontsize=24, color='purple')
        #viz_tools.set_aspect(ax)
        mesh = ax.pcolormesh(array_name,cmap=cmap)
        fig.colorbar(mesh)
        if 'png' in fname:
            dest = fname
        else:
            dest = fname + '.png'
        plt.savefig(dest)
        plt.cla()

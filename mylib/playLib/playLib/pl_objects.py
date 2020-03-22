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

    def pl_create_png(self, fname, array_name, cmap='prism', 
        xlabel='xlabel', ylabel='ylabel',
        title='TITLE', subtitle='SubTitle',
        figsize=(6,6)):
        """creates a png file

        Parameters:
            fname:   the name of the output.png file
            array
            cmap
            xlabel
            ylabel
            title
            subtitle
            figsize

        """
        

        #aspect=array_name.shape[0]/array_name.shape[1]
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        #ax.set_aspect(aspect)
        #plt.gca().invert_yaxis()
        plt.title(title, fontsize=20, color='blue')
        plt.suptitle(subtitle, fontsize=30, color='green')
        t = plt.xlabel(xlabel, fontsize=20, color='red')
        plt.ylabel(ylabel, fontsize=24, color='purple')
        mesh = ax.pcolormesh(array_name,cmap=cmap)
        fig.colorbar(mesh)
        if 'png' in fname:
            dest = fname
        else:
            dest = fname + '.png'
        plt.savefig(dest)
        plt.cla()

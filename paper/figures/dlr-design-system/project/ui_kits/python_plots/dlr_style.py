# -*- coding: utf-8 -*-
"""
Define the DLR Corporate Design for Plots. Simply import as modul.

https://intranet.dlr.de/Seiten/f1cee728-0e4b-41d3-a092-6ac48689d9fa/Inhalt/CD-Handbuch%20.aspx?itemid=6f2692a5-c119-43c4-8e34-8f15ab197b1d&containerid=d755d16b-0e19-4ea3-9c18-3a3809b386cf&vTerms=InfoAndTools&termId=3222ff2a-4932-4e61-9ab6-d67afc41fe98

Created on Fri Jul 15 15:36:56 2022
@author: wagn_ja
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%% DLR colors
'''DLR colors according to https://intranet.dlr.de/Seiten/f1cee728-0e4b-41d3-a092-6ac48689d9fa/Inhalt/Richtlinien%20zur%20visuellen%20Gestaltung%20(CD-Handbuch).aspx?itemid=d21e9728-ce84-41b0-8eae-c922107e6b11&containerid=d755d16b-0e19-4ea3-9c18-3a3809b386cf&termId=f1cee728-0e4b-41d3-a092-6ac48689d9fa&vTerms=ContentByTopic
'''
global dlr_colors
#           #blue       #yellow       #green      #gray
dlr_colors=[ "#6cb9dc",  "#f8de53",  "#cad55c",  "#b1b1b1", #bais
             "#a7d3ec",  "#fcea7a",  "#d9df78",  "#cfcfcf", #bright
             "#3b98cb",  "#f2cd51",  "#a6bf51",  "#868585", #dark
             "#d1e8fa",  "#fff8be",  "#e6eaaf",  "#ebebeb", #brighter
             "#00658b",  "#d2ae3d",  "#82a043",  "#666666"] #darker

def get_dlr_palette(n_colors=None, desat=None, as_cmap=False, offset=None):
    """
    Return a list of the dlr colors or continuous dlr colormap defining a palette.

    Parameters
    ----------
    n_colors : int, optional
        number of colors in the palette, the default will be 20 (size of dlr_colors)
    desat : float, optional
        Proportion to desaturate each color by.
    as_cmap : bool, optional
        If True, return a matplotlib.colors.Colormap.
    offset : int, ptional
        Extract only the hex values of one of the 4 DLR colors: 
            0=blue, 1=grey, 2=green, 3=yellow

    Returns
    -------
    sns.color_palette

    """
    global dlr_colors
    
    if offset is not None:
        sub_dlr_colors= get_subset(offset)
    else:
        sub_dlr_colors=dlr_colors
        
    # Set your custom color palette
    return sns.color_palette(sub_dlr_colors,n_colors,desat,as_cmap)

def get_subset(offset=0):
    """
    Extract only the hex values of one of the 4 DLR colors: 
        0=blue, 1=grey, 2=green, 3=yellow

    Parameters
    ----------
    offset : int, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    dlr_colors : TYPE
        DESCRIPTION.

    """
    global dlr_colors
    if offset < 4:
        shifted_colors=np.roll(dlr_colors,offset)
        sub_dlr_colors=shifted_colors[0::4]
    else:
        import warnings
        warnings.warn("'Only 4 different colors defined! Select offset < 4'")
        sub_dlr_colors=dlr_colors
    return sub_dlr_colors

def get_blend_palette(offset=0,n_colors=6, as_cmap=False, mulitColor=True,reverse=False):
    """
    Create any number of gradations of a dlr color between the lightest and darkest gradation
    With mulitColor=True generate a Heatmap style Palette with blue -> green -> yellow

    Parameters
    ----------
    offset : int, ptional
        Extract only the hex values of one of the 4 DLR colors: 
            0=blue, 1=grey, 2=green, 3=yellow
    n_colors : TYPE, optional
        DESCRIPTION. The default is 6.
    as_cmap : TYPE, optional
        DESCRIPTION. The default is False.
    mulitColor: bool, optinal
        generate heatmap palette with blue, green, yellow; default True

    Returns
    -------
    palette : TYPE
        DESCRIPTION.

    """
    global dlr_colors
    colors = get_subset(offset)
    if mulitColor:
                    #dark blue,   yellow
        colorList=[dlr_colors[16],dlr_colors[1]]
        if reverse:
            colorList.reverse()
        palette=sns.blend_palette(colorList,n_colors=n_colors, as_cmap=as_cmap, input='hex')

    else:
        colorList=colors[-2:]
        if reverse:
            colorList.reverse()
        palette=sns.blend_palette(colorList, n_colors=n_colors, as_cmap=as_cmap, input='hex')
    
    return palette

dlr_palette= sns.set_palette(get_dlr_palette())

#%% Adapt Paramters
dlr_params = {'axes.labelcolor': '0',
             'axes.labelsize' : '10',
             'axes.labelweight': 'light',
             'text.color': '0',
             'xtick.color': '0',
             'ytick.color': '0',
             'xtick.bottom': True,
             'xtick.top': False,
             'ytick.left': True,
             'ytick.right': False,
             'xtick.labelsize': '10',  # font size of the tick labels
             'ytick.labelsize': '10',  # font size of the tick labels
             'font.family': ['Frutiger'],
             'font.sans-serif': ['Arial'],
             'font.weight': 'light',
             'font.size': '10',
             'lines.linewidth': 2,
             'patch.edgecolor': 'w',
             "axes.spines.right" : False,
             "axes.spines.top"   : False}

sns.set_theme(context='notebook', 
              style='white', 
              palette=dlr_palette, 
              font='Frutiger', 
              font_scale=1, 
              color_codes=True, 
              rc=dlr_params)

if __name__ == '__main__':
    # Load the penguins dataset
    penguins = sns.load_dataset("penguins")
    
    # Plot sepal width as a function of sepal_length across days
    g = sns.lmplot(
        data=penguins,
        x="bill_length_mm", y="bill_depth_mm", hue="species",
        height=3.9,
        aspect=1.62
    )
    
    # Use more informative axis labels than are provided by default
    g.set_axis_labels("Snoot length (mm)", "Snoot depth (mm)")
    sns.despine(offset=5, trim=True);
    #plt.savefig('./examples/lmplot.png')
    #%%
    import pandas as pd
    f, ax = plt.subplots(1,1, figsize=(6.3, 3.9))
    rs = np.random.RandomState(365)
    values = rs.randn(365, 4).cumsum(axis=0)
    dates = pd.date_range("1 1 2016", periods=365, freq="D")
    data = pd.DataFrame(values, dates, columns=["A", "B", "C", "D"])
    data = data.rolling(7).mean()
    
    sns.lineplot(data=data, linewidth=2.5)
    sns.despine(offset=5, trim=True);
    #plt.savefig('./examples/lineplot.png')

    #%%
    # Initialize the figure with a logarithmic x axis
    f, ax = plt.subplots(figsize=(6.3, 3.9))
    ax.set_xscale("log")
    
    # Load the example planets dataset
    planets = sns.load_dataset("planets")
    
    # Plot the orbital period with horizontal boxes
    sns.boxplot(x="distance", y="method", data=planets,
                whis=[0, 100], width=.6)
    
    # Add in points to show each observation
    sns.stripplot(x="distance", y="method", data=planets,
                  size=4, color=".3", linewidth=0)
    
    # Tweak the visual presentation
    ax.xaxis.grid(True)
    ax.set(ylabel="")
    sns.despine(trim=True, left=True)
    plt.tight_layout()
    #plt.savefig('./examples/stripplot.png')
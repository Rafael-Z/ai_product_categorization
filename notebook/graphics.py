import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sunburst(nodes, hide_level=[], highlight_option=[], total=np.pi * 2, offset=0, level=0, ax=None, figsize=(10, 10), showLabel=True):
    if ax == None:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(plt.subplot(111, projection='polar'))

    if level == 0 and len(nodes) == 1:
        label, value, subnodes = nodes[0]
        ax.bar([0], [2], [np.pi * 2], color='white')
        #ax.text(0, 0, label, ha='center', va='center')
        sunburst(subnodes, hide_level, highlight_option, total=value, level=level + 1, ax=ax, showLabel=showLabel)
    elif nodes:
        d = np.pi * 2 / total
        labels = []
        widths = []
        local_offset = offset
        for label, value, subnodes in nodes:
            labels.append(label)
            widths.append(value * d)
            sunburst(subnodes, hide_level, highlight_option, total=total, offset=local_offset,
                     level=level + 1, ax=ax, showLabel=showLabel)
            local_offset += value
        if level not in hide_level:
            values = np.cumsum([offset * d] + widths[:-1])
            heights = [2] * len(nodes)
            bottoms = np.zeros(len(nodes)) + level*2
            if len(highlight_option) >= level:
                color = ['#999999']*len(values)
                if highlight_option[level-1] in labels:
                    idx = labels.index(highlight_option[level-1])
                    color[idx] = '#D07275'

                rects = ax.bar(values, heights, widths, bottoms, linewidth=1,
                               edgecolor='white', align='edge', color=color)
                if highlight_option[level-1] in labels and showLabel:
                    idx = labels.index(highlight_option[level-1])
                    x = rects[idx].get_x() + rects[idx].get_width() / 2
                    y = rects[idx].get_y() + rects[idx].get_height() / 2
                    rotation = (90 + (360 - np.degrees(x) % 180)) % 360
                    ax.text(x, y, labels[idx], rotation=rotation, ha='center', va='center', fontsize = 11) 
            else:
                rects = ax.bar(values, heights, widths, bottoms, linewidth=1,
                               edgecolor='white', align='edge')
                if showLabel:
                    for rect, label in zip(rects, labels):
                        x = rect.get_x() + rect.get_width() / 2
                        y = rect.get_y() + rect.get_height() / 2
                        rotation = (90 + (360 - np.degrees(x) % 180)) % 360
                        ax.text(x, y, label, rotation=rotation, ha='center', va='center', fontsize = 11) 

    if level == 0:
        ax.set_theta_direction(-1)
        ax.set_theta_zero_location('N')
        ax.set_axis_off()

def prepare_sunburst_data(dataframe, column_names, level=0, parent_index=None):
    data = []
    if level == 0:
        cat = dataframe.groupby(
            [column_names[level]]
        ).agg(
            {'name': 'count'}
        )
    else:
        cat = dataframe.loc[
            dataframe[column_names[level - 1]] == parent_index
        ].groupby(
            [column_names[level]]
        ).agg(
            {'name': 'count'}
        )
    for cat_index in cat.index:
        subdata = []
        if level < len(column_names) - 1:
            subdata = prepare_sunburst_data(dataframe, column_names, level+1, cat_index)
        data.append((cat_index.split('::')[-1], cat.loc[cat_index,'name'], subdata))

    if level == 0:
        data = [('root', dataframe.shape[0], data)]
    return data
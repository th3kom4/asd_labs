import collections
import math
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg') 

def plot_data(data, logarithmic=False, oneplot=False, data_2={}, 
              label_data2_label=True, 
              data_label='', data2_label='', 
              legend_pos=0, legend2_pos=0, 
              show_markers=True,
              x_axis_label='Input size (log10)',
              y_axis_label='Comparisons (log10)'):
    
    fig = plt.figure() 
    
    num = 0
    
    if oneplot:
        num = 1
        if len(data_2) > 0:
            num += 1
    else:
        num = len(data)
        if len(data_2) > 0:
            num += 1
            
    colors = ['r','b','g','c','m','y']
    markers = ['s','o','x','^','v','<','>']
    lines = ['-', '--', '-.', ':'] 

    ax = fig.add_subplot(num, 1, 1)
    ax.grid(True)
    if data_label:
        ax.set_title(data_label)

    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)

    i = -1
    line_titles = []
    x_max = y_max = 0
    
    for label, points in data.items():
        i += 1
        od_points = collections.OrderedDict(sorted(points.items()))
        
        if logarithmic:
            xs = [math.log(x, 10) if x > 0 else 0 for x in od_points.keys()]
            ys = [math.log(y, 10) if y > 0 else 0 for y in od_points.values()]
        else:
            xs = list(od_points.keys())
            ys = list(od_points.values())
            
        xs.insert(0, 0)
        ys.insert(0, 0)
        
        if xs: x_max = max(x_max, max(xs))
        if ys: y_max = max(y_max, max(ys))
        
        style = colors[i % len(colors)] + '-'
        if show_markers:
            style += markers[i % len(markers)]
            
        ax.plot(xs, ys, style, label=label)
        line_titles.append(label)
        
    ax.set_xlim((0, x_max * 1.1))
    ax.set_ylim((0, y_max * 1.1))
    ax.legend(line_titles, loc=legend_pos)

    if len(data_2) > 0:
        ax = fig.add_subplot(num, 1, num)
        ax.grid(True)
        if data2_label:
            ax.set_title(data2_label)
            
        i = -1
        line_titles = []
        x_max = y_max = 0
        
        for label, value in data_2.items():
            i += 1
            j = -1
            
            for name, points in value.items():
                j += 1
                od_points = collections.OrderedDict(sorted(points.items()))
                
                if logarithmic:
                    xs = [math.log(x, 10) if x > 0 else 0 for x in od_points.keys()]
                    ys = [math.log(y, 10) if y > 0 else 0 for y in od_points.values()]
                else:
                    xs = list(od_points.keys())
                    ys = list(od_points.values())
                    
                xs.insert(0, 0)
                ys.insert(0, 0)
                
                if xs: x_max = max(x_max, max(xs))
                if ys: y_max = max(y_max, max(ys))
                
                current_line = lines[i % len(lines)]
                style = colors[j % len(colors)] + current_line
                if show_markers:
                    style += markers[j % len(markers)]
                    
                ax.plot(xs, ys, style)
                
                if label_data2_label:
                    line_titles.append(name + ' ' + label)
                else:
                    line_titles.append(name)
                    
        ax.set_xlim((0, x_max * 1.1))
        ax.set_ylim((0, y_max * 1.1))
        ax.legend(line_titles, loc=legend2_pos)

    print("Graph generated...")
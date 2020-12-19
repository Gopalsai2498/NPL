# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 05:12:52 2020

@author: anil.ms
"""

import numpy as np
from bokeh.plotting import figure, show

#line plot
from bokeh.models import HoverTool

x_line = np.arange(10)
y_line = np.random.rand(10)

#define plot size,title, x_axis & y_axis
line_plot= figure(plot_width=500, plot_height=325, title='Line Plot', x_axis_label = 'x', y_axis_label='y')

#assign x, y data to required plot
line_plot.line(x_line, y_line, legend_label='line', line_width=2)

#add hover
line_plot.add_tools(HoverTool())

#display plot
show(line_plot)
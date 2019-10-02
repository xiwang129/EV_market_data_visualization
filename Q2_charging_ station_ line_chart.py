
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
from pandas import read_csv
from bokeh.models import ColumnDataSource,CustomJS,HoverTool,CDSView,CategoricalColorMapper, Legend
from bokeh.io import output_file,show
from bokeh.plotting import figure,gmap, show
from bokeh.io import curdoc
from bokeh.layouts import gridplot, widgetbox,column
from bokeh.models.widgets import Slider, Select
from bokeh.palettes import Spectral6


x = [2013,2014,2015,2016,2017]
y_ca=[127,127,306,324,238]
y_ny=[15,37,35,189,124]
y_fl=[23,21,59,100,113]
y_tx=[8,7,44,94,77]

y_ca2=[26,48,73,36,51]
y_ny2=[1,4,1,5,0]
y_fl2=[22,11,18,2,1]
y_tx2=[4,4,2,4,0]


p = figure(plot_width=900, plot_height=400, title='US Public/Private EV Charging Sations By State')

r0=p.line(x, y_ca , line_width=2, line_color='#DD4968')
r1=p.line(x,y_ny , line_width=2,line_color='blue')
r2=p.line(x,y_fl , line_width=2,line_color='#35B778')
r3=p.line(x,y_tx, line_width=2,line_color='#FDE724')


r4=p.line(x, y_ca2 , line_width=2, line_color='#410967')
r5=p.line(x,y_ny2 , line_width=2,line_color='#932567')
r6=p.line(x,y_fl2 , line_width=2,line_color='#DC5039')
r7=p.line(x,y_tx2, line_width=2,line_color='#FBA40A')

p.xaxis.axis_label = "Year"
p.yaxis.axis_label = "Number of Stations"

legend = Legend(items=[('CA',[r0]),('NY',[r1]),('FL',[r2]),('TX',[r3]),
                    ('CA pri',[r4]),('NY pri',[r5]),('FL pri',[r6]),('TX pri',[r7])], location=(15, 0))
p.add_layout(legend, 'right')
p.legend.click_policy="hide"

curdoc().add_root(p) 
curdoc().title = "US EV Stations"

show(p)


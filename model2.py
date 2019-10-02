
# coding: utf-8

# In[7]:


import pandas as pd
from pandas import read_csv
from bokeh.models import ColumnDataSource,CustomJS,HoverTool,CDSView,CategoricalColorMapper
from bokeh.io import output_file,show
from bokeh.plotting import figure,gmap
from bokeh.io import curdoc
from bokeh.layouts import gridplot, widgetbox,column
from bokeh.transform import dodge
from bokeh.core.properties import value
from bokeh.models.widgets import Select,MultiSelect


model = ['Nissan LEAF', 'Chevrolet Volt PHEV', 'Tesla Model S', 'Toyota Prius Prime Plug-in']
#time = ['2012','2013','2014','2015','2016']

time=dict('2012' = [9819,23461,2171,12749],
        '2013'   = [22610,23094,19000,12088],
        '2014'   = [30200,18805,16750,13264],
        '2015'   = [17269,15393,26200,4191],
        '2016'   = [14006,24739,29156,2474])

data = {'model' : model,
        'time':time}

source=ColumnDataSource(data)

p = figure(x_range= model, y_range=(2000, 30200), plot_height=350, title="US EV Sales by Model Type",
           toolbar_location=None, tools="")

p.vbar(x=dodge('model', -0.25, range=p.x_range), top='2012', width=0.2, source=source,
       color="#e84d60", legend=value("2012"))

p.vbar(x=dodge('model',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,
       color="#718dbf", legend=value("2016"))


p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
                                            
multi_select = MultiSelect(title="Year Option:", value=['2012', '2016'],
                           options=[('2012','2012'), ('2013', '2013'), ('2014','2014'), ('2015','2015'),('2016','2016')])


def new_plot(attr, old, new):
    filtered = data[data['time'] == multi_select.value]
    source.data={
        'model' : model,
        '2012'   : filtered[9819,23461,2171,12749],
        '2013'   : filtered[22610,23094,19000,12088],
        '2014'   : filtered[30200,18805,16750,13264],
        '2015'   : filteredfiltered[17269,15393,26200,4191],
        '2016'   : filtered[14006,24739,29156,2474],}

controls=[multi_select]
for control in controls:
    control.on_change('value', new_plot)
    

grid = gridplot([multi_select, p], ncols=2, plot_width=600, plot_height=400)

curdoc().add_root(grid) 
curdoc().title = "EV Model"

show(p)



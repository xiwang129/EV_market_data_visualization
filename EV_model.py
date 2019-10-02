
# coding: utf-8

# In[1]:


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


model = ['Nissan LEAF', 'Chevrolet Volt', 'Tesla Model S', 'Toyota Prius Prime','Ford Fusion']
time = ['2012','2013','2014','2015','2016']

df=pd.DataFrame(data={
        'model' : model,
        'time': time,
        '2012' : [9819,23461,2171,12749,0],
        '2013'   : [22610,23094,19000,12088,6089],
        '2014'   : [30200,18805,16750,13264,11550],
        '2015'   : [17269,15393,26200,4191,9750],
        '2016'   : [14006,24739,29156,2474,15928]
    })

source=ColumnDataSource(df)

tools = ["pan", "reset",'zoom_in','zoom_out']
p = figure(x_range= model, y_range=(2000, 30200), plot_height=350, title="US EV Sales by Model Type",
           toolbar_location=None, tools=tools)

p.vbar(x=dodge('model', -0.25, range=p.x_range), top='2012', width=0.2, source=source,
       color="#e84d60", legend=value("2012"))

p.vbar(x=dodge('model',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,
       color="#718dbf", legend=value("2016"))
                                           

multi_select = MultiSelect(title=" Select multiple years:", width=200, value=['2012', '2016'],
                           options=[('2012','2012'), ('2013', '2013'), ('2014','2014'), ('2015','2015'),('2016','2016')])

def callback (attr, old, new):
    df2 = df[df.time.isin(multi_select.value)]
    source.data = source.from_df(df2) 

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"  
       
controls=[multi_select]
for control in controls:
    control.on_change('value', callback)
    
grid = gridplot([multi_select, p], ncols=2, plot_width=600, plot_height=400)

curdoc().add_root(grid) 
curdoc().title = "EV Model"

show(p)



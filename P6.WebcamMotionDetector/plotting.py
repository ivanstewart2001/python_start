from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%Ss")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%Ss")

cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime', height=100, width=500,title="Motion Graph")
p.yaxis.major_tick_line_alpha=0
p.yaxis[0].ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start","@Start_string"), ("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

output_file("Graph.html")
show(p)
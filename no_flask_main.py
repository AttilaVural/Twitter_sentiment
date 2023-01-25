# copied from https://docs.bokeh.org/en/latest/docs/user_guide/server/app.html
from bokeh.plotting import figure, curdoc
from bokeh.models import DatetimeTickFormatter
import snscrape_test as sn
    
p = figure(height=350, width=1500, x_axis_type="datetime")

df = sn.sentiment("test", 3)

print(df)

p.circle(
    df['date'],
    df['com_score'],
    size=20,
    color="navy",
    alpha=0.5
)

# Format the axis to show dates properly
p.xaxis.formatter = DatetimeTickFormatter(years="%d/%m/%Y %H:%M:%S",
                                          months="%d/%m/%Y %H:%M:%S",
                                          days="%d/%m/%Y %H:%M:%S",
                                          hours="%d/%m/%Y %H:%M:%S",
                                          hourmin="%d/%m/%Y %H:%M:%S",
                                          minutes="%d/%m/%Y %H:%M:%S",
                                          minsec="%d/%m/%Y %H:%M:%S",
                                          seconds="%d/%m/%Y %H:%M:%S",
                                          milliseconds="%d/%m/%Y %H:%M:%S",
                                          microseconds="%d/%m/%Y %H:%M:%S")

# put the button and plot in a layout and add to the document
curdoc().add_root(p)
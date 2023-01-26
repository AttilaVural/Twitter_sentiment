# copied from https://docs.bokeh.org/en/latest/docs/user_guide/server/app.html
from bokeh.plotting import figure, curdoc
from bokeh.models import DatetimeTickFormatter, RELATIVE_DATETIME_CONTEXT
import snscrape_test as sn
import pandas as pd
    
p = figure(height=350, width=1500, x_axis_type="datetime")

df = sn.sentiment("brøndby if", 100)

# becomes a pandas series type
#df = df.groupby(df.date.dt.day)['com_score'].mean()
df = df.groupby(df.date.dt.to_period('D'))['com_score'].mean()

# Convert back to a pandas dataframe
df = pd.DataFrame({'date':df.index, 'com_score':df.values})

print(df)

p.circle(
    df['date'],
    df['com_score'],
    size=20,
    color="navy",
    alpha=0.5
)
p.line(
    df['date'],
    df['com_score']
)

# Format the axis to show dates properly
p.xaxis.formatter.context = RELATIVE_DATETIME_CONTEXT()
# p.xaxis.formatter = DatetimeTickFormatter(years="%d/%m/%Y %H:%M:%S",
                                          # months="%d/%m/%Y %H:%M:%S",
                                          # days="%d/%m/%Y %H:%M:%S",
                                          # hours="%d/%m/%Y %H:%M:%S",
                                          # hourmin="%d/%m/%Y %H:%M:%S",
                                          # minutes="%d/%m/%Y %H:%M:%S",
                                          # minsec="%d/%m/%Y %H:%M:%S",
                                          # seconds="%d/%m/%Y %H:%M:%S",
                                          # milliseconds="%d/%m/%Y %H:%M:%S",
                                          # microseconds="%d/%m/%Y %H:%M:%S")

# put the button and plot in a layout and add to the document
curdoc().add_root(p)
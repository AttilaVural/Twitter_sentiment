# copied from https://docs.bokeh.org/en/latest/docs/user_guide/server/app.html
from bokeh.plotting import figure, curdoc
import snscrape_test as sn
    
p = figure(height=350, width=500)

scores = sn.sentiment("test", 10)
p.circle(
    [i for i in range(len(scores))],
    [scores[j] for j in range(len(scores))],
    size=20,
    color="navy",
    alpha=0.5
)

# put the button and plot in a layout and add to the document
curdoc().add_root(p)
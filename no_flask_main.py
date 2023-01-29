# copied from https://docs.bokeh.org/en/latest/docs/user_guide/server/app.html
from bokeh.plotting import figure, curdoc
from bokeh.models import DatetimeTickFormatter, RELATIVE_DATETIME_CONTEXT
import snscrape_test as sn
import pandas as pd
from bokeh.models import Button, TextInput, ColumnDataSource, NumericInput
from bokeh.layouts import column
import pymongo
from datetime import datetime, timedelta
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
mydb = myclient["mydatabase"]
mycol = mydb["records"]

p = figure(height=350, width=1500, x_axis_type="datetime")
source = ColumnDataSource({})
p.circle(
    x="date",
    y="com_score",
    source=source,
    size=20,
    color="navy",
    alpha=0.5
)
p.line(x="date", y="com_score", source=source)

# Format the axis to show dates properly
p.xaxis.formatter.context = RELATIVE_DATETIME_CONTEXT()

# create a callback that saves the data
def save_records():
    document_count = mycol.count_documents({})
    print("Documents before insertion", document_count)
    x = mycol.insert_many(raw_df.to_dict(orient='records'))
    document_count = mycol.count_documents({})
    print("Documents after insertion", document_count)
    
    # print("The following data has been saved:")
    # for x in mycol.find():
        # print(x)
    #mycol.delete_many({'name': 'Peter'})
    
def get_records():
    # Remove previous glyphs
    # p.renderers = [] ### gammel måde
    # Scrape data
    

    # Virker pt som den originale kode, men når du fjerne udkommenteringen ved "search_string" giver den fejl
    yesterday = datetime.now() - timedelta(10)  
    search_string = text_input.value# + " since:" + datetime.strftime(yesterday, '%Y-%m-%d') + " until:" + datetime.strftime(yesterday, '%Y-%m-%d')
    search_string = "data science since:2023-01-01 until:2023-01-05"
    search_string = text_input.value + " " + since_date.value + " " + until_date.value
    print(search_string)
    global raw_df
    raw_df = sn.sentiment(search_string, max_entries.value)
    print(raw_df)
    # for i in range(30):
        # yesterday = datetime.now() - timedelta(i)  
        # search_string = text_input.value + "since:" + datetime.strftime(yesterday, '%Y-%m-%d')
        # print(search_string)
        # temp = sn.sentiment(search_string, 100)
        # pd.concat([raw_df, temp])
        
    if raw_df.empty == False:
        # Group by date: day. This converts it from a dataframe to a series
        df = raw_df.groupby(raw_df.date.dt.to_period('D'))['com_score'].mean()
        # Convert back to a pandas dataframe
        df = pd.DataFrame({'date':df.index, 'com_score':df.values})
        
        print("Input field value:", text_input.value)
        print("df.size: ", df.size)
        print("len():", len(df))
        print(df)
        
        # replace all data in an existing ColumnDataSource
        source.data = df
        

# add a button widget and configure with the call back
save_button = Button(label="Save data")
save_button.on_event('button_click', save_records)

search_button = Button(label="Get data")
search_button.on_event('button_click', get_records)

text_input = TextInput(value="default", title="Search string:")
max_entries = NumericInput(value=1, low=1, high=10, title="Total tweets to retrieve (1-10):")
since_date = TextInput(value="since:2023-01-01", title="Since:")
until_date = TextInput(value="until:2023-01-10", title="Until:")

# put the button and plot in a layout and add to the document
curdoc().add_root(column(save_button, search_button, text_input, max_entries, since_date, until_date, p))
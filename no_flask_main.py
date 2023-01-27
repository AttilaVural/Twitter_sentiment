# copied from https://docs.bokeh.org/en/latest/docs/user_guide/server/app.html
from bokeh.plotting import figure, curdoc
from bokeh.models import DatetimeTickFormatter, RELATIVE_DATETIME_CONTEXT
import snscrape_test as sn
import pandas as pd
from bokeh.models import Button, TextInput, ColumnDataSource
from bokeh.layouts import column
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.list_database_names()
mydb = myclient["mydatabase"]
mycol = mydb["records"]
from datetime import datetime, timedelta


p = figure(height=350, width=1500, x_axis_type="datetime")

p.circle(
    [],
    [],
    size=20,
    color="navy",
    alpha=0.5
)
p.line(
    [],
    []
)

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
    p.renderers = []
    # Scrape data
    
    ###################################################
    ########## Eksperimentiel kode ####################
    ###################################################
    # Virker pt som den originale kode, men når du fjerne udkommenteringen ved "search_string" giver den fejl
    yesterday = datetime.now() - timedelta(10)  
    search_string = text_input.value# + " since:" + datetime.strftime(yesterday, '%Y-%m-%d') + " until:" + datetime.strftime(yesterday, '%Y-%m-%d')
    print(search_string)
    raw_df = sn.sentiment(search_string, 100)
    print(raw_df)
    # for i in range(30):
        # yesterday = datetime.now() - timedelta(i)  
        # search_string = text_input.value + "since:" + datetime.strftime(yesterday, '%Y-%m-%d')
        # print(search_string)
        # temp = sn.sentiment(search_string, 100)
        # pd.concat([raw_df, temp])
        
    ################################################### 
    ###################################################
    ################################################### 
    
    #############################################################
    ######### Udkommenteret original kode: ######################
    #############################################################
    # raw_df = sn.sentiment(text_input.value, 100)
    #############################################################
    #############################################################
    #############################################################
    
    # Group by date: day. This converts it from a dataframe to a series
    df = raw_df.groupby(raw_df.date.dt.to_period('D'))['com_score'].mean()
    # Convert back to a pandas dataframe
    df = pd.DataFrame({'date':df.index, 'com_score':df.values})
    
    print("Input field value:", text_input.value)
    print("df.size: ", df.size)
    print("len():", len(df))
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
    

# add a button widget and configure with the call back
save_button = Button(label="Save data")
save_button.on_event('button_click', save_records)

search_button = Button(label="Get data")
search_button.on_event('button_click', get_records)

text_input = TextInput(value="default", title="Label:")

# put the button and plot in a layout and add to the document
curdoc().add_root(column(save_button, search_button, text_input, p))
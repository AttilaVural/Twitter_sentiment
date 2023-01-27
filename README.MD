Bare noter til post artiklen:


I have the following steps to take whenever i start coding. Is this a CI-CD flow?

> git clone ....

> cd ....

> md DB_data

First start the mongoDB server:

> mongod.exe --dbpath="%cd%\DB_data"

Now open another CMD instance from this folder and start the bokeh server:

> start cmd

> python -m venv env

> .\env\scripts\activate

> pip install -r requirements.txt

> bokeh serve --show no_flask_main.py
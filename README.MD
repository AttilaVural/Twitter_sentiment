Bare noter til post artiklen:


I have the following steps to take whenever i start coding. Is this a CI-CD flow?

> git clone ....

> cd ....

> python -m venv env

> .\env\scripts\activate

> pip install -r requirements.txt

> md DB_data

> mongod.exe --dbpath="\<path to project folder\>\DB_data"

> bokeh serve --show no_flask_main.py
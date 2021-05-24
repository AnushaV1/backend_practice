## Backend-app with REST API

## Tech Stack
* ** Python, Flask, SQLAlchemy, PostgreSQL, JSON **

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `CREATEDB noyo_db`
5. `python seed.py`
6. `flask run or python app.py`

To test the application
1. `CREATEDB noyo_db_test`
2. `python -m unittest`

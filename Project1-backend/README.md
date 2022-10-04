# Installation 

1. `python3 -m venv venv`
2. `source venv/bin/activate `
3. `venv\Scripts\activate`
4. `pip install flask `
4. `pip install -U Flask-SQLAlchemy`
4. `pip install Flask-Migrate`
5. `export FLASK_APP=Project1-backend`
6. `export FLASK_ENV=development`
7. `rm Project1-backend/db.sqlite3`
7. `flask db init`
8. `flask db migrate`
9. `flask db upgrade`
10. `flask run`

# To check sqlite db
- `sqlite3 Project1-backend/db.sqlite3`
- `select * from user;`
- `.exit`
- `.tables`
- `.schema`


# TODO 
- Use [flasgger](https://github.com/flasgger/flasgger) to add swagger documentation for backend 

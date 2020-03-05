# Python Flask Record Shop

Record Store CRUD app implemented in Python with Flask, connecting to a PostgreSQL database.

Dependencies:
- Python3
  - Flask
  - psycopg2
- PostgreSQL

To install:

```
$ pip3 install psycopg2
$ pip3 install Flask
```

You will also need to create a PostgreSQL database called `record_store`:

```
$ createdb record_store
```

To set up the tables:

```
$ psql -d record_store -f ./db/record_store.sql
```

To run the app:
```
$ python3 app.py
```

To see the app running in a web browser, go to [http://localhost:5000/](http://localhost:5000).

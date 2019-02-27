# poc-python-flask-backend

A basic flask app that has one route which accepts an
sql query. 

That query is proxied to the database and the result is returned.

## Up and Running

1. Install flask
2. Install dependencies in venv
3. python run-server.py


## API

Query: `/query/<your_query_string_here>`

example: `curl http://127.0.0.1:5000/query/SELECT%20*%20FROM%20user_details`

Response:

Either you receive an array o users, or an error object, which returns the sql error.

*Error*
```json
{
    "error": "(pymysql.err.ProgrammingError) (1064, u\"You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '' at line 1\") [SQL: u'SELECT'] (Background on this error at: http://sqlalche.me/e/f405)"
}
```

*Success*
```json
[
    {
        "first_name": "david",
        "gender": "Female",
        "last_name": "john",
        "password": "e6a33eee180b07e563d74fee8c2c66b8",
        "status": 1,
        "user_id": 1,
        "username": "rogers63"
    },
    {
        "first_name": "rogers",
        "gender": "Male",
        "last_name": "paul",
        "password": "2e7dc6b8a1598f4f75c3eaa47958ee2f",
        "status": 1,
        "user_id": 2,
        "username": "mike28"
    }
]
```
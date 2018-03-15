# MySQL Errors

## Config Dict from MySQLConnection Class

```python
config = {
    'host': 'localhost',
    'database': db,
    'user': 'root',
    'password': 'root',
    'port': '3306',
}
```

### MISSING or WRONG USER NAME or PASSWORD

```python
OperationalError: (_mysql_exceptions.OperationalError) (1045, "Access denied for user 'lawerencelee'@'localhost' (using password: YES)") (Background on this error at: http://sqlalche.me/e/e3q8)
```

### WRONG PORT NUMBER

```python
OperationalError: (_mysql_exceptions.OperationalError) (2003, "Can't connect to MySQL server on '127.0.0.1' (61)") (Background on this error at: http://sqlalche.me/e/e3q8)
```

### BAD DATABASE NAME

```python
OperationalError: (_mysql_exceptions.OperationalError) (1049, "Unknown database 'frienddb'") (Background on this error at: http://sqlalche.me/e/e3q8)
```
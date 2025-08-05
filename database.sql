#user info
mysql> CREATE TABLE Users (
    -> user_id INTEGER PRIMARY KEY,
    -> name VARCHAR(20) NOT NULL,
    -> phone INTEGER UNIQUE NOT NULL
    -> );
Query OK, 0 rows affected (0.09 sec)

#menu to order from
mysql> CREATE TABLE Menu (
    -> item_id INTEGER PRIMARY KEY,
    -> item_name VARCHAR(50) NOT NULL,
    -> price INTEGER NOT NULL
    -> );
Query OK, 0 rows affected (0.02 sec)

#orders placed
mysql> CREATE TABLE Orders (
    -> order_id INTEGER PRIMARY KEY,
    -> user_id INTEGER,
    -> item_id INTEGER,
    -> quantity INTEGER
    -> );
Query OK, 0 rows affected (0.02 sec)
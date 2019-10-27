import psycopg2 as dbapi2
from db import db_url as url


def createUser(name, password):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO USERS (NAME, PASSWORD) VALUES (%s, %s)"""
            cursor.execute(statement, (name, password))
            connection.commit()

def createList(name, date, userid):
    with dbapi2.connect(url) as connection:
        with connection.cursor() as cursor:
            statement = """INSERT INTO LIST (NAME, DATE, USERID) VALUES (%s, %s, %s)"""
            cursor.execute(statement, (name, date, userid))
            connection.commit()
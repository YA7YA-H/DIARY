import psycopg2
import pprint as pp


class DatabaseConnection:
    """Database connection"""

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='mydiarydb' user='hassan' host='localhost' password='andela' port='5432'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pp.pprint("SORRY cannot connect to database")

    def create_tables_user(self):
        try:
            user_table = """CREATE TABLE users(
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(100) NOT NULL,
            lastname VARCHAR(100) NOT NULL,
            email VARCHAR(100)UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL
        )"""
            self.cursor.execute(user_table)
        except (Exception, psycopg2.DatabaseError) as e:
            pp.pprint(e)

    def create_tables_entry(self):
        try:
            entry_table = """CREATE TABLE entries(
            id SERIAL PRIMARY KEY,
            date VARCHAR(100) NOT NULL,
            content VARCHAR(200) NOT NULL
        )"""
            self.cursor.execute(entry_table)
        except (Exception, psycopg2.DatabaseError) as e:
            pp.pprint(e)

    def add_new_user(self, firstname, lastname, email, password):
        try:
            self.cursor.execute(
                "INSERT INTO users(firstname,lastname, email, password) VALUES(%s,%s,%s,%s)",
                (firstname, lastname, email, password))
        except (Exception, psycopg2.IntegrityError) as error:
            pp.pprint(error)

    def add_new_entry(self, date, content):
        try:
            self.cursor.execute(
                "INSERT INTO entries(date,content) VALUES(%s,%s)",
                (date, content))
        except (Exception, psycopg2.IntegrityError) as error:
            pp.pprint(error)

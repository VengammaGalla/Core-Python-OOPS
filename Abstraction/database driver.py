from abc import ABC, abstractmethod
class DatabaseDriver(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def close(self):
        pass

class MySQLDriver(DatabaseDriver):

    def connect(self):
        print("Connected to MySQL")

    def execute(self, query):
        print("MySQL executing:", query)

    def close(self):
        print("MySQL connection closed")

class PostgresDriver(DatabaseDriver):

    def connect(self):
        print("Connected to PostgreSQL")

    def execute(self, query):
        print("PostgreSQL executing:", query)

    def close(self):
        print("PostgreSQL connection closed")

class SQLiteDriver(DatabaseDriver):

    def connect(self):
        print("Connected to SQLite")

    def execute(self, query):
        print("SQLite executing:", query)

    def close(self):
        print("SQLite connection closed")


# Main code
def use_database(database):
    database.connect()
    database.execute("SELECT * FROM employees")
    database.close()

# MySQL
db = MySQLDriver()
use_database(db)

print()

# PostgreSQL
db = PostgresDriver()
use_database(db)

print()

# SQLite
db = SQLiteDriver()
use_database(db)
import pymysql
import config

class DBManager:
    def __init__(self):
        pass

    def connect(self, host, user, password, db_name):
        try:
            db = pymysql.connect(
                host = host,
                user = user,
                password = password,
                db = db_name
            )
            return db
        except Exception:
            print("Error cannot connect to database: " + e)
        
    def execute_query(self, db, query):
        with db:
            cursor = db.cursor()
            try:
                cursor.execute(pymysql.escape_string(query))
                return cursor.fetchall()
            except Exception:
                raise Exception(f"Failed to execute query {query}")

db_manager = DBManager()
db = db_manager.connect(
    config.db_host, 
    config.db_user, 
    config.db_password, 
    config.db_name
)

query = "SELECT * FROM people"
people = db_manager.execute_query(db, query)
print(people)
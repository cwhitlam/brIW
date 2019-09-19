import pymysql

class DBConnector:
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
            print("Error cannot connect to database")
        
    def execute_query(self, db, query):
        with db:
            cursor = db.cursor()
            try:
                cursor.execute(pymysql.escape_string(query))
                return cursor.fetchall()
            except Exception:
                raise Exception(f"Failed to execute query {query}")
            

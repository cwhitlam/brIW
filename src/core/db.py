import pymysql
import src.core.config as config

def get_db_connection():
    try:
        return pymysql.connect(
            host = config.db_host,
            user = config.db_user,
            password = config.db_password,
            db = config.db_name
        )
    except Exception as e:
        print("Error cannot connect to database: " + e)

def fetch_all_from_db(query):
    connection = get_db_connection()
    #query = pymysql.escape_string(query)
    #query = query.strip('\n')
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print (e)
        return []
    finally:
        connection.close()
        
def get_all_people():
    query = """
                SELECT 
                    pe.person_id,
                    pe.first_name,
                    pe.surname,
                    d.drink_id,
                    d.name AS drink_name
                FROM people AS pe
                LEFT JOIN preferences AS pr ON pe.person_id=pr.person_id
                LEFT JOIN drinks AS d ON pr.drink_id=d.drink_id
            """
    return fetch_all_from_db(query)

def get_all_drinks():
    query = """
                SELECT 
                    drink_id,
                    name 
                FROM drinks
            """
    return fetch_all_from_db(query)
   
    
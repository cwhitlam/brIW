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
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print (e)
        return []
    finally:
        connection.close()

def execute_query(query):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print (e)
        return
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
                FROM tbl_people AS pe
                LEFT JOIN tbl_drinks AS d ON pe.preferred_drink_id=d.drink_id
            """
    return fetch_all_from_db(query)

def get_all_drinks():
    query = """
                SELECT 
                    drink_id,
                    name 
                FROM tbl_drinks
            """
    return fetch_all_from_db(query)

def add_new_person(first_name, surname, preferred_drink_id):

    if (preferred_drink_id == None):
        preferred_drink_id = "NULL"

    query = f"""
        INSERT INTO tbl_people (first_name, surname, preferred_drink_id)
        VALUES ('{first_name}','{surname}', {preferred_drink_id})
    """
    execute_query(query)
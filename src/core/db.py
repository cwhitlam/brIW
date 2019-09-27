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

def fetch_one_from_db(query):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchone()
    except Exception as e:
        print (e)
        return []
    finally:
        connection.close()

def execute_query(query, hold_commit = False):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if not hold_commit:
            connection.commit()
    except Exception as e:
        print (e)
        return
    finally:
        connection.close()
        return cursor.lastrowid
       

def get_all_people():
    query = """
                SELECT 
                    pe.person_id,
                    pe.first_name,
                    pe.surname,
                    d.drink_id,
                    d.name AS drink_name
                FROM 
                    tbl_people AS pe
                LEFT JOIN 
                    tbl_drinks AS d ON pe.preferred_drink_id=d.drink_id
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

def add_new_drink(drink_name):
    query = f"""
        INSERT INTO tbl_drinks (name)
        VALUES ('{drink_name}')
    """
    execute_query(query)

def update_drink_preference(person_id, drink_id):
    query = f"""
        UPDATE tbl_people SET preferred_drink_id = {drink_id} 
        WHERE person_id={person_id}
    """
    execute_query(query)

def get_person_by_id(person_id):
    query = f"""
        SELECT
            p.preferred_drink_id,
            d.name AS drink_name,
            p.first_name,
            p.surname,
            p.person_id
        FROM
            tbl_people AS p
        LEFT JOIN
            tbl_drinks AS d ON d.drink_id=p.preferred_drink_id
        WHERE
            p.person_id = {person_id}
    """
    return fetch_one_from_db(query)

def get_drink_by_id(drink_id):
    query = f"""
        SELECT
            d.drink_id,
            d.name AS drink_name
        FROM
            tbl_drinks AS d
        WHERE
            d.drink_id = {drink_id}
    """
    return fetch_one_from_db(query)

def create_round_with_orders(round):
    query = f"""
        INSERT INTO 
            tbl_rounds(maker_id, created_datetime, expiry_datetime)
        VALUES 
            ({round.maker.id}, NOW(), NOW() + INTERVAL {round.minutes_remaining} MINUTE)

    """
    round_id = execute_query(query)
    print(round_id)
    create_orders(round.orders, round_id)
    
def create_orders(orders, round_id):
    all_orders_string = ""
    for index in range(0,len(orders)):
        order = orders[index]
        order_string = f"({round_id}, {order.person.id}, {order.drink.id})"
        if index < len(orders)-1:
            order_string += ","
        all_orders_string += order_string

    query = f"""
        INSERT INTO 
            tbl_orders(round_id, person_id, drink_id)
        VALUES
            {all_orders_string}
    """
    execute_query(query)

def get_current_round():
    query = f"""
        SELECT 
            r.maker_id,
            r.round_id,
            p.first_name,
            p.surname,
            r.expiry_datetime,
            TIMESTAMPDIFF(MINUTE, NOW(), r.expiry_datetime) AS minutes_remaining
        FROM
            tbl_rounds AS r 
        INNER JOIN
            tbl_people AS p ON p.person_id=r.maker_id
        WHERE
            (NOW() < r.expiry_datetime)     
    """
    return fetch_one_from_db(query)

def get_orders_by_round_id(round_id):
    query = f"""
        SELECT 
            o.person_id,
            p.first_name,
            p.surname,
            o.drink_id,
            d.name AS drink_name
        FROM 
            tbl_orders AS o
        INNER JOIN
            tbl_people AS p ON o.person_id=p.person_id
        INNER JOIN
            tbl_drinks AS d ON o.drink_id = d.drink_id 
        WHERE
            o.round_id = {round_id}
    """

    return fetch_all_from_db(query)
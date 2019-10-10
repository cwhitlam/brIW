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

def fetch_all_from_db(query, parameters = None):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, parameters)
        return cursor.fetchall()
    except Exception as e:
        print (e)
        return []
    finally:
        connection.close()

def fetch_one_from_db(query, parameters = None):
    connection = get_db_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query, parameters)
        return cursor.fetchone()
    except Exception as e:
        print (e)
        return []
    finally:
        connection.close()

def execute_query(query, parameters = None, hold_commit = False):
    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameters)
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
                    CONCAT(pe.first_name, ' ', pe.surname) AS full_name,
                    d.drink_id,
                    d.name AS drink_name
                FROM 
                    tbl_people AS pe
                LEFT JOIN 
                    tbl_drinks AS d ON pe.preferred_drink_id=d.drink_id
                ORDER BY
                    pe.person_id ASC
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

    query = f"""
        INSERT INTO tbl_people (first_name, surname, preferred_drink_id)
        VALUES (%s, %s, %s)
    """
    paramaters = (first_name.capitalize(), surname.capitalize(), preferred_drink_id)
    execute_query(query, paramaters)

def add_new_drink(drink_name):
    query = f"""
        INSERT INTO tbl_drinks (name)
        VALUES (%s)
    """

    parameters = (drink_name.capitalize())
    execute_query(query, parameters)

def update_drink_preference(person_id, drink_id):
    query = f"""
        UPDATE tbl_people SET preferred_drink_id = %s 
        WHERE person_id = %s
    """
    parameters = (drink_id, person_id)
    execute_query(query, parameters)

def get_drink_preference_by_person_id(person_id):
    query = f"""
        SELECT
            d.drink_id,
            d.name AS drink_name
        FROM
            tbl_drinks AS d
        INNER JOIN
            tbl_people AS p ON d.drink_id=p.preferred_drink_id
        WHERE
            p.person_id = %s
    """
    parameters = (person_id)
    return fetch_one_from_db(query, parameters)

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
            p.person_id = %s
    """
    parameters = (person_id)
    return fetch_one_from_db(query, parameters)

def get_drink_by_id(drink_id):
    query = f"""
        SELECT
            d.drink_id,
            d.name AS drink_name
        FROM
            tbl_drinks AS d
        WHERE
            d.drink_id = %s
    """
    parameters = (drink_id)
    return fetch_one_from_db(query, parameters)

def create_round(maker_id, round_duration):
    query = f"""
        INSERT INTO
            tbl_rounds(maker_id, created_datetime, expiry_datetime)
        VALUES
            (%s, NOW(), NOW() + INTERVAL %s MINUTE)
    """
    parameters = (maker_id, round_duration)
    execute_query(query, parameters)

def add_order_to_round(round_id, person_id, drink_id, special_requests):
    if (special_requests == None):
        special_requests = ""
    
    query = f"""
        INSERT INTO
            tbl_orders (round_id, person_id, drink_id, special_requests)
        VALUES
            (%s, %s, %s, %s)
    """
    parameters = (round_id, person_id, drink_id, special_requests)
    execute_query(query, parameters)

def get_num_of_orders_for_round(round_id):
    query = f"""
        SELECT 
            COUNT(*) AS num_of_orders
        FROM
            tbl_orders as o
        WHERE
            (o.round_id = %s)
    """
    parameters = (round_id)
    result = fetch_one_from_db(query, parameters)
    if result == []:
        return 0
    return result["num_of_orders"]

def get_current_rounds():
    query = f"""
        SELECT 
            p.person_id AS maker_id,
            p.first_name,
            p.surname,
            d.name AS drink_name,
            d.drink_id,
            CONCAT(p.first_name, ' ' , p.surname) AS maker_fullname,
            r.round_id,
            DATE_ADD(r.expiry_datetime, INTERVAL 1 HOUR) AS expiry_datetime,
            TIMESTAMPDIFF(MINUTE, NOW(), r.expiry_datetime) AS minutes_remaining
        FROM
            tbl_rounds as r 
        INNER JOIN
            tbl_people as p ON p.person_id=r.maker_id
        LEFT JOIN
            tbl_drinks as d ON p.preferred_drink_id=d.drink_id
        WHERE
            r.expiry_datetime > NOW()
    """
    result = fetch_all_from_db(query)
    
    for index in range(0, len(result)):
        round = result[index]
        round["num_of_orders"] = get_num_of_orders_for_round(int(round["round_id"]))
        result[index] = round 

    if result == None:
        return []
    return result   

def get_past_rounds(num_of_rounds):
    query = f"""
        SELECT 
            CONCAT(p.first_name, ' ' , p.surname) AS maker_fullname,
            r.round_id,
            DATE_ADD(r.expiry_datetime, INTERVAL 1 HOUR) AS expiry_datetime,
            TIMESTAMPDIFF(MINUTE, NOW(), r.expiry_datetime) AS minutes_remaining
        FROM
            tbl_rounds as r 
        INNER JOIN
            tbl_people as p on p.person_id=r.maker_id
        WHERE
            r.expiry_datetime < NOW()
        ORDER BY
            r.expiry_datetime DESC
        LIMIT %s
    """
    parameters = (int(num_of_rounds))
    result = fetch_all_from_db(query, parameters)
    
    for index in range(0, len(result)):
        round = result[index]
        round["num_of_orders"] = get_num_of_orders_for_round(int(round["round_id"]))
        result[index] = round 

    if result == None:
        return []
    return result   
   
def get_orders_by_round_id(round_id):
    query = f"""
        SELECT
            o.order_id, 
            o.person_id,
            p.first_name,
            p.surname,
            CONCAT(p.first_name, ' ' , p.surname) AS fullname,
            o.drink_id,
            d.name AS drink_name,
            o.special_requests
        FROM 
            tbl_orders AS o
        INNER JOIN
            tbl_people AS p ON o.person_id=p.person_id
        INNER JOIN
            tbl_drinks AS d ON o.drink_id = d.drink_id 
        WHERE
            o.round_id = %s
    """
    parameters = (round_id)
    return fetch_all_from_db(query, parameters)

def get_round_by_round_id(round_id):
    query = f"""
        SELECT
            CONCAT(p.first_name, ' ' , p.surname) as maker_fullname,
            r.round_id,
            timestampdiff(minute, now(), r.expiry_datetime) as minutes_remaining,
            DATE_ADD(r.expiry_datetime, INTERVAL 1 HOUR) AS expiry_datetime
        FROM
            tbl_rounds as r 
        INNER JOIN
            tbl_people as p on p.person_id=r.maker_id
        WHERE 
            r.round_id = %s
    """
    parameters = (round_id)
    result = fetch_one_from_db(query, parameters)
    
    if result == None:
        return []

    result["orders"] = get_orders_by_round_id(result["round_id"])
    return result   
  
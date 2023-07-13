import MySQLdb

def connect():
    db = MySQLdb.connect(host="localhost", user="root", passwd="12345", db="avalia_unb")
    return db

def close(db):
    db.close()

def execute_query(query, values=None):
    db = connect()
    cursor = db.cursor()

    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)

    db.commit()
    close(db)

    return cursor


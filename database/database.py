import sqlite3


def init_db():

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()


    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,

        username TEXT UNIQUE,

        password TEXT

    )
    """
    )


    cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS letters(

        id INTEGER PRIMARY KEY,

        username TEXT,

        letter TEXT

    )
    """
    )


    conn.commit()

    conn.close()



def save_letter(username, letter):


    conn = sqlite3.connect(
        "database/users.db"
    )


    cursor = conn.cursor()


    cursor.execute(

    """
    INSERT INTO letters
    (username, letter)

    VALUES (?,?)

    """,

    (
        username,
        letter
    )

    )


    conn.commit()

    conn.close()



def get_letters(username):


    conn = sqlite3.connect(
        "database/users.db"
    )


    cursor = conn.cursor()


    cursor.execute(

    """
    SELECT letter

    FROM letters

    WHERE username=?

    """,

    (
        username,
    )

    )


    data = cursor.fetchall()


    conn.close()


    return data
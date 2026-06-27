import sqlite3
import hashlib


def create_user(username, password):

    conn = sqlite3.connect(
        "database/users.db"
    )

    cursor = conn.cursor()


    password = hashlib.sha256(
        password.encode()
    ).hexdigest()


    try:

        cursor.execute(

            """
            INSERT INTO users
            (username,password)

            VALUES (?,?)

            """,

            (
                username,
                password
            )

        )


        conn.commit()

        return True


    except:

        return False



def login_user(username,password):


    conn = sqlite3.connect(
        "database/users.db"
    )


    cursor = conn.cursor()


    password = hashlib.sha256(
        password.encode()
    ).hexdigest()


    cursor.execute(

        """
        SELECT *
        FROM users

        WHERE username=?
        AND password=?

        """,

        (
            username,
            password
        )

    )


    user = cursor.fetchone()


    return user
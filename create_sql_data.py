import random
import sqlite3


def random_value(start=0, end=20):
    return random.randint(start, end)


def create_weapons_table():
    data_base = sqlite3.connect('game_params.db')
    sql = data_base.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS weapons (
            'reload speed' INT,
            'rotational speed' INT,
            'diameter' INT,
            'power volley' INT,
            'count' INT
        )""")
    data_base.commit()

    for i in range(0, 20):
        sql.execute(f"INSERT INTO weapons VALUES (?, ?, ?, ?, ?)", (random_value(), random_value(), random_value(), random_value(), random_value()))
        data_base.commit()


create_weapons_table()

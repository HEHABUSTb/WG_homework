import random
import sqlite3
import allure




def random_value(start=0, end=20):
    return random.randint(start, end)


@allure.step
def create_ships_table(data_base_name='game_params.db'):
    data_base = sqlite3.connect(data_base_name)
    sql = data_base.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS ships (
                'ship' TEXT,
                'weapon' TEXT,
                'hull' TEXT,
                'engine' TEXT
            )""")
    data_base.commit()


@allure.step
def create_weapons_table(data_base_name='game_params.db'):
    data_base = sqlite3.connect(data_base_name)
    sql = data_base.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS weapons (
            'weapon' TEXT,
            'reload speed' INT,
            'rotational speed' INT,
            'diameter' INT,
            'power_volley' INT,
            'count' INT
        )""")
    data_base.commit()

    for i in range(1, 21):
        weapon_name = f'Weapon-{i}'
        sql.execute(f"INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?)", (weapon_name, random_value(),
                                                                       random_value(), random_value(), random_value(), random_value()))
        data_base.commit()


@allure.step
def create_hulls_table(data_base_name='game_params.db'):
    data_base = sqlite3.connect(data_base_name)
    sql = data_base.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS hulls (
                'hull' TEXT,
                'armor' INT,
                'type' INT,
                'capacity' INT
            )""")
    data_base.commit()

    for i in range(1, 6):
        hull_name = f'Hull-{i}'
        sql.execute(f"INSERT INTO hulls VALUES ('{hull_name}', {random_value()}, {random_value()}, {random_value()})")
        data_base.commit()


@allure.step
def create_engines_table(data_base_name='game_params.db'):
    data_base = sqlite3.connect(data_base_name)
    sql = data_base.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS engines (
                'engine' TEXT,
                'power' INT,
                'type' INT
            )""")
    data_base.commit()

    for i in range(1, 7):
        engine_name = f'Engine-{i}'
        sql.execute(f"INSERT INTO engines VALUES ('{engine_name}', {random_value()}, {random_value()})")
        data_base.commit()

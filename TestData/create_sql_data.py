import random
import sqlite3
import allure


def random_value(start=1, end=20):
    return random.randint(start, end)


class CreateDB:

    def create_ships_table(self, data_base_name='game_params.db'):
        data_base = sqlite3.connect(data_base_name)
        sql = data_base.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS ships (
                    'ship' TEXT PRIMARY KEY,
                    'weapon' TEXT,
                    'hull' TEXT,
                    'engine' TEXT
                )""")
        data_base.commit()

        for i in range(1, 201):
            ship_name = f'Ship-{i}'
            weapon_name = f'Weapon-{random_value()}'
            hull_name = f'Hull-{random_value(1, 5)}'
            engine_name = f'Engine-{random_value(1, 6)}'
            sql.execute(f"INSERT INTO ships VALUES ('{ship_name}', '{weapon_name}', '{hull_name}', '{engine_name}')")
            data_base.commit()
        data_base.close()

    @allure.step
    def create_weapons_table(self, data_base_name='game_params.db'):
        data_base = sqlite3.connect(data_base_name)
        sql = data_base.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS weapons (
                'weapon' TEXT PRIMARY KEY,
                'reload speed' INT,
                'rotational speed' INT,
                'diameter' INT,
                'power_volley' INT,
                'count' INT,
                FOREIGN KEY(weapon) REFERENCES ships(weapon)
            )""")
        data_base.commit()

        for i in range(1, 21):
            weapon_name = f'Weapon-{i}'
            sql.execute(f"INSERT INTO weapons VALUES (?, ?, ?, ?, ?, ?)", (weapon_name, random_value(),
                                                                           random_value(), random_value(),
                                                                           random_value(), random_value()))
            data_base.commit()
        data_base.close()

    def create_hulls_table(self, data_base_name='game_params.db'):
        data_base = sqlite3.connect(data_base_name)
        sql = data_base.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS hulls (
                    'hull' TEXT PRIMARY KEY,
                    'armor' INT,
                    'types' INT,
                    'capacity' INT,
                    FOREIGN KEY(hull) REFERENCES ships(hull)
                )""")
        data_base.commit()

        for i in range(1, 6):
            hull_name = f'Hull-{i}'
            sql.execute(f"INSERT INTO hulls VALUES ('{hull_name}', {random_value()}, {random_value()}, {random_value()})")
            data_base.commit()
        data_base.close()

    def create_engines_table(self, data_base_name='game_params.db'):
        data_base = sqlite3.connect(data_base_name)
        sql = data_base.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS engines (
                    'engine' TEXT PRIMARY KEY,
                    'power' INT,
                    'type' INT,
                    FOREIGN KEY(engine) REFERENCES ships(engine)
                )""")
        data_base.commit()

        for i in range(1, 7):
            engine_name = f'Engine-{i}'
            sql.execute(f"INSERT INTO engines VALUES ('{engine_name}', {random_value()}, {random_value()})")
            data_base.commit()

    data_base = sqlite3.connect('game_params.db')
    sql = data_base.cursor()


create = CreateDB()
create.create_ships_table()
create.create_engines_table()
create.create_hulls_table()
create.create_weapons_table()

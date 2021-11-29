import logging
import os
import sqlite3
from shutil import copyfile
import allure
from TestData.create_sql_data import random_value


class CreateFakeDB:

    def copy_table(self, path, path_to):
        try:
            copyfile(path, path_to)
        except Exception as e:
            print(f"The error '{e}' occurred")
            raise e

    def update_hulls_table(self, path_to_db):
        data_base = sqlite3.connect(path_to_db)
        sql = data_base.cursor()

        hulls = sql.execute(f"SELECT Count (*) FROM hulls")
        hulls_count = 0
        for val in hulls:
            hulls_count += val[0]

        for i in range(1, hulls_count + 1):
            # sql.execute(f"UPDATE hulls SET armor = {random_value()} WHERE hull = 'Hull-{i}'")
            hull_name = f'Hull-{i}'
            sql.execute(f"UPDATE hulls SET armor = ?, types = ?, capacity = ? WHERE hull = ?",
                        (random_value(), random_value(), random_value(), hull_name))
            data_base.commit()
        data_base.close()

    def update_ships_table(self, path_to_db):
        data_base = sqlite3.connect(path_to_db)
        sql = data_base.cursor()
        ships = sql.execute(f"SELECT Count (*) FROM ships")
        ships_count = 0
        for val in ships:
            ships_count += val[0]

        for i in range(1, ships_count + 1):
            ship_name = f'Ship-{i}'

            weapon = sql.execute("SELECT weapon FROM weapons ORDER BY RANDOM() LIMIT 1").fetchall()
            weapon = weapon[0][0]

            hull = sql.execute("SELECT hull FROM hulls ORDER BY RANDOM() LIMIT 1").fetchall()
            hull = hull[0][0]

            engine = sql.execute("SELECT engine FROM engines ORDER BY RANDOM() LIMIT 1").fetchall()
            engine = engine[0][0]

            sql.execute(f"UPDATE ships SET weapon = ?, hull = ?, engine = ? WHERE ship = ?",
                        (weapon, hull, engine, ship_name))
            data_base.commit()
        data_base.close()

    def update_engines_table(self, path_to_db):
        data_base = sqlite3.connect(path_to_db)
        sql = data_base.cursor()

        hulls = sql.execute(f"SELECT Count (*) FROM engines")
        hulls_count = 0
        for val in hulls:
            hulls_count += val[0]

        for i in range(1, hulls_count + 1):
            # sql.execute(f"UPDATE hulls SET armor = {random_value()} WHERE hull = 'Hull-{i}'")
            engine_name = f'Engine-{i}'
            sql.execute(f"UPDATE engines SET power = ?, type = ? WHERE engine = ?", (random_value(), random_value(), engine_name))
            data_base.commit()
        data_base.close()

    def update_weapons_table(self, path_to_db):
        data_base = sqlite3.connect(path_to_db)
        sql = data_base.cursor()

        weapons = sql.execute(f"SELECT Count (*) FROM weapons")
        count = 0
        for val in weapons:
            count += val[0]

        for i in range(1, count + 1):
            # sql.execute(f"UPDATE hulls SET armor = {random_value()} WHERE hull = 'Hull-{i}'")
            weapon_name = f'Weapon-{i}'
            sql.execute(f"UPDATE weapons SET 'reload speed' = ?, 'rotational speed' = ?, diameter = ?, power_volley = ?, count = ? WHERE weapon = ?",
                        (random_value(), random_value(), random_value(), random_value(), random_value(), weapon_name))
            data_base.commit()
        data_base.close()

    @allure.step
    def update_all_fake_table(self, path_to_db):
        self.update_ships_table(path_to_db)
        self.update_weapons_table(path_to_db)
        self.update_hulls_table(path_to_db)
        self.update_engines_table(path_to_db)
        logging.info('All fake value was updated')

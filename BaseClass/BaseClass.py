import os
import sqlite3


class BaseClass:

    def get_game_data(self):
        path = os.getcwd() + '\\TestData\\game_params.db'
        # path = 'D:\\GIT_Repository\\WG_homework\\TestData\\game_params.db'
        connection = sqlite3.connect(path)
        selector = "SELECT * FROM ships LEFT JOIN engines ON ships.engine == engines.engine " \
                   "LEFT JOIN hulls ON ships.hull == hulls.hull " \
                   "LEFT JOIN weapons ON ships.weapon == weapons.weapon"
        cursor = connection.cursor()

        try:
            cursor.execute(selector)
            field_name = list(map(lambda x: x[0], cursor.description))
            ships_data = []
            result = cursor.fetchall()
            for value in result:
                value = list(value)
                dictionary = dict(zip(field_name, value))
                ships_data.append(dictionary)
            cursor.close()
            return ships_data
        except Exception as e:
            print(f"The error '{e}' occurred")

    def get_fake_data(self, ship_name):
        path = os.getcwd() + '\\TestData\\fake_params.db'
        # path = 'D:\\GIT_Repository\\WG_homework\\TestData\\fake_params.db'
        connection = sqlite3.connect(path)
        result = connection.execute("SELECT * FROM ships LEFT JOIN engines ON ships.engine == engines.engine " \
                                    "LEFT JOIN hulls ON ships.hull == hulls.hull " \
                                    f"LEFT JOIN weapons ON ships.weapon == weapons.weapon WHERE ship = ('{ship_name}')")
        field_name = list(map(lambda x: x[0], result.description))
        result = result.fetchall()
        dictionary = {}
        for value in result:
            value = list(value)
            dictionary = dict(zip(field_name, value))
        connection.close()
        return dictionary

import os
import pytest
import logging
from BaseClass.BaseClass import BaseClass


def get_all_data(what_params_you_need):
    ships = BaseClass().get_game_data()
    ids = []
    values = []
    params = []
    for ship in ships:
        ids.append(ship['ship'])
        val = []
        for key in what_params_you_need:
            if key in ship:
                val.append(ship[key])
        values.append(val)
    for i in range(len(ids)):
        param = pytest.param(*tuple(values[i]), id=ids[i])
        params.append(param)
    return params


@pytest.mark.smoke
@pytest.mark.usefixtures('setup')
class TestGameParams(BaseClass):

    @pytest.mark.one
    @pytest.mark.parametrize("ship, engine, power, type", get_all_data(['ship', 'engine', 'power', 'type']))
    def example_add(self, ship, engine, power, type):
        print('GAME DATA')
        print(ship, engine, power, type)
        print('FAKE DATA')
        fake = self.get_fake_data(ship)
        print(fake)
        print(fake['engine'] == engine)
        fake_engine, fake_power = fake['engine'], int(fake['power'])
        assert (engine, power) == (fake_engine, fake_power)

    @pytest.mark.engines
    def test_engines(self, get_data):
        engine_name, engine_power, engine_type = get_data['engine'], float(get_data['power']), float(get_data['type'])

        fake_data = self.get_fake_data(get_data['ship'])
        fake_engine_name, fake_engine_power, fake_engine_type = fake_data['engine'], float(fake_data['power']), float(fake_data['type'])

        assert (engine_name, engine_power, engine_type) == (fake_engine_name, fake_engine_power, fake_engine_type),\
            f"Values not equal got {engine_name}, power:{engine_power}, type:{engine_type}" \
            f" should be {fake_engine_name}, {fake_engine_power}, {fake_engine_type}"

    @pytest.mark.engines
    @pytest.mark.parametrize("ship, engine, power, type", get_all_data(['ship', 'engine', 'power', 'type']))
    def test_engines(self, ship, engine, power, type):

        fake_data = self.get_fake_data(ship)
        fake_engine, fake_power, fake_type = fake_data['engine'], int(fake_data['power']), int(fake_data['type'])

        assert (engine, power, type) == (fake_engine, fake_power, fake_type),\
            f"Values not equal {engine}, power:{power}, type:{type}" \
            f" should be {fake_engine}, {fake_power}, {fake_type}"

    data = ['ship', 'hull', 'armor', 'types', 'capacity']

    @pytest.mark.hulls
    @pytest.mark.parametrize("ship, hull, armor, types, capacity", get_all_data(data))
    def test_hulls(self, ship, hull, armor, types, capacity):

        fake_data = self.get_fake_data(ship)
        fake_hull, fake_armor, fake_types, fake_capacity =\
            fake_data['hull'], int(fake_data['armor']), int(fake_data['types']), int(fake_data['capacity'])

        assert (hull, armor, types, capacity) ==\
               (fake_hull, fake_armor, fake_types, fake_capacity), \
               f"Values not equal {hull} armor: {armor}, type: {types}, capacity: {capacity}" \
               f" should be {fake_hull}, {fake_armor}, {fake_types} {fake_capacity}"

    data = ['ship', 'weapon', 'reload speed', 'rotational speed', 'diameter', 'power_volley', 'count']
    param = "ship, weapon, reload_speed, rotational_speed, diameter, power_volley, count"

    @pytest.mark.parametrize(param, get_all_data(data))
    @pytest.mark.weapons
    def test_weapons(self, ship, weapon, reload_speed, rotational_speed, diameter, power_volley, count):

        fake_data = self.get_fake_data(ship)
        fake_name, fake_reload_speed, fake_rotation = fake_data['weapon'], int(fake_data['reload speed']),\
                                                                                      int(fake_data['rotational speed'])
        fake_diameter, fake_power, fake_count = int(fake_data['diameter']), int(fake_data['power_volley']),\
                                                                                                int(fake_data['count'])
        assert (weapon, reload_speed, rotational_speed, diameter, power_volley, count) == \
               (fake_name, fake_reload_speed, fake_rotation, fake_diameter, fake_diameter, fake_power, fake_count), \
                f"Values not equal {weapon} reload speed: {reload_speed}, rotation: {rotational_speed}," \
                f" diameter: {diameter} power: {power_volley} count:{count} " \
                f"should be {fake_name, fake_reload_speed, fake_rotation, fake_diameter, fake_power, fake_count}"

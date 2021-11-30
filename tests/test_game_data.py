import os
import pytest
import logging
from BaseClass.BaseClass import BaseClass


@pytest.mark.smoke
@pytest.mark.usefixtures('setup')
class TestGameParams(BaseClass):

    data = BaseClass()
    ships = data.get_game_data()


    @pytest.fixture(params=ships)
    def get_data(self, request):
        """Will need to rework in smth like param = pytest.param(ship.name, hull_name, ship, hull, hulls_count, id='{}-{}'.format(ship.name, hull_name))"""
        return request.param

    @pytest.mark.one
    def example_add_t(self, get_data):
        print('GAME DATA')
        print(get_data)
        name = get_data['ship']
        print('FAKE DATA')
        fake = self.get_fake_data(name)
        print(fake['engine'] == get_data['engine'])
        engine_name, engine_power = get_data['engine'], float(get_data['power'])
        fake_engine_name, fake_engine_power = fake['engine'], float(fake['power'])
        assert (engine_name, engine_power) == (fake_engine_name, fake_engine_power)

    @pytest.mark.engines
    def test_engines(self, get_data):
        engine_name, engine_power, engine_type = get_data['engine'], float(get_data['power']), float(get_data['type'])

        fake_data = self.get_fake_data(get_data['ship'])
        fake_engine_name, fake_engine_power, fake_engine_type = fake_data['engine'], float(fake_data['power']), float(fake_data['type'])

        assert (engine_name, engine_power, engine_type) == (fake_engine_name, fake_engine_power, fake_engine_type),\
            f"Values not equal got {engine_name}, power:{engine_power}, type:{engine_type}" \
            f" should be {fake_engine_name}, {fake_engine_power}, {fake_engine_type}"

    @pytest.mark.hulls
    def test_hulls(self, get_data):
        hull_name, hull_armor, hull_type, hull_capacity =\
            get_data['hull'], int(get_data['armor']), int(get_data['types']), int(get_data['capacity'])

        fake_data = self.get_fake_data(get_data['ship'])
        fake_hull_name, fake_hull_armor, fake_hull_type, fake_hull_capacity =\
            fake_data['hull'], int(fake_data['armor']), int(fake_data['types']), int(fake_data['capacity'])

        assert (hull_name, hull_armor, hull_type, hull_capacity) ==\
               (fake_hull_name, fake_hull_armor, fake_hull_type, fake_hull_capacity), \
               f"Values not equal got {hull_name} armor: {hull_armor}, type: {hull_type}, capasity: {hull_capacity}" \
               f" should be {fake_hull_name}, {fake_hull_armor}, {fake_hull_type} {fake_hull_capacity}"

    @pytest.mark.weapons
    def test_weapons(self, get_data):
        name, reload_speed, rotation,  =  get_data['weapon'], int(get_data['reload speed']), int(get_data['rotational speed'])
        diameter, power, count = int(get_data['diameter']), int(get_data['power_volley']), int(get_data['count'])

        fake_data = self.get_fake_data(get_data['ship'])
        fake_name, fake_reload_speed, fake_rotation = fake_data['weapon'], int(fake_data['reload speed']),\
                                                                                      int(fake_data['rotational speed'])
        fake_diameter, fake_power, fake_count = int(fake_data['diameter']), int(fake_data['power_volley']),\
                                                                                                int(fake_data['count'])
        assert (name, reload_speed, rotation, diameter, power, count) == \
               (fake_name, fake_reload_speed, fake_rotation, fake_diameter, fake_diameter, fake_power, fake_count), \
                f"Values not equal got {name} reload speed: {reload_speed}, rotation: {rotation}, diameter: {diameter}" \
                f" count:{count} should be {fake_name, fake_reload_speed, fake_rotation, fake_diameter, fake_power, fake_count}"

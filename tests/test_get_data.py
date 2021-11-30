import os
import pytest
import logging
from BaseClass.BaseClass import BaseClass


def get_all_data(what_params_you_need):
    ships = BaseClass().get_game_data()
    ids = []
    values = []
    arg_names = []
    params = []
    for ship in ships:
        ids.append(ship['ship'])
        arg_names.append(what_params_you_need)
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
    def test_example(self, ship, engine, power, type):
        print(ship, engine, power, type)
        pass
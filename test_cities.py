import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1) == \
        pytest.approx(9.386+18.496+10.646, 0.01)
    assert compute_total_distance(road_map1) == 4.22

    '''add your further tests'''


def test_swap_cities():
    '''add your tests'''
    assert swap_cities(1, 2, 3) == ('a', 'b')

    assert road_map10 = [("Atlanta", "Georgia", 33.76, -84.39),
                         ("Honolulu", "Hawaii",  21.30895, -157.826182),
                         ("Boise", "Idaho", 43.613739, -116.237651)]

    assert swap_cities(road_map10, 0, 2) == 


def test_shift_cities():
    '''add your tests'''
    assert shift_cities(12) == []

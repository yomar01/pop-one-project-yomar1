import pytest
from cities import *

road_map1 = [("Montana", "Helana", 46.595805, -112.027031)]

road_map2 = [("Georgia", "Atlanta", 33.76, -84.39),
             ("Hawaii", "Honolulu", 21.30895, -157.826182)]

road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
             ("Delaware", "Dover", 39.161921, -75.526755),
             ("Minnesota", "Saint Paul", 44.95, -93.094)]

road_map4 = [("Oklahoma", "Oklahoma City", 35.482309, -97.534994),
             ("Oregon", "Salem", 44.931109, -123.029159),
             ("Pennsylvania", "Harrisburg", 40.269789, -76.875613),
             ("Rhode Island", "Providence", 41.82355, -71.422132)]

road_map5 = [("Utah", "Salt Lake City", 40.7547, -111.892622),
             ("Vermont", "Montpelier", 44.26639, -72.57194),
             ("Virginia", "Richmond", 37.54, -77.46),
             ("Washington", "Olympia", 47.042418, -122.893077),
             ("West Virginia", "Charleston", 38.349497, -81.633294)]


def test_compute_total_distance():

    assert compute_total_distance(road_map1) == \
        pytest.approx(0,0.1)
    assert compute_total_distance(road_map2) == \
        pytest.approx(148.97,0.1)
    assert compute_total_distance(road_map3) == \
        pytest.approx(38.53,0.1)
    assert compute_total_distance(road_map4) == \
        pytest.approx(106.12,0.1)
    assert compute_total_distance(road_map5) == \
        pytest.approx(166.73,0.1)
    

def test_swap_cities():
    '''add your tests'''
    assert swap_cities(road_map1, 0, 0) == ([('Montana', 'Helana', 46.595805, -112.027031)], 0.0)
    assert swap_cities(road_map2, 1, 0) == ([('Hawaii', 'Honolulu', 21.30895, -157.826182), ('Georgia', 'Atlanta', 33.76, -84.39)], pytest.approx(148.97,0.1))
    assert swap_cities(road_map3, 2, 0) == ([('Minnesota', 'Saint Paul', 44.95, -93.094), ('Delaware', 'Dover', 39.161921, -75.526755), ('Kentucky', 'Frankfort', 38.197274, -84.86311)], pytest.approx(38.53,0.1))
    assert swap_cities(road_map4, 3, 1) == ([('Oklahoma', 'Oklahoma City', 35.482309, -97.534994), ('Rhode Island', 'Providence', 41.82355, -71.422132), ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613), ('Oregon', 'Salem', 44.931109, -123.029159)], pytest.approx(106.12,0.1))
    assert swap_cities(road_map5, 4, 2) == ([('Utah', 'Salt Lake City', 40.7547, -111.892622), ('Vermont', 'Montpelier', 44.26639, -72.57194), ('West Virginia', 'Charleston', 38.349497, -81.633294), ('Washington', 'Olympia', 47.042418, -122.893077), ('Virginia', 'Richmond', 37.54, -77.46)], pytest.approx(173.46,0.1))

# def test_shift_cities():
#     '''add your tests'''
#     assert shift_cities(12) == []

from math import sqrt

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return 
    them as a list of four-tuples: 

      [(state, city, latitude, longitude), ...] 

    Use this as your initial `road_map`, that is, the cycle 

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """

    file = open(file_name, 'r')

    roadmap = list()

    for line in file:
        line = line.strip()
        line = line.split('\t')
        city, state, lon, lat = line
        tp = (state, city, float(lon), float(lat))
        roadmap.append(tp)

    return roadmap

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations. 
    Print only one or two digits after the decimal point.
    """
    
    lst = []
    
    for element in road_map:
        city, lon, lat = element[1], element[2], element[3]
        lon, lat = round(lon, 2), round(lat, 2)
        lst.extend([city, lon, lat])
    print(lst)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all 
    the connections in the `road_map`. Remember that it's a cycle, so that 
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    total_distance = 0

    for i in range(0, len(road_map)-1):
        total_distance += sqrt((road_map[i][2]-road_map[i][3])**2 + (road_map[i+1][2]-road_map[i+1][3])**2)

    total_distance += sqrt((road_map[49][2]-road_map[49][3])**2 + (road_map[0][2]-road_map[0][3])**2)

    return total_distance


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map. 
    """
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]
    return road_map1


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass


def print_map(road_map):
    """

    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass


if __name__ == "__main__":  # keep this in
    main()



data = read_cities('city-data.txt')


print(compute_total_distance(data))
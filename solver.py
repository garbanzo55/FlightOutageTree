import OutageVertex


def insert_outagevertex_into_sorted_list(lst, obj):
    for i in range(len(lst)):
        if lst[i] > n:
            lst.insert(i, n)
            return lst
    lst.append(n)
    return lst



def main():
    initial = OutageVertex(
        0,                  # weight 
        None,               # previous
        'FRA',              # departure_station_iata
        'LOS',              # arrival_station_iata
        1718372502,         # std
        'some type',        # ac_type
        'some requirement'  # ac_reqs   
    )

    childless_visited = [initial]

    terminate = False
    while not terminate:
        current = childless_visited.pop(0)
        next_flight_of_current = current.get_next_of_registration
        options = current.get_options()
        
        if not options:
            continue

        solution_found = False
        for option in options:
            if option.is_solution:
                print('solution found')
                terminate = True

        for option in options + [nexT_flight_of_current]:
            childless_visited = insert_outagevertex_into_sorted_list(childless_visited, option)

        









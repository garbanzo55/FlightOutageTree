class OutageVertex:
    
    def __init__(self, weight, previous, departure_station_iata, arrival_station_iata, std, ac_type, ac_reqs):
        this.weight = weight
        this.previous = previous
        this.next = None
        this.departure_station_iata = departure_station_iata
        this.arrival_station_iata = arrival_station_iata
        this.std = std
        this.ac_type = ac_type
        this.ac_reqs = ac_reqs


    def get_options(self):
        # should return the OutageVertex objects that could be (re)assigned to f(v)
        # this is a function of the flight plan (conext), the departure station, the std and the flight requirements.
        # must also do weighing
        # Should simply return OutageVertex objects.
        return None


    def is_solution(self):
        if not (self.departure_station_iata or self.arrival_station_iata):
            return True
        return False


    def get_next_of_registration(self):
        additional_weight = 1
        arrival_station_iata = None
        std = None
        ac_type = None
        ac_reqs = None
        result = OutageVertex(
            self.weight + additional_weight, 
            self, 
            self.arrival_station_iata, 
            arrival_station_iata, 
            std, 
            ac_type, 
            ac_reqs)
        return result


    def check_ac_reqs(self, ac_reqs):
        # check if an OutageVertex object fulfills given aircraft requirements
        return False


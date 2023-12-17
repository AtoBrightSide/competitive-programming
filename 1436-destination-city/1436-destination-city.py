class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # store all the possible destination cities, also all the departure cities
        # in order for a city to be a destination, it HAS to be in the dest cities, but NOT in depart cities
        
        pot_destinations = set([])
        dep_cities = set([])
        for dep, dest in paths:
            pot_destinations.add(dest)
            dep_cities.add(dep)
        
        for destination in pot_destinations:
            if destination not in dep_cities:
                return destination
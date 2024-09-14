our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#(intersection of sets)
shared_routes = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", shared_routes)

#(difference of sets)
unique_our_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_our_routes)

#(symmetric difference)
exclusive_routes = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", exclusive_routes)
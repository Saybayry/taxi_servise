
""" used osmX
    use lib for create route
"""
import osmnx as ox
import networkx as nx


def create_route(start_point, end_point, location)-> [(float, float)] :
    """this function return route coordinates"""
    G = ox.graph_from_place(location, network_type="drive")
    G = ox.speed.add_edge_speeds(G)
    G = ox.speed.add_edge_travel_times(G)
    orig = ox.distance.nearest_nodes(G, X=start_point[0], Y=start_point[1])
    dest = ox.distance.nearest_nodes(G, X=end_point[0], Y=end_point[1])
    route = ox.shortest_path(G, orig, dest, weight="travel_time")
    arr= []
    for el in route:
        x = (G.nodes[el])['x']
        y = (G.nodes[el])['y']
        arr.append((y, x))
    edge_lengths = ox.utils_graph.get_route_edge_attributes(G, route, "length")
    len = round(sum(edge_lengths))
    return arr, len


def calculate_price(len, tarif = 30, mintarif =124) -> float:
    """this function calculates
     price ride on taxi """
    price = (len/1000) * tarif
    if price <= mintarif:
        price=mintarif
    return price


def rander_route():
    """ this function render
     map and rule and return to img"""
    pass

def render_map():
    """ this function render map osm"""
    pass
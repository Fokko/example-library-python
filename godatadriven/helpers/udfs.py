from geopy import distance

SCHIPHOL_LAT = 52.3076865
SCHIPHOL_LON = 4.7674241


def distance_to_schiphol(lat, lon):
    """
    Computes the distance from lat, lon to Schiphol
    return: The distance in kilometer
    """
    schiphol = (SCHIPHOL_LAT, SCHIPHOL_LON)
    return distance.vincenty(schiphol, (lat, lon)).km

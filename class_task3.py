#Объединить наборы данных из предыдущих задач и посчитать, у какой станции метро больше всего остановок (в радиусе 0.5 км).

import csv
import json

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.
    return c * r

stops_data_file_path = 'data/data-398-2017-12-01.csv'
lobbies_data_file_path = 'data/data-397-2017-10-31.json'

stops_file = open (stops_data_file_path, 'r')
fields = stops_file.readline().replace('"','').split(';')
stops_data = csv.DictReader(stops_file, fields, delimiter = ';')

lobbies_file = open(lobbies_data_file_path, 'r')
lobbies_data = json.load(lobbies_file)

stations_stops = dict()

for stop in stops_data:
    for lobby in lobbies_data:
        lobby_lon = float(lobby['Longitude_WGS84'])
        lobby_lat = float(lobby['Latitude_WGS84'])
        stop_lon = float(stop['Longitude_WGS84'])
        stop_lat = float(stop['Latitude_WGS84'])
        # check the distance between lobby and stop
        if haversine(lobby_lon, lobby_lat, stop_lon, stop_lat) <= 0.5:
            # increase counter with known station
            if stations_stops.get(lobby['NameOfStation']):
                stations_stops[lobby['NameOfStation']] += 1
            # increase counter with new station
            else:
                stations_stops[lobby['NameOfStation']] = 1

station_with_max_stops_near = max(stations_stops, key = stations_stops.get)
print ('Станция с максимальным количеством остановок в радиусе 0.5 км: {}'.format(station_with_max_stops_near))
print ('Рядом с ней находится {} остановок.'.format(stations_stops[station_with_max_stops_near]))

stops_file.close()
lobbies_file.close()
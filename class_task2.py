# В этом задании требуется определить, 
# на каких станциях московского метро 
# сейчас идёт ремонт эскалаторов 
# и вывести на экран их названия.

import json

data_file = 'data/data-397-2017-10-31.json'

repair_escalator_stations = set()

with open(data_file, 'r') as f:
	data = json.load(f)
	for el in data:
		if len(el['RepairOfEscalators'])>0:
			repair_escalator_stations.add(el['NameOfStation'])

for station in repair_escalator_stations:
	print (station)
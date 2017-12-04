# Считать из csv-файла (с http://data.mos.ru/datasets/752) количество остановок, 
# вывести улицу, на которой больше всего остановок.
import csv

data_file = 'data/data-398-2017-12-01.csv'

with open (data_file, 'r') as f:
	fields = f.readline().replace('"','').split(';')
	reader = csv.DictReader(f, fields, delimiter = ';')

	street_counter = dict()
	for row in reader:
		if street_counter.get(row['Street']):
			street_counter[row['Street']] += 1
		else:
			street_counter[row['Street']] = 1
	max_stops_street = max(street_counter, key=street_counter.get)
	print ('Максимальное количество остановок находится на: {}'.format(max_stops_street))
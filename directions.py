#Used this script to populate the csv of Google direction times
#Manually filled in values with errors.
import urllib, simplejson
f = open('toptrips.csv', 'r')
out = open('urls.csv', 'w')
out.write('i, bike_url, transit_url\n')
i = 2
for line in f:
	line = line[:-1]
	args = line.split(',')
	bike_url = 'http://maps.googleapis.com/maps/api/directions/json?origin=' + args[-4] + ',' + args[-3] + '&destination=' + args[-2] + ',' + args[-1] +'&mode=bicycling&sensor=false'
	transit_url = 'http://maps.googleapis.com/maps/api/directions/json?origin=' + args[-4] + ',' + args[-3] + '&destination=' + args[-2] + ',' + args[-1] +'&mode=transit&departure_time=1393450200&sensor=false'
	out.write(str(i) + ',' + bike_url + ',' + transit_url + '\n')
	i = i + 1
f.close()
out.close()

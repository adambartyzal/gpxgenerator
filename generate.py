import sys
from datetime import datetime
import math

if (len(sys.argv) < 4):
  sys.exit(f'Usage: python {sys.argv[0]} waypoints_file.gpx' 'start_timestamp' 'speed')

waypoints_file = sys.argv[1]
start = int(sys.argv[2])
speed = int(sys.argv[3])
current = start

points = 0
distance = 0
prev_lat = 0
prev_lon = 0
#prev_ele = 0

with open(waypoints_file, 'r') as waypoints:
  for line in waypoints:
    if ('<trkpt' in line):
      points += 1

idx = 0

with open('generated.gpx', 'w') as generated:
  with open(waypoints_file, 'r') as waypoints:
    for line in waypoints:
      generated.write(line)
      if ('<trkpt' in line):
        lat = float(line[line.find('lat') + 5 : line.find('lat') + 14])
        lon = float(line[line.find('lon') + 5 : line.find('lon') + 14])
        distance = math.sqrt((lat - prev_lat) ** 2 + (lon - prev_lon) **2) * 300000 / speed
        prev_lat = lat
        prev_lon = lon
        idx += 1


      if ('<ele' in line):
        #ele = float(line[line.find('<ele>') + 5 : line.find('</ele>')])
        #ele_diff = ele - prev_ele
        if (idx != 1):
          current += distance
        now = datetime.fromtimestamp(current).isoformat()
        generated.write('				<time>' + now + '</time>\n')
        #prev_ele = ele


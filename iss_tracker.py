import math
import time
from datetime import datetime
import ephem
 
degrees_per_radian = 180.0 / math.pi
 
home = ephem.Observer()
home.lon = '90.0490'   # +E
home.lat = '35.1495'      # +N
home.elevation = 80 # meters
 
# Always get the latest ISS TLE data from:
# http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html
iss = ephem.readtle('ISS',
    '1 25544U 98067A   16130.57153142  .00016717  00000-0  10270-3 0  9006',
    '2 25544  51.6430 250.6723 0001862 101.2349 258.9013 15.54497794 38973'
)

mars = ephem.Mars()
venus = ephem.Venus()
saturn = ephem.Saturn()
moon = ephem.Moon()
sun = ephem.Sun()
 
while True:
    home.date = datetime.now()
    iss.compute(home)
    mars.compute(home)
    venus.compute(home)
    saturn.compute(home)
    moon.compute(home)
    sun.compute(home)
    print("====================================")
    print(home.date)
    print('iss: altitude %4.1f deg, azimuth %5.1f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    print('mars: altitude %4.lf deg, azimuth %5.lf deg' % (mars.alt * degrees_per_radian, mars.az * degrees_per_radian))
    print('venus: altitude %4.lf deg, azimuth %5.lf deg' % (venus.alt * degrees_per_radian, venus.az * degrees_per_radian))
    print('saturn: altitude %4.1f deg, azimuth %5.1f deg' % (saturn.alt * degrees_per_radian, saturn.az * degrees_per_radian))
    print('moon: altitude %4.lf deg, azimuth %5.lf deg' % (moon.alt * degrees_per_radian, moon.az * degrees_per_radian))
    print('sun: altitude %4.lf deg, azimuth %5.lf deg' % (sun.alt * degrees_per_radian, sun.az * degrees_per_radian))
    print("====================================")
    time.sleep(10.0)

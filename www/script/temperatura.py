import Adafruit_BMP.BMP085 as BMP085
 
sensor = BMP085.BMP085()
 
print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())

temperatura = '{0:0.2f}'.format(sensor.read_temperature())
presion = '{0:0.2f}'.format(sensor.read_pressure())
altitud = '{0:0.2f}'.format(sensor.read_altitude())
mar_presion = '{0:0.2f}'.format(sensor.read_sealevel_pressure())

print temperatura
print presion
print altitud
print mar_presion

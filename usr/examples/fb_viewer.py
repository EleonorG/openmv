import sensor
sensor.set_pixformat(sensor.RGB565)
while (True):
  image = sensor.snapshot()

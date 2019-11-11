import humidity, temperature

def data_page():
    temp, humid = humidity.collect_data()
    temp2C, temp2F = temperature.read_temp()
    return "Sensor 1: Temp={0:0.1f}*C  Humidity={1:0.1f}% <br/> Sensor2: {0:0.1f}*C, {0:0.1f}*F".format(temp, humid, temp2C, temp2F)


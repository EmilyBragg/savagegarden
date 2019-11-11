import Adafruit_DHT as Ada

DHT_SENSOR = Ada.DHT22

DHT_PIN = 21

def collect_data():
    temperature, humidity = Ada.read_retry(DHT_SENSOR, DHT_PIN)
    print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    return temperature, humidity

if __name__ == "__main__":
	collect_data()



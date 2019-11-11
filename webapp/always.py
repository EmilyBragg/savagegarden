import mymail, time

def send_alerts():
    while True:
        mymail.email_alert()
        time.sleep(24*60*60)

if __name__ == "__main__":
    send_alerts()

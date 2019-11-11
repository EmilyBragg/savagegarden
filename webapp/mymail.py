import smtplib, util

def email_alert(examp_str=""):

    server = smtplib.SMTP_SSL('smtp.zoho.com', port=465)

    print("Server Started...")
    server.login('savagegarden@zoho.com','3671A113A0')

    print("Server Login Successful")

    msg ="""From:savagegarden@zohomail.com\nTo:decapod73@gmail.com, ebragg09@gmail.com\nSubject: daily data\n
   """
    msg = msg+util.data_page()

    try:
        server.sendmail('savagegarden@zohomail.com','decapod73@gmail.com, ebragg09@gmail.com',msg)
    except Exception as e:
        print(e)
        return server

    print("Sending Message...")
    server.quit()
    print("Quit Server")

email_alert()

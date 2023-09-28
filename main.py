import requests
from twilio.rest import Client
import smtplib

key = "a781ec62b6488517e40d0379f5b60cef"
lat = 33.684422
long = 73.047882

RECIPIENT_EMAIL = "swegmaster7373@gmail.com"
EMAIL = "contact.alliedestate@gmail.com"
PASSWORD = "qtrcfzrajwvlzwwt"

account_sid = 'AC0b602fec6483feb14abfcf90c22bfc2f'
auth_token = 'efc3ac1aff6bd22b3e2f8bfef925bde'

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": lat,
    "lon": long,
    "appid": key
}

request = requests.get(OWM_endpoint, params=parameters)

weather_data = request.json()

# for n in range(0, 3):
#     if weather_data["list"][n]["weather"][0]["id"] < 700:
#         print("Bring an umbrella")
#         break

weather_slice = weather_data["list"][:4]

id_codes = [item["weather"][0]["id"] for item in weather_slice]

for id in id_codes:
    if id < 700:
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     from_='+12056496992',
        #     body='It will rain today, remember to bring an umbrella!',
        #     to='+923555724968'
        # )
        with smtplib.SMTP("smtp.gmail.com") as email:
            email.starttls()
            email.login(user=EMAIL, password=PASSWORD)
            email.sendmail(to_addrs=RECIPIENT_EMAIL, from_addr=EMAIL, msg=("Subject:Rain Expected\n\n"
                                                                          "Carry an umbrella with you, it's going to rain today!"))

        break


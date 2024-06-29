import requests
import pprint
from dotenv import load_dotenv
import os
import time
import datetime



#ESTEEEE DE AQUIIII SE CONECTAAA CON LA PAAGINAAA DE VUELLOSSS

load_dotenv()



URL = "https://test.api.amadeus.com/v1"
ENDPOINT = "/reference-data/locations/cities"
LOCACION_IATA= "LON"



class FlightSearch:

    def __init__(self):
        self.ACCESS_TOKEN = self.get_token()

    def get_token(self):

        """ESTAAA FUNCIONNN LO QUE HACE ES QUE ME REGRESA O ME RETURNA MI TOKEN PORQUE MI
        TOKEN SE VENCE CADAA 30 MIN ENTONCES ESTA FUNCION ACTUALIZA EL TOKEN

        RETURN TOKEN
        """

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": os.environ["API_KEY"],
            "client_secret": os.environ["API_SECRET"]
        }

        response = requests.post(url=os.environ["TOKEN_ENDPOINT"], headers=header, data=body)
        print("EL TOKEENN ES: ",response.json()["access_token"])
        return response.json()["access_token"]





    def Get_IATA_Code(self, country):
        """"
        Esta funcion me regresa mi IATA de la country que yo le pase
        """
        header = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}"
        }
        param = {
            "keyword": country,
            "max": 2,
            "includeX":"AIRPORTS"
        }

        solicitud = requests.get(url=URL+ENDPOINT, params=param, headers=header)
        return solicitud.json()["data"][0]["iataCode"]

    def Search_Fights(self, destinacion_iata, date, cheaper: int): # el cheaper se le pasa mi precio maximo que despues se va actualizar con un precio menor
        params = {
            "originLocationCode": LOCACION_IATA,
            "destinationLocationCode": destinacion_iata,
            "nonStop": "true",
            "currencyCode": "GBP",
            "adults": 1,
            "departureDate": date,
            "maxPrice": cheaper


        }
        header = {
            "Authorization": f"Bearer {self.ACCESS_TOKEN}"
        }

        solicitud = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",params=params,headers=header)


        flag = 0
        #print(solicitud.json())
        for info in solicitud.json()["data"]:
            print(info["price"]["total"])
            if float(info["price"]["total"]) <=float(cheaper):
                cheaper = info["price"]["total"]
                flag = 1

        if flag == 1: # esto quiere decir que si encontro un vuelo mas barato
            #print(f"Vuelo mas barato encontrado {cheaper}")
            return cheaper
        else:
            #print("No se encontro ningun vuelo barato relacionado con el preciomaximo que le estas pasando")
            return














#
# for i in range(6*30):
#     date = datetime.datetime.now() + datetime.timedelta(days=i+1)
#     date = date.strftime("%Y-%m-%d")
#     print(date)




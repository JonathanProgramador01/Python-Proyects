#### ESTEEE ES DE MI PAGINAAAA DE VUELLLLOSSSSS

import os

import datetime
import requests
from dotenv import load_dotenv
import pprint



load_dotenv()

URL = "https://test.api.amadeus.com"
API_KEY = os.environ.get("Api_Key")
API_SECRET = os.environ.get("API_SECRET")
ORIGIN_LOCACION = "LON"


class Flight_Search:
    def __init__(self):
        self.TOKEN = self.get_token()
        self.HEADER = {
            "Authorization": f"Bearer {self.TOKEN}"
        }

    def get_token(self):
        ENDPOINT = "/v1/security/oauth2/token"
        HEADER = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        DATA = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET,
        }
        try:
            post = requests.post(url=URL+ENDPOINT, headers=HEADER, data=DATA)
            data = post.json()
            return data["access_token"]
        except:
            print("Algo fallo al pedir las constraseñas de la API Flight_Search")
            return None
    def get_country_code(self, pais: str):

        ENPOINT = "/v1/reference-data/locations/cities"
        PARAMETROS = {
            "keyword": pais,
            "max": 1,
        }

        try:
            solicitud = requests.get(url=URL+ENPOINT, headers=self.HEADER, params=PARAMETROS)
            data = solicitud.json()
            return data["data"][0]["iataCode"]
        except Exception as e:
            print("Algooo fallo con tu requesttt de solicitudesss ")
            return None



    def search_flight(self, iata_code: str, lowest_price:int,country: str):

        ENDPOINT = "/v2/shopping/flight-offers"
        fecha_de_mañana = datetime.datetime.now() + datetime.timedelta(days=1)
        fecha_de_mañana = str(fecha_de_mañana).split(" ")[0]
        fecha_dentro_180_dias = datetime.datetime.now() + datetime.timedelta(days=(6*30)+1)
        fecha_dentro_180_dias = str(fecha_dentro_180_dias).split(" ")[0]
        vuelo_mas_barato = lowest_price
        flag = 0
        arrival = None
        departure = None



        parameters = {
            "originLocationCode": ORIGIN_LOCACION,
            "destinationLocationCode": iata_code,
            "departureDate": fecha_de_mañana,
            "returnDate": fecha_dentro_180_dias,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "maxPrice": lowest_price,
        }
        try:
            solicutud = requests.get(url=URL+ENDPOINT, params=parameters, headers=self.HEADER)
            for data in solicutud.json()["data"]:
                price = float(data["price"]["total"])
                if price < vuelo_mas_barato:
                    vuelo_mas_barato = price
                    flag = 1
                    departure = data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    arrival = data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]

            print(f"Geeting flights for {country}...")
            if flag != 0:
                print(country, vuelo_mas_barato)
                return (vuelo_mas_barato, departure, arrival,fecha_de_mañana, fecha_dentro_180_dias)
            else:
                print("Por el momento no hay ningun vuelo barato con tu costo")
                return None


        except:
            print("Naaa")
            return None













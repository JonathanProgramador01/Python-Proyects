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
ORIGIN_LOCACION = "MEX"


class Flight_Search:
    def __init__(self):
        self.data = None

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
            print(data)
            return data["data"][0]["iataCode"]
        except Exception as e:
            print("Algooo fallo con tu requesttt de solicitudesss ")
            return None



    def search_flight(self, iata_code: str, lowest_price:int,country: str,nonshop: str):

        ENDPOINT = "/v2/shopping/flight-offers"
        fecha_de_mañana = datetime.datetime.now() + datetime.timedelta(days=1)
        fecha_de_mañana = str(fecha_de_mañana).split(" ")[0]
        fecha_dentro_180_dias = datetime.datetime.now() + datetime.timedelta(days=(6*30)+1)
        fecha_dentro_180_dias = str(fecha_dentro_180_dias).split(" ")[0]

        parameters = {
            "originLocationCode": ORIGIN_LOCACION,
            "destinationLocationCode": iata_code,
            "departureDate": fecha_de_mañana,
            "returnDate": fecha_dentro_180_dias,
            "adults": 1,
            "nonStop": nonshop,
            "currencyCode": "MXN",
            "maxPrice": lowest_price,
        }
        solicutud = requests.get(url=URL+ENDPOINT, params=parameters, headers=self.HEADER)
        self.data = solicutud.json()
        print(self.data)

        try:
            print("PAIS: ",country)
            return self.get_the_cheapest_flight()

        except:
            print("Naa No existe ese pais checa bien tus argumentos  ") # este me sirve tanto como si susede algo con un pais que no exista o tanto como no alla viajes baratos con tu solicutud
            return None



    def get_the_cheapest_flight(self): # Osea si mi vuelo no tiene paradas
        #Si esta vacia no tengo vuelos
        if len(self.data["data"]) <= 0:
            print("Lo sientoo pero no tenemos vuelos tan baratosss")
            return None

       #######################################################
        cheaper = float(self.data["data"][0]["price"]["total"])
        stops = 0

        for data in self.data["data"]:
            precio = float(data["price"]["total"])
            if precio <= cheaper:
                cheaper = precio
                if len(data["itineraries"][0]["segments"]) == 1 and len(data["itineraries"][1]["segments"]) == 1:

                    print("DIRECTO")
                    Depature_airport_code = data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    Arrival_airport_code = data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                    outbound_date = data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    inbound_date = data["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
                    stops = 0


                else:
                    stops = len(data["itineraries"][0]["segments"])-1
                    stops += len(data["itineraries"][1]["segments"])-1


                    Depature_airport_code = data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    Arrival_airport_code = data["itineraries"][0]["segments"][len(data["itineraries"][0]["segments"])-1]["arrival"]["iataCode"]
                    outbound_date = data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    inbound_date = data["itineraries"][1]["segments"][1]["arrival"]["at"].split("T")[0]

        return cheaper, Depature_airport_code, Arrival_airport_code, outbound_date, inbound_date, stops























        # print(cheaper)
        # print(Depature_airport_code)
        # print(Arrival_airport_code)
        # print(outbound_date)
        # print(inbound_date)


        #return cheaper, Depature_airport_code, Arrival_airport_code, outbound_date, inbound_date







Object = Flight_Search()
a = Object.search_flight("PAR", 40_000, country="NYC", nonshop="false")
print(a)













#BKK no cuenta con viajes directos afuezas tiene+que hacer paradas

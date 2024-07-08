#ESTAAAAA ES DEEE SHEETT ##############################################


import requests
import os
from dotenv import load_dotenv
from pprint import pprint


#Esto es el que se encarga de mi archivo .env
load_dotenv()


SHEET_ENDPOINT_PRICES = os.environ.get("SHEET_ENDPOINT_PRICES")
SHEET_ENDPOINT_USERS = os.environ.get("SHEET_ENDPOINT_USERS")

HEADER = {
    "Authorization": os.environ.get("Authorization"),
}

class Data_Manager:
    def __init__(self):
        self.iatacode = []
        self.city = []
        self.lowest = []
        self.id = []
        self.gmails = []
    def get_info_sheet(self):
        """
        Optiene toda la informcion de mi sheet
        :return: toda la data de mi sheet
        """
        try:
            solicitud = requests.get(url=SHEET_ENDPOINT_PRICES, headers=HEADER)
            data = solicitud.json()
            print(data)
            return data["prices"]

        except:
            print("Algo anda mal cuando pedimos nuestra Api para SHEET")
            return None

    def editing_iata_code(self,iata_code: str, id: int):
        """
        edita mi fila de mi iata code
        :param iata_code:
        :param id:
        :return: None
        """
        DATA = {
            "price":{
                "iataCode": iata_code
            }
        }
        solicitud = requests.put(url=SHEET_ENDPOINT_PRICES+"/"+str(id), json=DATA, headers=HEADER)


    def get_emails(self):

        solicitud = requests.get(url=SHEET_ENDPOINT_USERS, headers=HEADER)
        for gmail in solicitud.json()["users"]:
            self.gmails.append(gmail["whatIsYourEmail ?"])
        print(self.gmails)
        

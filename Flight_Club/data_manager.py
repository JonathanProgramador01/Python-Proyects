#ESTAAAAA ES DEEE SHEETT ##############################################


import requests
import os
from dotenv import load_dotenv
from pprint import pprint


#Esto es el que se encarga de mi archivo .env
load_dotenv()


SHEET_ENDPOINT = "https://api.sheety.co/ba1e1384d057dcdbba4ec68247a110fd/viajesss/prices"
HEADER = {
    "Authorization": os.environ.get("Authorization"),
}

class Data_Manager:
    def __init__(self):
        self.iatacode = []
        self.city = []
        self.lowest = []
        self.id = []
    def get_info_sheet(self):
        """
        Optiene toda la informcion de mi sheet
        :return: toda la data de mi sheet
        """
        try:
            solicitud = requests.get(url=SHEET_ENDPOINT, headers=HEADER)
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
        solicitud = requests.put(url=SHEET_ENDPOINT+"/"+str(id), json=DATA, headers=HEADER)





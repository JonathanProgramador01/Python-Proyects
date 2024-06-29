import requests
from pprint import pprint
from dotenv import load_dotenv
import os


#COOMOOO ESSSTTEEEE ES DE MIIIIII SHEEEETTTT
# Load environment variables from .env file
load_dotenv()

KEY = os.environ["KEY"]
PUT = os.environ["PUT"]
GET = os.environ["GET"]



header = {
    "Authorization": f"Basic {KEY}"
}
class DataManager:
    def __init__(self):
        self.sheet = requests.get(url=GET, headers=header)
        self.id = 2

    def get_informacion_sheet(self):
        print(self.sheet.json())
        return {"sheet data": self.sheet.json()["prices"]}


    def put_iata_code(self,Codeiata):
        """
        ESTE ME PONEE EL IATA CODE EN MI ROW
        :param Codeiata:
        :return:NO ME REGRESAA NADAAA
        """
#TIENEEE UN ERRO EN EL DATOOO IDDDDD
        json = {
            "price": {
                "iataCode": Codeiata
            }
        }
        request = requests.put(url=PUT+str(self.id), json=json, headers=header)
        print(request.text)
        self.id += 1


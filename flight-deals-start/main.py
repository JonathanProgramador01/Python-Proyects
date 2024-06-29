#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

flight_search = FlightSearch() # este es para que se conecte con mi pagina de vuelos
data_manager = DataManager() # este es de mi sheet
sheet_data = data_manager.get_informacion_sheet() #aqui le paso toda la info de mi sheet
flight_data = FlightData()




List_Of_Iata_Code = [] #esta de aqui es endode se le van a almacenar mis iata code
List_Of_Lowest_Price = []
List_Of_countries = []


for data in sheet_data["sheet data"]: # este for es para mete mis iata code en una lista de mi sheet
    print(data)
    country = data["city"]
    price = data["lowestPrice"]

    iata_code = flight_search.Get_IATA_Code(country=country)
    List_Of_countries.append(country)
    List_Of_Iata_Code.append(iata_code)
    List_Of_Lowest_Price.append(price)


flight_data.get_the_cheaper_flight(city=List_Of_countries,iata_code=List_Of_Iata_Code,lowest_price=List_Of_Lowest_Price)

print(List_Of_countries)
print(List_Of_Lowest_Price)
print(List_Of_Iata_Code)
















# for country in List_Of_Iata_Code: Esto de aqui es para porner mi iata code en mi sheet
#     data_manager.put_iata_code(Codeiata=country)













































API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = "c0ifpayZQ1t33pj9y0zpzEw9Ibly"
token_type = "Bearer"


# print(API_SECRET)
#
# header = {
#     "'Authorization": f"Bearer {ACCESS_TOKEN}"
# }
# ENDPOINT = "/reference-data/locations/cities"
# URL = f"https://test.api.amadeus.com/v1{ENDPOINT}"
#
#



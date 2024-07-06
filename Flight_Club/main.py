import time
import notification_manager
from data_manager import Data_Manager
from flight_search import Flight_Search
from flight_data import Flight_Data


sheet = Data_Manager()
flight = Flight_Search()
data = Flight_Data()

info = sheet.get_info_sheet()
for fila in info:
    try: 
        sheet.city.append(fila["city"])
        sheet.iatacode.append(fila["iataCode"])
        sheet.lowest.append(fila["lowestPrice"])
        sheet.id.append(fila["id"])
    except:
        break

for i in range(len(sheet.city)):
    # ESTEEE FOR ES PARA PONER MIS IATA CODEEE
    sheet.iatacode[i] = flight.get_country_code(sheet.city[i])
    sheet.editing_iata_code(sheet.iatacode[i], sheet.id[i])
    time.sleep(1)


vuelos_baratos = []
#Este es para ver mivuelo mas baratooo DE CADDAA COUNTRYYY
for i in range(len(sheet.city)):
    cheapest = flight.search_flight(iata_code=sheet.iatacode[i], lowest_price=sheet.lowest[i],country=sheet.city[i])
    if cheapest != None:
        vuelos_baratos.append(cheapest)
    time.sleep(1)

print(vuelos_baratos)

## ESTA DE AQUII ES GENEROS PUEDEN SER VUELOOSSS EL VUELO MAS BARATO DE MI SOLICITUDD NO LO COMPARA SIMPLEMENTE ME LO DAAAA

for i in range(len(vuelos_baratos)):
    mensaje = f"""
low price alert! Only  ${vuelos_baratos[i][0]} to fly 
from {vuelos_baratos[i][1]} to {vuelos_baratos[i][2]}, on {vuelos_baratos[i][3]} 
until {vuelos_baratos[i][4]}.
    """
    notification_manager.send_whatsapp(mensaje)
    time.sleep(2)







####ESTOO DE AQUIII ME DA EL VUELOOO MAS MAS BARATO DE MI TABLA SI HAY DOS VUELOS QUE CUMPLEN MIS CONDICCIONES ESTE DETERMINA
### CUAL DE ELLAS ES MAS BARRATOO
# data.find_cheapest(vuelos_baratos) ### AQUI LE MANDO MI LISTA PARA QUE DE LOS SELECCIONADOS DETERMINE AUN QUIEN ES EL MAS VARATO
#
# mensaje = f"""
# low price alert! Only  £{data.cheapest} to fly
# from {data.Depature_airport_code} to {data.Arrival_airport_code}, on {data.outbound_date}
# until {data.inbound_date}.
# """
#
#
# notification_manager.send_whatsapp(mensaje)













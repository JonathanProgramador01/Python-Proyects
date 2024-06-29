import datetime
from flight_search import FlightSearch




class FlightData:
    #This class is responsible for structuring the flight data.
    """Esta se engarga de conectarce con fligh search para que tu
    le pases el iata code y la fecha y ella te regrese el vuelo mas barato

    """
    def __init__(self):

        self.flight_prices = []
        self.flight_search = FlightSearch()
        self.index_days = 1

    def get_the_cheaper_flight(self, city: list, iata_code : list, lowest_price: list):

        for i in range(6):
            flag = 0
            max = lowest_price[i] # mas es el que va a contener el valor minimo
            print(f"Buscando vuelo para {city[i]}: ")
            for j in range(30*6):
                date = datetime.datetime.now() + datetime.timedelta(days=self.index_days)
                date = date.strftime("%Y-%m-%d")
                self.index_days += 1


                cheaper = self.flight_search.Search_Fights(iata_code[i], date, max) # aqui supuestamente encontrando el viaje mas barato de ese dia
                if cheaper is not None:
                        flag = 1
                        max = cheaper

            if flag == 1: # esque si encontro

                print("precioo ",max)
                self.flight_prices.append(max)
            else:

                print("precioo  No se eoncontro un viaje mas barato al precio que estas pidiendo", max)
                self.flight_prices.append("No se eoncontro un viaje mas barato al precio que estas pidiendo")





prueba = FlightData()



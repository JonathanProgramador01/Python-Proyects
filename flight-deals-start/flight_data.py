import datetime
from flight_search import FlightSearch




class FlightData:
    #This class is responsible for structuring the flight data.
    """Esta se engarga de conectarce con fligh search para que tu
    le pases el iata code y la fecha y ella te regrese el vuelo mas barato

    """
    def __init__(self,iata_code: list, prices: list):

        self.flight_prices = []
        self.ita_code = iata_code
        self.flight_search = FlightSearch()
        date = datetime.datetime.now() + datetime.timedelta(days = 100)
        self.index_days = 1
        self.maxprice = prices # esta es de mi

        


        print(date.strftime("%Y-%m-%d"))

    def get_the_cheaper_flight(self,):

        for i in range(6):
            cheaper = self.maxprice[i]
            for j in range(30):
                date = datetime.datetime.now() + datetime.timedelta(days=self.index_days)
                date = date.strftime("%Y-%m-%d")
                self.index_days += 1




                if self.flight_search.Search_Fights(self.ita_code[i], date, self.maxprice[i])




#150.45

        









prueba = FlightData()



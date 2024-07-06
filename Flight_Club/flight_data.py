
class Flight_Data:
    def __init__(self):
        self.cheapest = None
        self.Depature_airport_code = None
        self.Arrival_airport_code = None
        self.outbound_date = None # fecha de salida
        self.inbound_date = None # fecha entrante


    def find_cheapest(self, data: list):

        self.cheapest = data[0][0]
        for i in range(len(data)):
            if self.cheapest >= data[i][0]:
                self.cheapest = data[i][0]
                self.Depature_airport_code = data[i][1]
                self.Arrival_airport_code = data[i][2]
                self.outbound_date = data[i][3]
                self.inbound_date = data[i][4]
        print(self.cheapest)
        print( self.Depature_airport_code)
        print( self.Arrival_airport_code)
        print( self.outbound_date)
        print( self.inbound_date)


class Flight:
    def __init__(self, flightId, source, destination, price):
        self.flightId = flightId
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result

    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def print_search_results(result):
    if result:
        print("\nSearch Results:")
        for flight in result:
            print(f"Flight ID: {flight.flightId}, From: {flight.source}, To: {flight.destination}, Price: {flight.price}")
    else:
        print("No flights found.")

def main():
    flight_table = FlightTable()

    flight_data = [
        ["AI161E90", "BLR", "BOM", 5600],
        ["BR161F91", "BOM", "BBI", 6750],
        ["AI161F99", "BBI", "BLR", 8210],
        ["VS171E20", "JLR", "BBI", 5500],
        ["AS171G30", "HYD", "JLR", 4400],
        ["AI131F49", "HYD", "BOM", 3499]
    ]

    for data in flight_data:
        flight = Flight(data[0], data[1], data[2], data[3])
        flight_table.add_flight(flight)

    while True:
        print("\nSearch Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            city = input("Enter the city: ")
            result = flight_table.search_by_city(city)
            print_search_results(result)
        elif choice == 2:
            source = input("Enter the source city: ")
            result = flight_table.search_by_source(source)
            print_search_results(result)
        elif choice == 3:
            source = input("Enter the source city: ")
            destination = input("Enter the destination city: ")
            result = flight_table.search_between_cities(source, destination)
            print_search_results(result)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

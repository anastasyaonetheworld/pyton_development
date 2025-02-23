if __name__ == "__main__":
    # Class Vehicle: A basic class that represents a general vehicle
    # It includes basic properties common to all vehicles (such as model, manufacturer, color....)
    class Vehicle:
        """
        A class representing a generic vehicle with basic attributes and methods.

        Attributes:
            manufactured (str): The manufacturer of the vehicle.
            stamp (str): The stamp or brand of the vehicle.
            model (str): The model name or number of the vehicle.
            number_car (str): The vehicle's unique number identifier.
            colour (str): The color of the vehicle.
            number_of_seats (int): The number of seats in the vehicle.
        """

        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int) -> None:
            """
            Initializes a new Vehicle object with the provided attributes.
            """
            self.manufactured = manufactured
            self.stamp = stamp
            self.model = model
            self.number_car = number_car
            self.colour = colour
            self.number_of_seats = number_of_seats

        def __str__(self) -> str:
            """
            Returns a simple string description of the vehicle, including its model,
            stamp, and manufacturer.
            """
            return f"Car model is {self.model}, stamp is {self.stamp}, manufactured is {self.manufactured}."

        def __repr__(self) -> str:
            """
            Returns a detailed string representation of the vehicle with all its attributes.
            """
            return (f"Vehicle(manufactured={self.manufactured}, stamp={self.stamp}, "
                    f"model={self.model}, number_car={self.number_car}, "
                    f"colour={self.colour}, number_of_seats={self.number_of_seats})")

        def is_electric(self) -> bool:
            """
            Checks if the vehicle is electric. The base vehicle is not electric by default.
            """
            return False

        def get_fuel_type(self) -> str:
            """
            Returns the fuel type of the vehicle. The default vehicle has an unknown fuel type.
            """
            return "Unknown"

        def get_max_speed(self) -> int:
            """
            Returns the maximum speed of the vehicle. The default maximum speed is 0.
            """
            return 0


    # Class Passenger_car: Extends Vehicle to provide specific attributes and functions for passenger cars
    # This class adds the trunk size and overrides the max speed function for passenger vehicles.
    class Passenger_car(Vehicle):
        """
        A subclass of Vehicle that represents a passenger car.
        """

        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int, trunk_size_in_volume: int) -> None:
            """
            Initializes a new Passenger_car object with the provided attributes,
            including those inherited from Vehicle and the trunk size.
            """
            super().__init__(manufactured, stamp, model, number_car, colour, number_of_seats)
            self.trunk_size_in_volume = trunk_size_in_volume

        def __repr__(self) -> str:
            """
            Returns a detailed string representation of the passenger car, including
            the trunk size along with all other vehicle attributes.
            """
            return (f"Passenger_car(manufactured={self.manufactured}, stamp={self.stamp}, "
                    f"model={self.model}, number_car={self.number_car}, "
                    f"colour={self.colour}, number_of_seats={self.number_of_seats}, "
                    f"trunk_size_in_volume={self.trunk_size_in_volume})")

        def get_max_speed(self) -> int:
            """
            Returns the maximum speed of the passenger car.
            Passenger cars typically have higher max speeds compared to other vehicles.
            """
            return 200


    # Class Cargo_truck: Extends Vehicle to represent cargo trucks with specific attributes
    # This class adds the container size and overrides the max speed function for cargo trucks.
    class Cargo_truck(Vehicle):
        """
        A subclass of Vehicle that represents a cargo truck.
        """

        def __init__(self, manufactured: str, stamp: str, model: str, number_car: str,
                     colour: str, number_of_seats: int, container_size_in_volume: int) -> None:
            """
            Initializes a new Cargo_truck object with the provided attributes,
            including those inherited from Vehicle and the container size.
            """
            super().__init__(manufactured, stamp, model, number_car, colour, number_of_seats)
            self.container_size_in_volume = container_size_in_volume

        def __repr__(self) -> str:
            """
            Returns a detailed string representation of the cargo truck, including
            the container size along with all other vehicle attributes.
            """
            return (f"Cargo_truck(manufactured={self.manufactured}, stamp={self.stamp}, "
                    f"model={self.model}, number_car={self.number_car}, "
                    f"colour={self.colour}, number_of_seats={self.number_of_seats}, "
                    f"container_size_in_volume={self.container_size_in_volume})")

        def get_max_speed(self) -> int:
            """
            Returns the maximum speed of the cargo truck.
            Cargo trucks typically have lower maximum speeds due to their size and weight.
            """
            return 120
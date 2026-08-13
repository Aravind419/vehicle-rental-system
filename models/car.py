
from .vehicle import Vehicle

class Car(Vehicle):
    
    def __init__(self, vehicle_number,brand,rental_price,number_of_seats):
        super().__init__(vehicle_number,brand,rental_price)
        self.number_of_seats = number_of_seats
    
    def display_details(self):
         return (
            f"Vehicle Number: {self.vehicle_number}\n"
            f"Brand: {self.brand}\n"
            f"Rental Price/Day: {self.rental_price}\n"
            f"Number of Seats: {self.number_of_seats}"
        )
    def calculate_rental(self, days):
        rental = self.rental_price * days
        
        if days >= 7:
            discount = rental * 10 / 100
            rental = rental - discount
        return rental
    

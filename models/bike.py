from .vehicle import Vehicle

class Bike(Vehicle):
    
    def __init__(self, vehicle_number, brand, rental_price, engine_capacity):
        super().__init__(vehicle_number,brand,rental_price)
        self.engine_capacity = engine_capacity
        
    def display_details(self):
        return(
            f"Vehicle Number: {self.vehicle_number}\n"
            f"Brand: {self.brand}\n"
            f"Rental Price/Day: {self.rental_price}\n"
            f"Engine Capacity: {self.engine_capacity}"
        )
    
    def calculate_rental(self,days):
        rental = self.rental_price * days
        
        # discount if rent more than 4
        if days >= 5:
            discount = rental * 5 / 100
            rental = rental - discount
        return rental

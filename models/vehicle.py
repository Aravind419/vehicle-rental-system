class Vehicle:
    def __init__(self, vehicle_number, brand, rental_price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.rental_price = rental_price
        
    def display_details(self):
        return f"Vehicle brand is {self.brand} and vehicle number is {self.vehicle_number} rent per day is {self.rental_price}"
    
    def calculate_rental(self, days):
        return self.rental_price * days
    
rental_day = int(input("How many days need vehicle for rent: "))

car = Vehicle("123XXyz","BMW",1000)
vehicle_info = car.display_details()
rent = car.calculate_rental(rental_day)
print(vehicle_info)
print(f"rent for {rental_day} is {rent}")
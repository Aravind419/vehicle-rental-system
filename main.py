from models.car import Car  
from models.bike import Bike

def main():
    car1 = Car("CAR1", "BMW", 1000, 5)
    car2 = Car("CAR2", "BMW", 900, 4)
    
    bike1 = Bike("BIKE1", "Yamaha", 800, "150cc")
    bike2 = Bike("BIKE2", "Honda", 600, "125cc")
    
    vehicles = [car1, car2, bike1, bike2]
    days = int(input("Enter rental duration days: "))
    
    print("======= Vehicle Rental Details =======")
    
    for vehicle in vehicles:
        print("----------------------")
        print(vehicle.display_details())
        rental_amount = vehicle.calculate_rental(days)
        print(f"Rental for {days} days: {rental_amount:.2f}")
        
if __name__ == "__main__":
    main()
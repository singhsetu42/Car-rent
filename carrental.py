class Car:
    def __init__(self, car_type, price_per_day):
        self.car_type = car_type
        self.price_per_day = price_per_day
        self.is_available = True

    def __str__(self):
        return f"{self.car_type} - ${self.price_per_day}/day"


class CarRentalSystem:
    def __init__(self):
        self.cars = {
            "sedan": Car("sedan", 50),
            "suv": Car("suv", 70),
            "convertible": Car("convertible", 100),
            "truck": Car("truck", 80)
        }

    def display_availability(self):
        print("Car types, availability, and prices:")
        for car_type, car in self.cars.items():
            print(f"{car_type}: {car.is_available} cars available at ${car.price_per_day}/day")

    def rent_car(self, car_type):
        if self.cars[car_type].is_available:
            self.cars[car_type].is_available = False
            print(f"Successfully rented a {car_type}")
        else:
            print(f"Sorry, all {car_type}s are currently unavailable")

    def return_car(self, car_type):
        if not self.cars[car_type].is_available:
            self.cars[car_type].is_available = True
            print(f"Successfully returned a {car_type}")
        else:
            print(f"Sorry, there are no {car_type}s currently rented")

    def user_input(self):
        while True:
            print("\nOptions:")
            print("1. Display availability")
            print("2. Rent a car")
            print("3. Return a car")
            print("4. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_availability()
            elif choice == "2":
                car_type = input("Enter the car type you want to rent: ")
                self.rent_car(car_type)
            elif choice == "3":
                car_type = input("Enter the car type you want to return: ")
                self.return_car(car_type)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    car_rental_system = CarRentalSystem()
    car_rental_system.user_input()
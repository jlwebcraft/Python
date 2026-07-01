"""
Create a Car Object with the following initial attributes:
fuel
mileage
km_run
fuel_capacity

And with the following methods

- run() that takes in a km as a parameter, this method should firstly check if you have enough fuel to run that kilometers
  based on the mileage. Then if it can, it should increase the km_run by run and display a successfully run message.

- change_mileage() that takes in new_mileage as a parameter and changes it's mileage

- reset_km_run() that resets the km_run to 0.

- refill() that takes in litres as a parameter, this method should firstly check if the current fuel plus the new litres of
  fuel added would exceed the fuel_capacity or not. If not, then it should, add the fuel, and display a successful refill message.

- change_fuel_capacity() that takes in new_fuel_capacity as a parameter and changes it's fuel_capacity.

- display_info() method that prints the detailed information about the car and it's condition.
"""


class car:
    company_name = "Tata"
    estd = "2025"

    def car_create(self,fuel,mileage,km_run,fuel_capacity):
        self.capacity = 17
        self.fuel = fuel
        self.mileage = mileage
        self.km_run = km_run
        self.fuel_capacity = fuel_capacity

    def run(self,run):
        if run <= self.capacity * self.mileage:
            print(f"Car ran {run} km")
            self.capacity -= run / self.mileage
            self.km_run += run
            print(f"Updated km is {self.km_run}")
            print(f"New fuel capacity: {self.capacity}")
        else:
            print("Not enough fuel")

    def change_mileage(self,change_mileage):
        self.mileage=change_mileage
        print(f"new mileage is: {self.mileage}")

    def reset_km_run(self):
        self.km_run=0
        print(f"KM ran successfully updated to: {self.km_run}")

    def refill(self,refill):
        if(refill+self.capacity<=self.fuel_capacity):
            self.capacity += refill
            print(f"car successfully refilled updated fuel capacity is: {self.capacity}")
        else:
            print("It exceeds Car fuel capacity")

    def change_fuel_capacity(self, change_fuel_capacity):
        self.fuel_capacity = change_fuel_capacity()

    def display_info(self):

        print("fuel:", self.fuel)
        print("mileage:", self.mileage)
        print("km_run:", self.km_run)
        print("fuel_capacity:", self.fuel_capacity)
        print("Available fuel:", self.capacity)

Altroz=car()
Altroz.car_create("diesel", 24, 2913, 37)
Altroz.run(10)
Altroz.change_mileage(34)
Altroz.reset_km_run()
Altroz.refill(30)
print()
print()

print("Car info are displayed below:")
print(f"{Altroz.company_name}, {Altroz.estd}")
Altroz.display_info()
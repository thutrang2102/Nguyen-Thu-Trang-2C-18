class Car:
   def __init__(self, __year_model, __make):
       self.__year_model = __year_model
       self.__make = __make
       self.__speed = 0

       # set the arguments for speed,year, and make

   def set_year_model(self, year):
       self.__year_model = year

   def set_make(self, make):
       self.__make = make

   def set_speed(self, speed):
       self.__speed = 0

       # the returns for speed, year, and make

   def get_year_model(self):
       return self.__year_model

   def get_make(self):
       return self.__make

   def get_speed(self):
       return self.__speed

   def accelerate(self):
       self.__speed += 5

   def brake(self):
       self.__speed -= 5

   def get_speed(self):
       return self.__speed
   def printResult(self):
       print( 'Car year:', self.__year_model, ', car make:', self.__make, 'and speed is: ')
car = Car("S650 2020", "Maybach")
car.printResult()

for i in range(5):
   car.accelerate()
   print("Current Speed:", car.get_speed())

for i in range(5):
   car.brake()
   print("Current speed after brake:", car.get_speed())
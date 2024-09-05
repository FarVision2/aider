import unittest
from tests.fixtures.sample_code_base.sample import Car, Garage

class TestCar(unittest.TestCase):
    def test_accelerate(self):
        car = Car("Toyota", "Corolla", 2020)
        car.accelerate(30)
        self.assertEqual(car.speed, 30)

    def test_brake(self):
        car = Car("Toyota", "Corolla", 2020)
        car.accelerate(30)
        car.brake(10)
        self.assertEqual(car.speed, 20)

    def test_honk(self):
        car = Car("Toyota", "Corolla", 2020)
        self.assertEqual(car.honk(), None)

class TestGarage(unittest.TestCase):
    def test_add_car(self):
        garage = Garage()
        car = Car("Toyota", "Corolla", 2020)
        garage.add_car(car)
        self.assertIn(car, garage.cars)

    def test_remove_car(self):
        garage = Garage()
        car = Car("Toyota", "Corolla", 2020)
        garage.add_car(car)
        garage.remove_car(car)
        self.assertNotIn(car, garage.cars)

    def test_list_cars(self):
        garage = Garage()
        car1 = Car("Toyota", "Corolla", 2020)
        car2 = Car("Tesla", "Model 3", 2022)
        garage.add_car(car1)
        garage.add_car(car2)
        self.assertEqual(len(garage.cars), 2)

if __name__ == "__main__":
    unittest.main()

import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_childager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(11), 50)

    def test_teenager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def test_midager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(59), 150)

    def test_oldager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    def test_negativeager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")

    def test_rezeroager_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), "50")

if __name__ == '__main__':
    unittest.main()

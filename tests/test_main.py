import unittest
from src import dice

class TestDice(unittest.TestCase):
    def test_roll_dice(self):
        rolls = dice.roll_dice(5)
        self.assertEqual(len(rolls), 5)
        for roll in rolls:
            self.assertIn(roll, range(1, 7))
    
    def test_parse_input_valid(self):
        self.assertEqual(dice.parse_input("3"), 3)
    
    def test_parse_input_invalid(self):
        with self.assertRaises(ValueError):
            dice.parse_input("7")

if __name__ == "__main__":
    unittest.main()
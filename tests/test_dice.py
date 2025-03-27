import unittest
from unittest.mock import patch
from src import dice  # Assuming the code is in a module named dice.py

class TestDice(unittest.TestCase):
    def setUp(self):
        """Setup test data using module constants."""
        self.single_die_1 = [dice.DICE_ART[1]]
        self.two_dice_1_2 = [dice.DICE_ART[1], dice.DICE_ART[2]]
        self.three_dice_1_2_3 = [
            dice.DICE_ART[1], dice.DICE_ART[2], dice.DICE_ART[3]]


    def test_roll_dice(self):
        # Test that the correct number of dice are rolled
        rolls = dice.roll_dice(5)
        self.assertEqual(len(rolls), 5)
        for roll in rolls:
            self.assertIn(roll, range(1, 7))
            
        # Test edge cases
        self.assertEqual(len(dice.roll_dice(1)), 1)
        self.assertEqual(len(dice.roll_dice(6)), 6)


    def test_parse_input_valid(self):
        # Test all valid inputs
        for i in range(1, 7):
            self.assertEqual(dice.parse_input(str(i)), i)


    def test_parse_input_invalid(self):
        # Test various invalid inputs
        with self.assertRaises(ValueError):
            dice.parse_input("0")
        with self.assertRaises(ValueError):
            dice.parse_input("7")
        with self.assertRaises(ValueError):
            dice.parse_input("foo")
        with self.assertRaises(ValueError):
            dice.parse_input("")
        with self.assertRaises(ValueError):
            dice.parse_input("3.5")


    def test_get_dice_faces(self):
        # Test that correct faces are returned for various inputs
        test_cases = [
            ([1], self.single_die_1),
            ([1, 2], self.two_dice_1_2),
            ([3, 3, 3], [dice.DICE_ART[3]] * 3),
        ]


        for input_values, expected in test_cases:
            with self.subTest(input_values=input_values):
                result = dice._get_dice_faces(input_values)
                self.assertEqual(result, expected)


    def test_generate_dice_faces_rows(self):
        # Test single die
        expected_single = list(dice.DICE_ART[1])
        self.assertEqual(dice._generate_dice_faces_rows(
            self.single_die_1), expected_single)
        
        # Test two dice
        expected_two = [
            dice.DICE_ART[1][0] + " " + dice.DICE_ART[2][0],
            dice.DICE_ART[1][1] + " " + dice.DICE_ART[2][1],
            dice.DICE_ART[1][2] + " " + dice.DICE_ART[2][2],
            dice.DICE_ART[1][3] + " " + dice.DICE_ART[2][3],
            dice.DICE_ART[1][4] + " " + dice.DICE_ART[2][4],
        ]
        self.assertEqual(dice._generate_dice_faces_rows(
            self.two_dice_1_2), expected_two)


    def test_generate_dice_faces_diagram(self):
        # Test with known values
        test_values = [1, 2, 3]
        result = dice.generate_dice_faces_diagram(test_values)
        
        # Split into lines for easier verification
        lines = result.split('\n')
        
        # Verify header
        header = lines[0]
        self.assertTrue(header.startswith('~'))
        self.assertTrue(header.endswith('~'))
        self.assertIn('RESULTS', header)
        
        # Verify body uses the correct dice faces
        expected_rows = dice._generate_dice_faces_rows(
            self.three_dice_1_2_3)
        for i, line in enumerate(lines[1:]):
            self.assertEqual(line, expected_rows[i])


    @patch('random.randint')
    def test_roll_dice_randomness(self, mock_randint):
        # Test that random.randint is called correctly
        mock_randint.return_value = 3
        result = dice.roll_dice(2)
        self.assertEqual(result, [3, 3])
        self.assertEqual(mock_randint.call_count, 2)
        mock_randint.assert_called_with(1, 6)


if __name__ == "__main__":
    unittest.main()
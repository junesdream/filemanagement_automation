import unittest
from data_cleaner import DataCleaner

class TestDataCleaner(unittest.TestCase):
    def test_clean_data(self):
        data = [
            {"city": "Berlin", "temperature": -15, "humidity": 95},
            {"city": "Munich", "temperature": 10, "humidity": 85},
            {"city": "Hamburg", "temperature": -5, "humidity": 40},
        ]
        cleaner = DataCleaner(data)
        cleaned_data = cleaner.clean_data()

        self.assertEqual(len(cleaned_data), 2, "Data cleaning failed!")
        for entry in cleaned_data:
            self.assertGreater(entry["temperature"], -10, "Temperature filter failed!")
            self.assertLessEqual(entry["humidity"], 90, "Humidity filter failed!")

if __name__ == "__main__":
    unittest.main()

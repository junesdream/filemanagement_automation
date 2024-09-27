import unittest
import os
from data_fetcher import DataFetcher

class TestDataFetcher(unittest.TestCase):
    def test_fetch_data(self):
        fetcher = DataFetcher()
        data = fetcher.fetch_data()
        # Check if data is not empty
        self.assertGreater(len(data), 0, "Data fetching failed!")
        # Check if expected keys are present in the data
        for entry in data:
            self.assertIn("city", entry, "Key 'city' not found in fetched data!")
            self.assertIn("temperature", entry, "Key 'temperature' not found in fetched data!")
            self.assertIn("humidity", entry, "Key 'humidity' not found in fetched data!")

    def test_save_data(self):
        fetcher = DataFetcher()
        data = fetcher.fetch_data()
        test_data_dir = "data"
        test_file = f"{test_data_dir}/test_weather_data.json"

        # Ensure the 'data' directory exists
        if not os.path.exists(test_data_dir):
            os.makedirs(test_data_dir)

        fetcher.save_data(test_file)

        # Check if the file was created
        self.assertTrue(os.path.exists(test_file), "Data file was not saved!")

        # Cleanup the test file after testing
        if os.path.exists(test_file):
            os.remove(test_file)

if __name__ == "__main__":
    unittest.main()

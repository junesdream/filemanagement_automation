import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_reporter import DataReporter
import unittest

class TestDataReporter(unittest.TestCase):
    def test_generate_report(self):
        data = [
            {"city": "Berlin", "temperature": 15, "humidity": 70},
            {"city": "Munich", "temperature": 10, "humidity": 80},
        ]
        reporter = DataReporter(data)
        test_report_dir = "reports"
        test_report_file = f"{test_report_dir}/test_weather_report.txt"

        # Ensure the 'reports' directory exists
        if not os.path.exists(test_report_dir):
            os.makedirs(test_report_dir)

        reporter.generate_report(test_report_file)

        # Check if the report file was created
        self.assertTrue(os.path.exists(test_report_file), "Report file was not generated!")

        # Check if the file contains content
        with open(test_report_file, "r") as file:
            content = file.read()
            self.assertGreater(len(content), 0, "Report content is empty!")

        # Cleanup the test report file after testing
        if os.path.exists(test_report_file):
            os.remove(test_report_file)

if __name__ == "__main__":
    unittest.main()

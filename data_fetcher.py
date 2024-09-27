import json
import random

class DataFetcher:
    def __init__(self):
        self.data = []

    # Simulate fetching data from an API (for example, weather data)
    def fetch_data(self):
        self.data = [
            {"city": "Berlin", "temperature": random.uniform(-5, 30), "humidity": random.randint(20, 100)},
            {"city": "Munich", "temperature": random.uniform(-5, 30), "humidity": random.randint(20, 100)},
            {"city": "Hamburg", "temperature": random.uniform(-5, 30), "humidity": random.randint(20, 100)}
        ]
        return self.data

    # Save fetched data into a JSON file
    def save_data(self, file_name="data.json"):
        with open(file_name, "w") as file:
            json.dump(self.data, file, indent=4)

# Example usage
fetcher = DataFetcher()
data = fetcher.fetch_data()
fetcher.save_data("weather_data.json")

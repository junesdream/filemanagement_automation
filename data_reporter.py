class DataReporter:
    def __init__(self, data):
        self.data = data

    # Create a report as a simple text file summarizing the data
    def generate_report(self, file_name="report.txt"):
        with open(file_name, "w") as report:
            for entry in self.data:
                report.write(f"City: {entry['city']}, Temperature: {entry['temperature']}°C, Humidity: {entry['humidity']}%\n")

# Example usage

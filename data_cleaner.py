class DataCleaner:
    def __init__(self, data):
        self.data = data

    # Clean the data by removing records with temperature below -10 or humidity > 90
    def clean_data(self):
        cleaned_data = [entry for entry in self.data if entry["temperature"] > -10 and entry["humidity"] <= 90]
        return cleaned_data

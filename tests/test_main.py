import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_fetcher import DataFetcher
from data_cleaner import DataCleaner
from data_reporter import DataReporter
from email_sender import EmailSender

def main():
    # Fetching data
    fetcher = DataFetcher()
    data = fetcher.fetch_data()
    fetcher.save_data("data/weather_data.json")

    # Cleaning data
    cleaner = DataCleaner(data)
    cleaned_data = cleaner.clean_data()

    # Generating report
    reporter = DataReporter(cleaned_data)
    reporter.generate_report("reports/weather_report.txt")

    # Sending report via email
    email_sender = EmailSender("recipient@example.com", "Weather Report", "Please find the weather report attached.")
    email_sender.send_email()

if __name__ == "__main__":
    main()

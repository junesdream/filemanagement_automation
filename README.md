# File Management Automation Project

This is a Python project that automates data fetching, cleaning, reporting, and emailing using plain Python.

## Features
- Fetches weather data (simulated API)
- Cleans data (removes entries with extreme values)
- Generates a report
- (Simulated) Sends the report via email

## Project Structure
. ├── data_fetcher.py # Fetches data (simulated) ├── data_cleaner.py # Cleans data ├── data_reporter.py # Generates reports ├── email_sender.py # Simulates sending email ├── main.py # Runs the full workflow ├── tests/ # Contains test cases │ ├── test_data_fetcher.py │ ├── test_data_cleaner.py │ ├── test_data_reporter.py │ └── test_email_sender.py ├── requirements.txt # Python dependencies └── .github/workflows/ci.yml # GitHub Actions CI configuration

## Setup
1. Clone this repository.
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main program:
   ```bash 
   python main.py
   ```
4. To run the tests
   ```bash 
   python -m unittest discover -s tests
   ```
## CI
This project uses GitHub Actions for continuous integration. It automatically runs tests on every push or pull request to the main branch.

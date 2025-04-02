Weather Analysis and Land Assessment

Overview

This Python based application provides weather forecasts, land assessment insights, and subscription-based user access. It uses the OpenWeatherMap API to retrieve weather data and provides analysis on temperature and rainfall trends. The application also includes a user registration system with subscription validation stored in an SQLite database.

Features

User Registration: Users can register using their full name and a government-issued ID card.

Subscription System: Users pay a yearly subscription fee of $5 to access weather data.

Weather Forecast: Fetches and displays weather conditions for any location.

Land Assessment: Analyzes land conditions based on temperature and rainfall data.

Data Visualization: Generates graphs for temperature and rainfall trends.

Technologies Used

Python 3

SQLite (for user database management)

OpenWeatherMap API (for weather data retrieval)

Matplotlib (for data visualization)

Requests (for API calls)

Installation and Setup

Prerequisites

Ensure you have Python 3 installed along with the required dependencies:

pip install requests matplotlib

API Key Setup

This application uses OpenWeatherMap API. Obtain an API key from OpenWeatherMap and replace API_KEY in the script.

Running the Application

Clone the repository:

git clone https://github.com/rcyubahiro/Agripioneers.git
cd weather-land-analysis

Run the Python script:

python3 weather.py

Usage

1. User Registration

New users can register by entering their full name and ID card number.

They must make a payment to activate their subscription.

2. Subscription Verification

Existing users can log in with their ID card number to check their subscription status.

3. Weather Forecast & Land Analysis

Users enter a location (e.g., Kigali, Rwanda).

The application retrieves and displays a 5-day forecast.

Land assessment is provided based on temperature and rainfall trends.

Users can choose to visualize the data using graphs.

Example Output

 Weather Analysis and Land Assessment 
1. New User Registration
2. Existing User Login
Select option (1/2): 2
Enter your ID card number: 123456789

Welcome back, John Doe!
Your subscription is valid until 2025-03-30.

Enter location to analyze (city, country): Nairobi, Kenya

 Weather Forecast 
Date: 2025-03-31  Temp: 22.5°C | Rain: 5 mm
Date: 2025-04-01  Temp: 24.0°C | Rain: 0 mm
...
 Land Analysis:
Suitable for agriculture. Ideal conditions for crops.

Troubleshooting

Database errors: Ensure weather_users.db exists and is not corrupted.

API request failures: Check internet connection and verify the API key.

Matplotlib errors: Ensure matplotlib is installed using pip install matplotlib.

## Author
Developed by Team 3 

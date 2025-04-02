#!/usr/bin/env python3
import requests
import json
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime, timedelta

# Database setup
conn = sqlite3.connect('weather_users.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    id_card TEXT UNIQUE NOT NULL,
    subscription_date TEXT,
    subscription_end TEXT,
    payment_status BOOLEAN DEFAULT FALSE
)
''')
conn.commit()


            check_exit(choice)

            if choice == '1':
                if not register_user():
                    continue
                id_card = input("\nPlease enter your ID card number to continue: ")
                check_exit(id_card)
            elif choice == '2':
                id_card = input("Enter your ID card number: ")
                check_exit(id_card)
            else:
                print("Invalid selection")
                continue

            if not check_subscription(id_card):
                continue

            while True:
                location = input("\nEnter location to analyze (city, country) or 'Q' to quit: ")
                check_exit(location)

                weather_data = get_weather_data(location)
                if not weather_data:
                    continue

                display_weather_forecast(weather_data)

                # Calculate averages for land analysis
                temps = [entry['main']['temp'] for entry in weather_data['list']]
                rains = [entry.get('rain', {}).get('3h', 0) for entry in weather_data['list']]
                avg_temp = sum(temps)/len(temps)
                avg_rain = sum(rains)/len(rains)

                print("\n--- Land Analysis ---")
                print(analyze_land(avg_rain, avg_temp))

                graph_choice = input("\nShow weather graphs? (y/n/Q): ").upper()
                check_exit(graph_choice)
                if graph_choice == 'Y':
                    plot_weather_data(weather_data)
                elif graph_choice == 'Q':
                    break
    finally:
        conn.close()

if __name__ == "__main__":
    main()
# API configuration
API_KEY = "86d63794f43673e581ee542a46a9d96c"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
SUBSCRIPTION_PRICE = 5  # USD per year          

def register_user():
    """Register a new user with ID verification and subscription payment"""
    print("\n--- User Registration ---")
    print("(Press 'Q' at any time to quit)\n")
    name = input("Enter your full name: ")
    check_exit(name)
    
    id_card = input("Enter your government-issued ID card number: ")
    check_exit(id_card)
    
    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE id_card=?", (id_card,))
    if cursor.fetchone():
        print("Error: This ID card is already registered.")
        return False
    
    # Payment processing (simulated)
    print(f"\nSubscription Price: ${SUBSCRIPTION_PRICE} per year")
    payment = input("Enter payment amount (USD): ")
    check_exit(payment)
    
    try:
        payment = float(payment)
        if payment < SUBSCRIPTION_PRICE:
            print("Error: Insufficient payment amount.")
            return False
    except ValueError:
        print("Error: Invalid payment amount.")
        return False
    
    # Calculate subscription dates
    today = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
    
    # Store user data
    cursor.execute('''
    INSERT INTO users (name, id_card, subscription_date, subscription_end, payment_status)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, id_card, today, end_date, True))
    conn.commit()
    
    print("\nRegistration successful!")
    print(f"Thank you for subscribing, {name}!")
    print(f"Your subscription is valid until {end_date}")
    return True
<<<<<<< HEAD
def get_weather_data(location):
    """Fetch weather data from OpenWeatherMap API"""
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
    return None
=======
def check_subscription(id_card):
    """Check if user has an active subscription"""
    cursor.execute('''
    SELECT name, subscription_end FROM users 
    WHERE id_card=? AND payment_status=1 AND subscription_end >= date('now')
    ''', (id_card,))
    user = cursor.fetchone()
    
    if user:
        print(f"\nWelcome back, {user[0]}!")
        print(f"Your subscription is valid until {user[1]}")
        return True
    
    print("\nError: No active subscription found.")
    print("Please register and pay the subscription fee to access the service.")
    return FalseO
def get_weather_data(location):
    """Fetch weather data from OpenWeatherMap API"""
    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
    return None

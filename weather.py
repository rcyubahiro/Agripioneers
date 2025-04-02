<<<<<<< HEAD
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
SUBSCRIPTION_PRICE = 5  # USD per year                                                                                                                                                    207,1         Bot 
=======
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


       
  
 
  
>>>>>>> c7e2005b8194590f413e6ef46c58e26ccea9dc06

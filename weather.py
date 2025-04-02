def main():
    """Main program flow"""
    try:
        while True:
            print("\n=== Weather Analysis and Land Assessment ===")
            print("1. New User Registration")
            print("2. Existing User Login")
            print("Q. Quit Program")
            choice = input("\nSelect option (1/2/Q): ")
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

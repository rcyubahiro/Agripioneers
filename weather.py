import pymysql
import requests

# Database Credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "rob",
    "database": "Robert",
    "cursorclass": pymysql.cursors.DictCursor  # Fetch results as dictionaries
}

# OpenWeatherMap API
API_KEY = "86d63794f43673e581ee542a46a9d96c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to connect to MySQL database
def connect_db():
    try:
        return pymysql.connect(**DB_CONFIG)
    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")
        return None

# Function to fetch weather data from API
def get_weather(location):
    params = {"q": location, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data. Status code: {response.status_code}")
        return None

# Function to save user data
def save_user(name, location):
    db = connect_db()
    if not db:
        return
    try:
        with db.cursor() as cursor:
            query = "INSERT INTO users (name, location) VALUES (%s, %s)"
            cursor.execute(query, (name, location))
            db.commit()
            print("User registered successfully!")
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    finally:
        db.close()

# Function to save weather data
def save_weather(user_id, weather_condition, temperature, humidity):
    db = connect_db()
    if not db:
        return
    try:
        with db.cursor() as cursor:
            query = "INSERT INTO weather (user_id, condition, temperature, humidity) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (user_id, weather_condition, temperature, humidity))
            db.commit()
    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
    finally:
        db.close()

# Function to get recommendations
def get_recommendations(weather_condition):
    recommendations = {
        "Clouds": "Consider planting leafy greens such as lettuce and spinach.",
        "Rain": "Opt for water-tolerant plants like rice and taro.",
        "Sunny": "Great conditions for tomatoes, peppers, and sunflowers.",
        "Snow": "Consider indoor gardening with herbs and microgreens."
    }
    return recommendations.get(weather_condition, "No recommendations available.")

# Function to get plant recommendations
def get_plants(weather_condition):
    plants = {
        "Clouds": ["Lettuce", "Spinach", "Cabbage"],
        "Rain": ["Rice", "Taro", "Watercress"],
        "Sunny": ["Tomatoes", "Peppers", "Sunflowers"],
        "Snow": ["Herbs", "Microgreens", "Mushrooms"]
    }
    return plants.get(weather_condition, ["No plants available."])

# Function to get gardening tips
def get_gardening_tips(weather_condition):
    tips = {
        "Clouds": ["Ensure proper drainage to avoid root rot.", "Use organic mulch to retain moisture."],
        "Rain": ["Avoid overwatering as soil is already saturated.", "Choose raised beds to prevent waterlogging."],
        "Sunny": ["Water early in the morning to prevent evaporation.", "Use shade cloth for delicate plants."],
        "Snow": ["Use grow lights for indoor plants.", "Maintain indoor humidity to prevent plant stress."]
    }
    return tips.get(weather_condition, ["No tips available."])

# Main function
def main():
    name = input("Enter your name: ")
    location = input("Enter your location (city, country): ")
    save_user(name, location)
    
    weather_location = input("Enter your location for weather updates: ")
    weather_data = get_weather(weather_location)
    
    if weather_data:
        weather_condition = weather_data["weather"][0]["main"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        
        print("\n--- Weather Information ---")
        print(f"Weather Condition: {weather_condition}")
        
        recommendation = get_recommendations(weather_condition)
        print("\nRecommendation:", recommendation)
        
        plants = get_plants(weather_condition)
        print("\nSelect a plant:")
        for i, plant in enumerate(plants, 1):
            print(f"{i}. {plant}")
        
        choice = int(input("Enter the number of your chosen plant: "))
        selected_plant = plants[choice - 1]
        print(f"You have selected: {selected_plant}")
        
        gardening_tips = get_gardening_tips(weather_condition)
        print("\nGardening Tips:")
        for tip in gardening_tips:
            print(f"- {tip}")
        
    else:
        print("No weather data available.")

if __name__ == "__main__":
    main()


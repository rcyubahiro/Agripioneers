

**## Description**
This is a command-line-based Weather and Gardening Recommendation application. The program fetches weather data for a given location, recommends suitable plants based on the weather condition, provides gardening tips, and allows users to interact with the database for storing their choices.

## Features
- User registration
- Fetch real-time weather data using OpenWeatherMap API
- Store user and weather information in MySQL database
- Provide plant recommendations based on weather conditions
- Offer gardening tips based on the selected plant and weather
- Interactive selection and data storage

## Technologies Used
- Python
- MySQL (via pymysql library)
- OpenWeatherMap API

## Database Schema
The application requires the following tables in MySQL:

### users Table
sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL
);


### weather Table
sql
CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    condition VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);


### plants Table
sql
CREATE TABLE plants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    weather_condition VARCHAR(50)
);


### recommendations Table
sql
CREATE TABLE recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT,
    recommendation TEXT,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);


### gardening_tips Table
sql
CREATE TABLE gardening_tips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    plant_id INT,
    tip TEXT,
    FOREIGN KEY (plant_id) REFERENCES plants(id)
);


## Installation
1. Clone the repository:
   sh
   git clone https://github.com/your-repo/cli-weather-app.git
   cd cli-weather-app
   
2. Install required dependencies:
   sh
   pip install pymysql requests
   
3. Set up the MySQL database and update DB_CONFIG in the script.
4. Obtain an OpenWeatherMap API key and replace API_KEY in the script.

## Usage
Run the program using:
sh
python myfile.py

Follow the interactive prompts to:
- Enter your name and location
- Retrieve weather data
- Get plant recommendations
- Select a plant and view gardening tips

## License
This project is open-source and available under the MIT License.

## Author
Developed by Team 3 

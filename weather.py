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


       
  
 
  

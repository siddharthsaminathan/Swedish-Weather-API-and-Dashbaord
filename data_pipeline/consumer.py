from kafka import KafkaConsumer
import json
import pandas as pd
from sqlalchemy import create_engine
import os

# Kafka Consumer setup
consumer = KafkaConsumer(
    'weather_data',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='weather_processing_group'
)

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/windsurf_db")
engine = create_engine(DATABASE_URL)

def process_weather_data(data):
    """Process incoming weather data and generate insights"""
    df = pd.DataFrame([data])
    
    # Calculate moving averages
    if 'wind_speed' in df.columns:
        df['wind_speed_ma'] = df['wind_speed'].rolling(window=10).mean()
    
    # Store processed data
    try:
        df.to_sql('processed_weather_data', engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Error storing processed data: {e}")

def main():
    print("Starting Weather Data Consumer...")
    for message in consumer:
        try:
            weather_data = message.value
            process_weather_data(weather_data)
            print(f"Processed weather data for location: {weather_data.get('location')}")
        except Exception as e:
            print(f"Error processing message: {e}")

if __name__ == "__main__":
    main()

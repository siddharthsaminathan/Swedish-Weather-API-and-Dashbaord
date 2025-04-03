from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
from kafka import KafkaProducer
import json
from typing import List, Optional
import os

app = FastAPI(
    title="OceanMetrics: Real-time Maritime Analytics Platform",
    description="Enterprise-grade distributed system for real-time weather analytics and maritime conditions monitoring. Built with FastAPI, Apache Kafka, PostgreSQL, and React.",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/windsurf_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Kafka setup
KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Models
class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    timestamp = Column(DateTime)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    temperature = Column(Float)
    wave_height = Column(Float)

class WeatherDataInput(BaseModel):
    location: str
    wind_speed: float
    wind_direction: str
    temperature: float
    wave_height: float

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to WindSurf Analytics API"}

@app.post("/weather-data/")
async def create_weather_data(data: WeatherDataInput):
    db = SessionLocal()
    try:
        weather_data = WeatherData(
            location=data.location,
            timestamp=datetime.utcnow(),
            wind_speed=data.wind_speed,
            wind_direction=data.wind_direction,
            temperature=data.temperature,
            wave_height=data.wave_height
        )
        db.add(weather_data)
        db.commit()
        
        # Send to Kafka
        producer.send('weather_data', value=data.dict())
        
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/weather-data/")
async def get_weather_data():
    db = SessionLocal()
    try:
        data = db.query(WeatherData).order_by(WeatherData.timestamp.desc()).limit(100).all()
        return data
    finally:
        db.close()

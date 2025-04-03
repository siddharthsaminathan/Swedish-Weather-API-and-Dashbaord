from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, Field
from datetime import datetime
from kafka import KafkaProducer
import json
from typing import List, Optional
import os

app = FastAPI(
    title="OceanMetrics: Real-time Maritime Analytics Platform",
    description="""
    Enterprise-grade distributed system for real-time weather analytics and maritime conditions monitoring. 
    Built with FastAPI, Apache Kafka, PostgreSQL, and React.
    
    Key Features:
    * Real-time weather data ingestion and processing
    * Event-driven architecture with Apache Kafka
    * Advanced analytics with moving averages
    * Interactive data visualization
    * RESTful API with automatic documentation
    * Containerized microservices deployment
    """,
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    terms_of_service="http://oceanmetrics.io/terms/",
    contact={
        "name": "OceanMetrics API Support",
        "email": "api@oceanmetrics.io",
        "url": "http://oceanmetrics.io/support",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
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
class WeatherDataBase(BaseModel):
    """
    Base model for weather data measurements.
    """
    location: str = Field(..., description="Geographic location of the measurement", example="Gothenburg, Sweden")
    wind_speed: float = Field(..., description="Wind speed in knots", example=15.5, ge=0)
    wind_direction: str = Field(..., description="Cardinal or intercardinal wind direction", example="NW", pattern="^(N|NE|E|SE|S|SW|W|NW)$")
    temperature: float = Field(..., description="Temperature in Celsius", example=18.5)
    wave_height: float = Field(..., description="Wave height in meters", example=1.2, ge=0)

class WeatherDataCreate(WeatherDataBase):
    """
    Schema for creating a new weather data measurement.
    """
    pass

class WeatherDataResponse(WeatherDataBase):
    """
    Schema for weather data response including database fields.
    """
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

class WeatherData(Base):
    """
    SQLAlchemy model for weather data storage.
    """
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    temperature = Column(Float)
    wave_height = Column(Float)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    """
    Welcome endpoint for OceanMetrics API.
    
    Returns:
        dict: Welcome message and API version information
    """
    return {
        "name": "OceanMetrics API",
        "version": "1.0.0",
        "description": "Enterprise-grade maritime analytics platform",
        "documentation": "/api/docs",
        "status": "operational"
    }

@app.post("/weather-data/")
async def create_weather_data(data: WeatherDataCreate):
    db = SessionLocal()
    try:
        weather_data = WeatherData(
            location=data.location,
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
        return [WeatherDataResponse.from_orm(d) for d in data]
    finally:
        db.close()

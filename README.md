# WindSurf Analytics Platform

A modern data engineering project that processes real-time weather data for windsurfing spots.

## Tech Stack
- FastAPI (Backend API)
- Apache Kafka (Real-time data streaming)
- PostgreSQL (Data storage)
- React (Frontend dashboard)
- Docker (Containerization)

## Features
- Real-time weather data collection from multiple sources
- Data processing and analytics pipeline
- Interactive dashboard for weather insights
- Historical data analysis
- Spot recommendations based on weather conditions

## Setup
1. Install Docker and Docker Compose
2. Clone this repository
3. Run `docker-compose up`
4. Access the dashboard at http://localhost:3000

## Project Structure
```
windsurf-project/
├── backend/           # FastAPI application
├── frontend/          # React dashboard
├── data_pipeline/     # Kafka consumers and producers
├── models/           # Data models and schemas
├── docker/           # Docker configuration
└── docker-compose.yml # Service orchestration
```

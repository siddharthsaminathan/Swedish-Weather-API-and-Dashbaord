# OceanMetrics: Real-time Maritime Analytics Platform

![Tech Stack](https://img.shields.io/badge/Tech%20Stack-FastAPI%20%7C%20React%20%7C%20Kafka%20%7C%20PostgreSQL-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## Overview

OceanMetrics is an enterprise-grade distributed system for real-time maritime weather analytics and condition monitoring. Built with modern technologies and cloud-native principles, it demonstrates expertise in:

- **Distributed Systems**: Event-driven architecture using Apache Kafka
- **Modern Backend**: FastAPI with async support and OpenAPI documentation
- **Data Engineering**: Real-time data processing pipeline with analytics
- **Frontend Development**: React-based interactive dashboard
- **DevOps**: Docker containerization and microservices architecture

## Key Features

- Real-time weather data ingestion and processing
- Event-driven architecture with Apache Kafka
- Advanced analytics with moving averages and trend analysis
- Interactive data visualization dashboard
- RESTful API with automatic OpenAPI documentation
- Containerized microservices deployment
- Scalable PostgreSQL database integration

## Architecture

This project showcases modern software engineering practices:

- **Backend**: FastAPI for high-performance async API
- **Frontend**: React with real-time data updates
- **Message Queue**: Apache Kafka for reliable event streaming
- **Database**: PostgreSQL for robust data persistence
- **Data Pipeline**: Python-based analytics processor
- **Infrastructure**: Docker and docker-compose

For detailed architecture information, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Getting Started

### Prerequisites
- Docker and docker-compose
- Python 3.11+
- Node.js 18+

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/oceanmetrics.git

# Start the services
docker-compose up -d

# Access the application
Frontend: http://localhost:3000
API Docs: http://localhost:8000/api/docs
```

## Development

### Backend API
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Dashboard
```bash
cd frontend
npm install
npm start
```

### Data Pipeline
```bash
cd data_pipeline
pip install -r requirements.txt
python consumer.py
```

## API Documentation

- OpenAPI Documentation: `/api/docs`
- ReDoc Alternative: `/api/redoc`
- Swagger UI: Interactive API testing interface

## Technologies Used

- **Backend Framework**: FastAPI
- **Frontend**: React
- **Message Broker**: Apache Kafka
- **Database**: PostgreSQL
- **Data Processing**: Pandas, SQLAlchemy
- **Containerization**: Docker
- **Documentation**: OpenAPI (Swagger)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [Your Email] - [Your LinkedIn]

Project Link: [https://github.com/yourusername/oceanmetrics](https://github.com/yourusername/oceanmetrics)

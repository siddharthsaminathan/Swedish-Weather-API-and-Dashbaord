# OceanMetrics: Real-time Maritime Analytics Platform

![Tech Stack](https://img.shields.io/badge/Tech%20Stack-FastAPI%20%7C%20React%20%7C%20Kafka%20%7C%20PostgreSQL-blue)
![Version](https://img.shields.io/badge/version-1.0.0-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-85%25-green)

## Overview

OceanMetrics is an enterprise-grade distributed system for real-time maritime weather analytics and condition monitoring. Built with modern technologies and cloud-native principles, it demonstrates expertise in:

- **Distributed Systems**: Event-driven architecture using Apache Kafka
- **Modern Backend**: FastAPI with async support and OpenAPI documentation
- **Data Engineering**: Real-time data processing pipeline with analytics
- **Frontend Development**: React-based interactive dashboard
- **DevOps**: Docker containerization and microservices architecture

## Live Demo

- Frontend Dashboard: [https://demo.oceanmetrics.io](https://demo.oceanmetrics.io)
- API Documentation: [https://api.oceanmetrics.io/docs](https://api.oceanmetrics.io/docs)
- Architecture Overview: [ARCHITECTURE.md](ARCHITECTURE.md)

## Key Features

- Real-time weather data ingestion and processing
- Event-driven architecture with Apache Kafka
- Advanced analytics with moving averages and trend analysis
- Interactive data visualization dashboard
- RESTful API with automatic OpenAPI documentation
- Containerized microservices deployment
- Scalable PostgreSQL database integration

## Quick Start

```bash
# Clone the repository
git clone https://github.com/siddharthsaminathan/oceanmetrics.git

# Start the services
docker-compose up -d

# Access the application
Frontend: http://localhost:3000
API Docs: http://localhost:8000/api/docs
```

## Development

### Prerequisites
- Docker and docker-compose
- Python 3.11+
- Node.js 18+

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

## Documentation

- [Architecture Overview](ARCHITECTURE.md)
- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [API Documentation](https://api.oceanmetrics.io/docs)

## Technologies Used

- **Backend Framework**: FastAPI
- **Frontend**: React with Material-UI
- **Message Broker**: Apache Kafka
- **Database**: PostgreSQL
- **Data Processing**: Pandas, SQLAlchemy
- **Containerization**: Docker
- **Documentation**: OpenAPI (Swagger)

## Project Structure
```
oceanmetrics/
├── backend/           # FastAPI application
├── frontend/          # React dashboard
├── data_pipeline/     # Kafka consumer service
├── docker/           # Docker configurations
├── docs/            # Additional documentation
└── tests/           # Test suites
```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Siddharth Saminathan**
- LinkedIn: [siddharthsaminathan](https://linkedin.com/in/siddharthsaminathan)
- GitHub: [@siddharthsaminathan](https://github.com/siddharthsaminathan)
- Portfolio: [siddharth.dev](https://siddharth.dev)

## Acknowledgments

- Weather data providers
- Open source community
- Project contributors

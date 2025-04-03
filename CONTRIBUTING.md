# Contributing to OceanMetrics

Thank you for your interest in contributing to OceanMetrics! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests
5. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/oceanmetrics.git

# Install dependencies
cd oceanmetrics
docker-compose up -d
```

## Coding Standards

- Follow PEP 8 for Python code
- Use ESLint for JavaScript code
- Write meaningful commit messages following [Conventional Commits](https://www.conventionalcommits.org/)
- Include tests for new features
- Update documentation as needed

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation with details of any interface changes
3. The PR will be merged once you have the sign-off of at least one maintainer

## Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

## Writing Documentation

- Use clear and concise language
- Include code examples where appropriate
- Update the API documentation for new endpoints
- Add docstrings to new functions and classes

## Community

- Join our [Discord server](https://discord.gg/oceanmetrics)
- Follow us on [Twitter](https://twitter.com/oceanmetrics)
- Read our [blog](https://oceanmetrics.io/blog)

## Questions?

Feel free to open an issue or contact the maintainers if you have any questions.

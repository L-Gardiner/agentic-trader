[![CI](https://github.com/L-Gardiner/agentic-trader/actions/workflows/main.yml/badge.svg)](https://github.com/L-Gardiner/agentic-trader/actions/workflows/main.yml)

# Agentic Trader

A modular trading bot platform using domain-driven design, incorporating ML/AI, advanced backend architecture, cloud infrastructure, and trading platform integrations.

## Project Structure

- `api/` - FastAPI backend service
- `domains/` - Core domain logic implementing DDD principles
  - [Backtesting](domains/backtesting/README.md)
  - [Execution](domains/execution/README.md)
  - [ML Pipeline](domains/ml_pipeline/README.md)
  - [Sentiment](domains/sentiment/README.md)
  - [Agents](domains/agents/README.md)
  - [Strategies](domains/strategies/README.md)
- [`infrastructure/`](infrastructure/README.md) - Cloud infrastructure and deployment configurations
- [`frontend-streamlit/`](frontend-streamlit/README.md) - Streamlit dashboard interface
- [`frontend-webapp/`](frontend-webapp/README.md) - React+TypeScript web application
- [`data/`](data/README.md) - Development datasets
- [`scripts/`](scripts/README.md) - Utility scripts and tools
- [`tests/`](tests/README.md) - Integration and system tests
- [`docs/`](docs/README.md) - Project documentation

## Setup

See [setup guide](docs/setup_guide.md) for detailed installation instructions.

## Contributing

Please read our [contribution guidelines](CONTRIBUTING.md) before submitting any changes.

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Project Roadmap](docs/roadmap.md)
- [Setup Guide](docs/setup_guide.md)

## License

This project is shared for educational and portfolio purposes only.
**Commercial use is not permitted.** Contact the author for licensing requests.
© 2025 Luke Gardiner. All rights reserved.

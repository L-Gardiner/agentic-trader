# Setup Guide

## Prerequisites

* Python 3.11 or higher
* Node.js 18 or higher
* Docker and Docker Compose
* AWS CLI configured (for deployment)
* Terraform 1.0 or higher

## Local Development Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/L-Gardiner/agentic-trader.git
   cd agentic-trader
   ```

2. **Set Up Python Environment with Poetry**
   This project uses [Poetry](https://python-poetry.org/) for dependency and virtual environment management.

   **Install Poetry (if not already installed):**

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   **Install dependencies:**

   ```bash
   poetry install
   ```

   **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   # Or use: source $(poetry env info --path)/bin/activate
   ```

   *(Optional)*: If you prefer the classic `poetry shell` command:

   ```bash
   poetry self add poetry-plugin-shell
   poetry shell
   ```

3. **Configure Environment Variables**

   ```bash
   cp .env.template .env
   # Edit .env with your configuration
   ```

4. **Install Pre-commit Hooks**

   ```bash
   poetry run pre-commit install
   ```

5. **Start Local Services**

   ```bash
   docker-compose up -d
   ```

## Development Workflow

1. **API Development**

   * FastAPI server runs at `http://localhost:8000`
   * API documentation at `http://localhost:8000/docs`
   * Make changes in the `api/` directory

2. **Frontend Development**

   * Streamlit dashboard: `http://localhost:8501`
   * React webapp: `http://localhost:3000`
   * Make changes in respective frontend directories

3. **Running Tests**

   ```bash
   poetry run pytest tests/
   ```

4. **Code Quality**
   These are also enforced automatically via pre-commit:

   ```bash
   poetry run black .
   poetry run ruff check .
   poetry run isort .
   ```

## Deployment

1. **Infrastructure Setup**

   ```bash
   cd infrastructure/terraform
   terraform init
   terraform plan
   terraform apply
   ```

2. **Container Deployment**

   ```bash
   # Build images
   docker build -t agentic-trader-api -f infrastructure/docker/api.Dockerfile .
   docker build -t agentic-trader-streamlit -f infrastructure/docker/streamlit.Dockerfile .
   docker build -t agentic-trader-webapp -f infrastructure/docker/webapp.Dockerfile .

   # Push to registry (after setting up ECR)
   docker push your-registry/agentic-trader-api:latest
   ```

## Troubleshooting

### Common Issues

1. **Database Connection**

   * Check PostgreSQL is running: `docker-compose ps`
   * Verify connection string in `.env`

2. **API Errors**

   * Check logs: `docker-compose logs api`
   * Verify environment variables

3. **Frontend Issues**

   * Clear browser cache
   * Check API endpoint configuration
   * Verify node modules: `npm clean-install`

### Getting Help

* Check the project documentation
* Open an issue on GitHub
* Contact the development team

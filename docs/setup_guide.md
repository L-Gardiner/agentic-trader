# Setup Guide

## Prerequisites

- Python 3.10 or higher
- Node.js 18 or higher
- Docker and Docker Compose
- AWS CLI configured (for deployment)
- Terraform 1.0 or higher

## Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-org/agentic-trader.git
   cd agentic-trader
   ```

2. **Set Up Python Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   ```bash
   cp .env.template .env
   # Edit .env with your configuration
   ```

4. **Install Pre-commit Hooks**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

5. **Start Local Services**
   ```bash
   docker-compose up -d
   ```

## Development Workflow

1. **API Development**
   - FastAPI server runs at `http://localhost:8000`
   - API documentation at `http://localhost:8000/docs`
   - Make changes in the `api/` directory

2. **Frontend Development**
   - Streamlit dashboard: `http://localhost:8501`
   - React webapp: `http://localhost:3000`
   - Make changes in respective frontend directories

3. **Running Tests**
   ```bash
   pytest tests/
   ```

4. **Code Quality**
   ```bash
   black .
   ruff check .
   isort .
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
   - Check PostgreSQL is running: `docker-compose ps`
   - Verify connection string in `.env`

2. **API Errors**
   - Check logs: `docker-compose logs api`
   - Verify environment variables

3. **Frontend Issues**
   - Clear browser cache
   - Check API endpoint configuration
   - Verify node modules: `npm clean-install`

### Getting Help

- Check the project documentation
- Open an issue on GitHub
- Contact the development team

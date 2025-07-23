FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt streamlit

# Copy application code
COPY frontend-streamlit/ frontend-streamlit/

# Set environment variables
ENV PYTHONPATH=/app
ENV PORT=8501

# Run the application
CMD ["streamlit", "run", "frontend-streamlit/main.py", "--server.port", "8501", "--server.address", "0.0.0.0"]

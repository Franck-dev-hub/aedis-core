# Base image
FROM python:3.13-slim

# Set working environment
WORKDIR /app

# Install system dependencies
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y postgresql-client
RUN rm -rf /var/lib/apt/lists/*

# Dependency layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Deploy source code
COPY . .

EXPOSE 8000

# Start server with proxy support
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

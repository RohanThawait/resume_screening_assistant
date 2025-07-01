# Use a base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command to run API server
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

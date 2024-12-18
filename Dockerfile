# Use a base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt file 
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./app /app

# Exposing Port on Container
EXPOSE 5000

# Run FastAPI with Uvicorn
CMD ["python", "run.py"]

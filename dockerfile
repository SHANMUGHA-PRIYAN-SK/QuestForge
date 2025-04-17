FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that the app will run on
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=src/web/app.py

# Run the application
CMD ["python", "src/web/app.py"]

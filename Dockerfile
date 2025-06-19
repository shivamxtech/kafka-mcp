FROM python:3.11-slim

# Ensure stdout/stderr are unbuffered
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Use python entrypoint
ENTRYPOINT ["python3", "src/main.py"]
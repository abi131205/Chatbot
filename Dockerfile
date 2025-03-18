# Use official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Start the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "gevent", "--bind", "0.0.0.0:8000", "app:app"]
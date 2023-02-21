# Use an official Python image as the base image
FROM python@sha256:1c7b5a998076ab7aa0a8745ab1461441a5bdc61e366985b9bfe3f4044c2b4503

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable
ENV FLASK_APP=app.py

# Expose the default Flask port
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
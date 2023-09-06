# Use an official Python image as the base image
FROM python@sha256:e5d592c422d6e527cb946ae6abb1886c511a5e163d3543865f5a5b9b61c01584

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
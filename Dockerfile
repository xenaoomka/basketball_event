# Use an official Python image as the base image
FROM python@sha256:9f955672f82a7e7138bcb64bb8352fb0a3025533b8be90a789be5a32526497ca

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
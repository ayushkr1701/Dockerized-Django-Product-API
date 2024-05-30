# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
# To avoid writing .pyc files and unnecessary cluttering in docker environment.
ENV PYTHONDONTWRITEBYTECODE 1 
# To ensure log messages appear in real time.
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files to the working directory
COPY . /code/

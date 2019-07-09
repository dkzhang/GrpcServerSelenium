# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Generate grpc file
RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/the.proto

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 50051

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "server.py"]
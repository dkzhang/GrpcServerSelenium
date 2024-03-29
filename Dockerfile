# Use an official Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file first to install. It can reduce the build workload.
COPY /app/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /app
COPY /app /app

# Generate grpc file
RUN python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./the.proto

# Make port 80 available to the world outside this container
EXPOSE 50051

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python", "server.py"]
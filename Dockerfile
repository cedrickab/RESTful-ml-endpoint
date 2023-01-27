FROM python:3.10.9-buster


# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run the tests
RUN python -m unittest

# Run the application
EXPOSE 5000
CMD [ "flask", "run","--host","127.0.0.1","--port","5000"]

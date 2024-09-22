# Use the official Python image.
FROM python:3.12

# Set the working directory.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the required packages.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container.
COPY . .

# Specify the command to run the Streamlit app.
CMD ["streamlit", "run", "main.py", "--server.port=3000", "--server.address=0.0.0.0"]

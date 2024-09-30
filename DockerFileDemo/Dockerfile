# Use the official Python image
FROM python:3

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Create an output directory for results
RUN mkdir -p /usr/src/app/output

# Start with bash shell to allow interactive use
CMD ["/bin/bash"]

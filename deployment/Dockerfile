# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a Conda environment from the environment.yml file
RUN conda env create -f environment.yml

# Expose the port on which your FastAPI app is running
EXPOSE 8080

# Start your FastAPI app using uvicorn within the Conda environment
CMD ["conda", "run", "-n", "temp-forecast", "uvicorn", "predict-fastapi:app", "--host", "0.0.0.0", "--port", "8080"]

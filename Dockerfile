FROM python:3.10.6

# Set the working directory to /app
WORKDIR /Project1

# Copy local contents into the container
ADD . /Project1

# Install all required dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
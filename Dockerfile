# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Install dependencies required for OpenCV
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=imageCompare/main.py

# Run main.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
# ... 其他 Dockerfile 指令 ...
# 使用 Gunicorn 而不是 Flask 开发服务器
#CMD ["gunicorn", "-b", "0.0.0.0:5000", "imageCompare.main:app"]

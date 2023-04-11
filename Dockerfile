# Our base image
FROM python:3.10-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY . .

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["flask", "run","--host","0.0.0.0","--port","5000"]
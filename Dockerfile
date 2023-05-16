# Use the official Python image from the Alpine distribution as the base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Add necessary build dependencies for Python packages
RUN apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev make

# Copy the requirements file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Remove unnecessary build dependencies
RUN apk del .build-deps

# Copy the entire bot source code
COPY . .

# Runtime config
ENV PYTHONPATH=/app \
    SAGE_API_PASSWORD= \
    SAGE_API_PASSWORD= \
    MATTERMOST_BOT_TOKEN= \
    SAGE_API_QUERY_URL= \
    MATTERMOST_URL= \
    MATTERMOST_TEAM= \
    MATTERMOST_URL= \
    SAGE_EMAIL_ACCOUNT= \
    SAGE_API_GET_TOKEN_URL=

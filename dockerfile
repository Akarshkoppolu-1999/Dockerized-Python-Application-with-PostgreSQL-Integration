FROM python:3.10-slim

WORKDIR /app

# Copy the app file to the container
COPY app.py .

# Install the library to talk to Postgres
RUN pip install psycopg2-binary

# Run the app
CMD ["python", "-u", "app.py"]
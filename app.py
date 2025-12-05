import psycopg2
import time

# Connection details
DB_HOST = "my-postgres"
DB_NAME = "mydb"
DB_USER = "user"
DB_PASS = "pass"

def connect():
    # Retry connection for 30 seconds
    for i in range(5):
        try:
            conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
            return conn
        except psycopg2.OperationalError:
            print("Waiting for database...")
            time.sleep(5)
    raise Exception("Could not connect to database")

conn = connect()
cur = conn.cursor()

# Create Table
print("Creating table...")
cur.execute("CREATE TABLE IF NOT EXISTS data (id SERIAL PRIMARY KEY, message TEXT);")

# Insert Data
print("Inserting data...")
cur.execute("INSERT INTO data (message) VALUES ('Hello from Docker! I am Akarsh');")
conn.commit()

# Read Data
cur.execute("SELECT * FROM data;")
rows = cur.fetchall()
for row in rows:
    print(f"Row: {row}")

conn.close()
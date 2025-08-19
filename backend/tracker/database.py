import psycopg2
import os

def get_connection():
    # Use DATABASE_URL from environment (Render provides this)
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        conn = psycopg2.connect(database_url)
    else:
        # Fallback for local development
        conn = psycopg2.connect(
            dbname="tracker",
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432"
        )
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_applications(
        id SERIAL PRIMARY KEY,
        company_name VARCHAR NOT NULL,
        job_title VARCHAR NOT NULL,
        status VARCHAR DEFAULT 'Applied',
        applied_date VARCHAR 
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized")

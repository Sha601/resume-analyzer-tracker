import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname ="tracker",
        user="postgres",
        password ="postgres",
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
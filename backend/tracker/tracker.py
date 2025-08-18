from .database import get_connection

def add_application(company_name, job_title, status="Applied", applied_date=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO job_applications(company_name, job_title, status, applied_date)
        VALUES(%s, %s, %s, %s)
    """, (company_name, job_title, status, applied_date))
    conn.commit()
    conn.close()
    return {"message": "Application added successfully"}

def view_applications():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM job_applications")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_status(application_id, new_status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE job_applications
        SET status =%s
        WHERE id=%s
    """, (new_status, application_id))
    conn.commit()
    conn.close()
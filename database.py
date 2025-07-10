import sqlite3

DB_NAME = "feedback.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT NOT NULL,
                tester TEXT NOT NULL,
                feedback_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT NOT NULL
            )
        ''')
        conn.commit()

def insert_feedback(version, tester, feedback_type, severity, description):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO feedback (version, tester, feedback_type, severity, description) VALUES (?, ?, ?, ?, ?)",
                  (version, tester, feedback_type, severity, description))
        conn.commit()

def get_feedback():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM feedback")
        return c.fetchall()

def delete_feedback(feedback_id):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
        conn.commit()

def update_feedback(feedback_id, version, tester, feedback_type, severity, description):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("""
            UPDATE feedback
            SET version = ?, tester = ?, feedback_type = ?, severity = ?, description = ?
            WHERE id = ?
        """, (version, tester, feedback_type, severity, description, feedback_id))
        conn.commit()
